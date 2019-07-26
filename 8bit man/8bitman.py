from Ressources.screenManager import screenManager
from Ressources.audioManager import audioManager
import time, pygame

screen = screenManager()
audio = audioManager()

screen.createScreen()
screen.setCaption('8 Bit Man')
screen.setIcon('Ressources/icon.png')
pygame.mouse.set_visible(False)
time.sleep(1)

screen.createIncName('incName', "Paulux inc.", (255,255,255), 32, 'Ressources/font.TTF', 0.6, 0.5)
audio.playIncNameEffect()

time.sleep(2)
screen.delete('incName')
time.sleep(1)

MainRun = True
State = 'affMenu'
playButton = None
settingsButton = None
quitButton = None
menuButton = None
level0Button = None
enButton = None
frButton = None
fpsYButton = None
fpsNButton = None
levelNumber = 0
menuSongPlaying = False
levelMenu = False
MouseVisible = False
levelProgress = 0
charCrouch = False
charJump = False
levelMaxProgress = 0
character = None

while MainRun:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MainRun = False

        if event.type == pygame.MOUSEBUTTONDOWN:            #gestion des clics de souris

            if State == 'menu':
                if playButton.pressed:
                    State = 'affLevelSelect'
                    audio.playButtonPressed()
                if settingsButton.pressed:
                    State = 'affSettings'
                    audio.playButtonPressed()
                if quitButton.pressed:
                    MainRun = False
                    audio.playButtonPressed()
                    State = 'quit'

            if State == 'settings':
                if menuButton.pressed:
                    State = 'affMenu'
                    audio.playButtonPressed()
                if enButton.pressed:
                    screen.language = 'en'
                    State = 'affSettings'
                    audio.playButtonPressed()
                if frButton.pressed:
                    screen.language = 'fr'
                    State = 'affSettings'
                    audio.playButtonPressed()
                if fpsYButton.pressed:
                    screen.updater.dispFPS = True
                    audio.playButtonPressed()
                if fpsNButton.pressed:
                    screen.updater.dispFPS = False
                    audio.playButtonPressed()

            if State == 'levelSelect':
                if level0Button.pressed:
                    State = 'affLevel'
                    levelNumber = 0
                    levelProgress = 0
                    levelMaxProgress = 100
                    audio.playButtonPressed()
                if menuButton.pressed:
                    State = 'affMenu'
                    audio.playButtonPressed()

            if State == 'levelMenu':
                if playButton.pressed:
                    State = 'affLevel'
                    audio.playButtonPressed()
                if menuButton.pressed:
                    State = 'affMenu'
                    audio.playButtonPressed()

        if event.type == pygame.KEYDOWN:                    #gestion des touches de clavier
            if State == 'levelMenu':
                if event.key == pygame.K_ESCAPE:
                    State = 'affLevel'
            if State == 'level':
                if event.key == pygame.K_ESCAPE:
                    State = 'affLevelMenu'
                if event.key == pygame.K_q or event.key == pygame.K_a:
                    if levelProgress > 0:
                        levelProgress -= 1
                        character.setAnimLeft()
                if event.key == pygame.K_s:
                    charCrouch = True
                    character.setAnimIdle()
                else:
                    charCrouch = False
                if event.key == pygame.K_z or event.key == pygame.K_w:
                    charJump = True
                else:
                    charJump = False
                if event.key == pygame.K_d:
                    if levelProgress < levelMaxProgress:
                        levelProgress += 1
                        character.setAnimRight()
                character.setXpos(levelProgress/100)
                character.setYpos(0.5)


    if State == 'level':                                    #gestion visibilitée souris
        if MouseVisible:
            pygame.mouse.set_visible(False)
            MouseVisible = False
    else:
        if not MouseVisible:
            pygame.mouse.set_visible(True)
            MouseVisible = True

    if State == 'affMenu':                                  #gestion des différents écrans
        screen.affMenu()
        playButton = screen.getObject('playButton')
        settingsButton = screen.getObject('settingsButton')
        quitButton = screen.getObject('quitButton')
        State = 'menu'

    if State == 'affLevelMenu':
        screen.affLevelMenu()
        playButton = screen.getObject('resumeButton')
        menuButton = screen.getObject('menuButton')
        State = 'levelMenu'

    if State == 'affLevelSelect':
        screen.affLevelSelect()
        level0Button = screen.getObject('level0Button')
        menuButton = screen.getObject('menuButton')
        State = 'levelSelect'

    if State == 'affLevel':
        screen.affLevel(levelNumber, levelMenu)
        character = screen.getObject('character')
        State = 'level'

    if State == 'affSettings':
        screen.affSettings()
        menuButton = screen.getObject('menuButton')
        enButton = screen.getObject('enButton')
        frButton = screen.getObject('frButton')
        fpsYButton = screen.getObject('fpsYButton')
        fpsNButton = screen.getObject('fpsNButton')
        State = 'settings'

    if State == 'menu':                                      #musique du menu
        if not menuSongPlaying:
            audio.playMenuSong()
            menuSongPlaying = True
    else:
        menuSongPlaying = False
        audio.stopMenuSong()

    if State == 'levelMenu':                                 #gestion menu de level
        levelMenu = True
    else:
        levelMenu = False

screen.quit()