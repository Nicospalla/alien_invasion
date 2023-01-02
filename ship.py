import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #Desde esta clase gestionamos la nave principal
    
    def __init__(self, ai_game):
        '''Inicializa la nave y configura su posicion inicial'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Cargamos la imagen de la nave y obtenemos su rect.
        self.image = pygame.image.load('images/abc.bmp')
        self.rect = self.image.get_rect()

        #esto coloca inicialmente la nave nueva en el centro inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        #Ahora guardamos un valor decimal para la nave.(se realciona con el self.setting -> ai_game.settings)
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Actualiza el movimiento de la nave en funcion de la bandera de movimiento'''
        #Paso dos, actualizamos valor de x de la nave, no de rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        '''Dibuja la nave en su ubicacion actual'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Centra la nave en la pantalla'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)