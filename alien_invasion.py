import sys
import pygame

from settings import Settings
from ship import Ship
class AlienInvasion:
    #Clase general para manejar los recursos y el comportamiento del juego

    def __init__(self):
        '''Inicializa el juego y crea recursos'''
        pygame.init()
        self.settings = Settings()

        #display.set_mode define el tamano de la pantalla
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #Configura el color de fondo de la pantalla
        pygame.display.set_caption('Alien Invasion')
        #Inicializa clase ship y crea la nave
        self.ship = Ship(self)
    
    def run_game(self):
        '''Inicia el bucle principal para el juego'''
        while True:
            # Busca eventos de teclado y raton
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redibuja la pantalla en cada paso por el bucle
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #Hace visible la ultima pantalla dibujada.
            pygame.display.flip()

if __name__ == "__main__":
    #Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()