import pygame
from Ressources.refresher import refresher
from Ressources.objects import incName, menuButton, levelViewer, titleText, character, titleCharacter, text, image
import ctypes
user32 = ctypes.windll.user32

class screenManager:
    def __init__(self):
        pygame.init()
        self.screen = None
        self.scene = []
        self.language = 'en'
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)

    def createScreen(self):
        self.screen = pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN)
        self.updater = refresher(self.screen, self.scene, 30)
        self.updater.start()

    def setCaption(self, text):
        pygame.display.set_caption(text)

    def setIcon(self, file):
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load(file), [32,32]))

    def createIncName(self, name, text, color, size, font, start, end):
        self.scene.append(incName(name, text, color, size, font, start, end))

    def delete(self, name):
        for item in self.scene:
            if item.name == name:
                item.delete()
                self.scene.remove(item)

    def deleteAll(self):
        for i in range(0,len(self.scene)):
            del self.scene[0]

    def quit(self):
        self.deleteAll
        self.updater.refresh = False
        pygame.quit()

    def getObject(self, objectName):
        for item in self.scene:
            if objectName == item.name:
                return item

    def affMenu(self):
        self.deleteAll()
        self.scene.append(image('image', 'Ressources/back.jpg', 0.5, 0.5, self.width, self.height))
        self.scene.append(titleText('titleText', '8 Bit Man', 'Ressources/font.TTF', 64, 0.7, 0.2))
        self.scene.append(titleCharacter('titleCharacter', 0.7, 0.6, 128))
        if self.language == 'fr':
            self.scene.append(menuButton('playButton', 'Jouer', 0.2, 0.3, 24))
            self.scene.append(menuButton('settingsButton', 'Parametres', 0.2, 0.5, 24))
            self.scene.append(menuButton('quitButton', 'Quitter', 0.2, 0.7 , 24))
        if self.language == 'en':
            self.scene.append(menuButton('playButton', 'Play', 0.2, 0.3, 24))
            self.scene.append(menuButton('settingsButton', 'Settings', 0.2, 0.5, 24))
            self.scene.append(menuButton('quitButton', 'Quit', 0.2, 0.7 , 24))

    def affSettings(self):
        self.deleteAll()
        self.scene.append(image('image', 'Ressources/back.jpg', 0.5, 0.5, self.width, self.height))
        if self.language == 'fr':
            self.scene.append(text('textLangue', 'Langage:', 0.2, 0.25, [255,255,255], 20))
            self.scene.append(menuButton('enButton', 'Anglais', 0.25, 0.3, 16))
            self.scene.append(menuButton('frButton', 'Francais', 0.35, 0.3, 16))
            self.scene.append(text('textFPS', 'Afficher les FPS:', 0.2, 0.4, [255,255,255], 20))
            self.scene.append(menuButton('fpsYButton', 'Oui', 0.25, 0.45, 16))
            self.scene.append(menuButton('fpsNButton', 'Non', 0.35, 0.45, 16))
            self.scene.append(menuButton('menuButton', 'Retour', 0.1, 0.9))
        if self.language == 'en':
            self.scene.append(text('textLangue', 'Language:', 0.2, 0.25, [255,255,255], 20))
            self.scene.append(menuButton('enButton', 'English', 0.25, 0.3, 16))
            self.scene.append(menuButton('frButton', 'French', 0.35, 0.3, 16))
            self.scene.append(text('textFPS', 'Display FPS:', 0.2, 0.4, [255,255,255], 20))
            self.scene.append(menuButton('fpsYButton', 'Yes', 0.25, 0.45, 16))
            self.scene.append(menuButton('fpsNButton', 'No', 0.35, 0.45, 16))
            self.scene.append(menuButton('menuButton', 'Return', 0.1, 0.9))

    def affLevelSelect(self):
        self.deleteAll()
        self.scene.append(image('image', 'Ressources/back.jpg', 0.5, 0.5, self.width, self.height))
        self.scene.append(levelViewer('level0Button', 0, 0.4, 0.3))
        if self.language == 'fr':
            self.scene.append(menuButton('menuButton', 'Retour', 0.1, 0.9))
        if self.language == 'en':
            self.scene.append(menuButton('menuButton', 'Return', 0.1, 0.9))

    def affLevel(self, level, levelmenu):
        if levelmenu:
            self.delete('resumeButton')
            self.delete('menuButton')
        else:
            self.deleteAll()
        self.scene.append(character('character'))

    def affLevelMenu(self):
        if self.language == 'fr':
            self.scene.append(menuButton('resumeButton', 'Reprendre', 0.5, 0.45, 16))
            self.scene.append(menuButton('menuButton', 'Quitter', 0.5, 0.55, 16))
        if self.language == 'en':
            self.scene.append(menuButton('resumeButton', 'Resume', 0.5, 0.45, 16))
            self.scene.append(menuButton('menuButton', 'Quit', 0.5, 0.55, 16))