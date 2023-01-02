import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import ScoreBoard


class AlienInvasion:
    # Clase general para manejar los recursos y el comportamiento del juego

    def __init__(self):
        '''Inicializa el juego y crea recursos'''
        pygame.init()
        # instaciamos a la clase settings
        self.settings = Settings()

        #Pantalla completa
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')
        #Instanciamos las esttadisticas del juego
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        # Inicializa clase ship y crea la nave
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group() 
        self.bullets = pygame.sprite.Group()

        self._create_fleet()

        #hace el boton de play
        self.play_button = Button(self, "Play")

    def run_game(self):
        '''Inicia el bucle principal para el juego'''
        while True:
            # Con el _chech_events refactorrizamos el codigo de run_game para que sea mas corto.
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _update_screen(self):
        # redibuja la pantalla en cada paso por el bucle
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        #Dibuja el boton de play si la bandera de juego esta inactiva
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Hace visible la ultima pantalla dibujada.
        pygame.display.flip()



    def _check_events(self):
        # Busca eventos de teclado y raton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not  self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            sleep(0.2)
            self.stats.game_active = True

            #elimina los alien y balas remanentes
            self.aliens.empty()
            self.bullets.empty()

            #Crea nueva flota
            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        '''Eventos al presionar una tecla'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''Eventos al soltar una tecla'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Crea una nueva bala y la agrupa en pygame.Group"""
        if  len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
    #Nos desasemos de las balas que ya se dispararon
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #Llama a la funcion que maneja las colisiones entre balas y aliens
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):    
        #Busca balas que hayan colisionado con algun alien
        #Si hay, se deshace de ambos
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self._start_new_level()

    def _start_new_level(self):
        """Cuando no quedan aliens en pantalla, inicia un nuevo nivel,
        esta vez mas dificil"""
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
        #aumenta nivel en pantalla
        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self):
        '''Comprueba si la flota esta en un borde,
        despues actualiza las posiciones de todos los aliens de la flota'''
        self._check_fleet_edges()
        self.aliens.update()
        #Busca colisiones alien-nave
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #Busca aliens llegando al final de la pantalla
        self._check_aliens_bottom()

    def _create_fleet(self):
        '''crea la flota de aliens
        El espacio entre aliens es igual a la anchura de 1 alien'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2* alien_width)
        number_aliens_x = available_space_x // (2* alien_width)
        #Determina el numero de filas de alien que caben en la pantalla
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        #Creamos la primer fila de aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 

    def _ship_hit(self):
        """REsponde al impacto de un alien con la nave"""

        #Disminuye la canitdadd de naves restantes si es mayor a las restantes
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #Se deshace de los aliens y balas restantes
            self.aliens.empty()
            self.bullets.empty()

            #crea la nueva flota y centra la nave
            self._create_fleet()
            self.ship.center_ship()

            #Pausa un poco el juego
            sleep(0.5)
        else:
            self.aliens.empty()
            self.bullets.empty()
            pygame.mouse.set_visible(True)
            self.stats.game_active = False
            


    def _check_aliens_bottom(self):
        '''Comprueba si algun alien llego al fondo de la pantalla'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #trata esta condicion como si hubiese tocado a la nave
                self._ship_hit()
                break

if __name__ == "__main__":
    # Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
