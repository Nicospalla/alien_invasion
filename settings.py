class Settings:
    #Una clase para guardar toda la config de Alien Invasions

    def __init__(self):
        '''Inicializa la config del juego'''
        #configuracion de pantalla
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230,230,230)

        #Configuracion de la nave:
        self.ship_speed = 0.8

        #Configuracion  de las balas:
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3