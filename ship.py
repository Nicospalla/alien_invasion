import pygame

class Ship:
    #Desde esta clase gestionamos la nave principal
    
    def __init__(self, ai_game):
        '''Inicializa la nave y configura su posicion inicial'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Cargamos la imagen de la nave y obtenemos su rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #esto coloca inicialmente la nave nueva en el centro inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Dibuja la nave en su ubicacion actual'''
        self.screen.blit(self.image, self.rect)