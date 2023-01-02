class Settings:
    #Una clase para guardar toda la config de Alien Invasions

    def __init__(self):
        '''Inicializa la config ESTATICAS del juego'''
        #configuracion de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Configuracion de la nave:
        self.ship_limit = 3

        #Configuracion  de las balas:
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #Configuracion de aliens
        self.fleet_drop_speed = 15

        #Rapidez con la que se acelera el juego
        self.speedup_scale = 1.05
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #Puntuacion
        self.alien_points = 50
        #fleet_direction  1 representa derecha; -1 izquierda
        self.fleet_direction = 1 

    def increase_speed(self):
        """incrementa las configuraciones de velocidad """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        