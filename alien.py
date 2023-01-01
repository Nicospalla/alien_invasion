import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''Una clase para representar a los alien'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

    #Carga la imagen del alien y configura atributo rect.
        self.image = pygame.image.load('images/nico_alien.bmp')
        self.rect = self.image.get_rect()

    #Inicializa un alien en la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    #Guarda la posicion exacta del alien
        self.x = float(self.rect.x)

    def check_edges(self):
        #Devuelve True si el alien esta en el borde de la pantalla
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        #mueve alien hacia la izquiera o la derecha (-1 o 1)
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x