import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    # Clase general para manejar los recursos y el comportamiento del juego

    def __init__(self):
        '''Inicializa el juego y crea recursos'''
        pygame.init()
        # instaciamos a la clase settings
        self.settings = Settings()

        # display.set_mode define el tamano de la pantalla
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        # Inicializa clase ship y crea la nave
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''Inicia el bucle principal para el juego'''
        while True:
            # Con el _chech_events refactorrizamos el codigo de run_game para que sea mas corto.
            self._check_events()
            self.ship.update()
            self.bullets.update()

            #Nos desasemos de las balas que ya se dispararon
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()

    def _update_screen(self):
        # redibuja la pantalla en cada paso por el bucle
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
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
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == "__main__":
    # Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()
