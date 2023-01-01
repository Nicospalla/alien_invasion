class Settings:
    #Una clase para guardar toda la config de Alien Invasions

    def __init__(self):
        '''Inicializa la config del juego'''
        #configuracion de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Configuracion de la nave:
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Configuracion  de las balas:
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #Configuracion de aliens
        self.alien_speed = 0.8
        """estaba en 10 el drop speed"""
        self.fleet_drop_speed = 15
        #fleet_direction  1 representa derecha; -1 izquierda
        self.fleet_direction = 1 