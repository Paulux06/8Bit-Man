import pygame

class audioManager:
    def __init__(self):
        pygame.mixer.init(22050, -16, 2, 64)
        self.incNameEffect = pygame.mixer.Sound('Ressources/incNameEffect.wav')
        self.menuSong = pygame.mixer.Sound('Ressources/menuSong.wav')
        self.buttonPressed = pygame.mixer.Sound('Ressources/buttonPressed.wav')

    def playIncNameEffect(self):
        pygame.mixer.Channel(1).play(self.incNameEffect)

    def playButtonPressed(self):
        pygame.mixer.Channel(1).play(self.buttonPressed)

    def playMenuSong(self):
        pygame.mixer.Channel(2).play(self.menuSong)

    def stopMenuSong(self):
        pygame.mixer.Channel(2).stop()