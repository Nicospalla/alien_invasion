class GameStats:
    '''Sigue las estadisticas del juego'''
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        #Bandera que Inicia Alien Invasion en estado activo
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """inicializa las estadisticas que pueden cambiar durante el juego"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1