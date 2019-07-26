import pygame

class incName:
    def __init__(self, name, text='Paulux Inc.', color=[255,255,255], size=32, font='Ressources/font.TTF', startPoint=0.8, endPoint=0.5):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.color = color
        self.progress = self.startPoint
        self.Xpos = 0
        self.Ypos = 0
        self.name = name
        self.text = text
        self.font = font
        self.size = size
        self.image = pygame.font.Font(self.font, self.size).render(self.text, True, self.color)

    def update(self, screen):
        if  self.progress > self.endPoint+0.001:
            self.progress -= (self.progress-self.endPoint)/10
        self.Xpos = screen.get_width()/2-self.image.get_width()/2
        self.Ypos = self.progress*screen.get_height()-self.image.get_height()/2
        screen.blit(self.image, [self.Xpos, self.Ypos])


    def delete(self):
        for i in range(255,0,-1):
            self.color = [i,i,i]
            self.image = pygame.font.Font(self.font, self.size).render(self.text, True, self.color)

class menuButton:
    def __init__(self, name, text='Button', Xpos=0, Ypos=0, size=16, color=[255,255,255], font='Ressources/font.TTF'):
        self.name = name
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.color = color
        self.text = text
        self.font = font
        self.size = size
        self.image = pygame.font.Font(font, size).render(text, True, color)
        self.pressed = False

    def update(self, screen):
        self.X = self.Xpos*screen.get_width()-self.image.get_width()/2
        self.Y = self.Ypos*screen.get_height()-self.image.get_height()/2
        Mx, My = pygame.mouse.get_pos()
        if self.X < Mx and Mx < self.X+self.image.get_width() and self.Y < My and My < self.Y+self.image.get_height():
            self.color = [255,255,255]
            self.pressed = True
        else:
            self.color = [200,200,200]
            self.pressed = False
        self.image = pygame.font.Font(self.font, self.size).render(self.text, True, self.color)
        screen.blit(self.image, [self.X, self.Y])

    def delete(self):
        for i in range(255,0,-5):
            self.color = [i,i,i]

class levelViewer:
    def __init__(self, name, picture, Xpos, Ypos):
        self.name = name
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.color = [200,200,200]
        if picture == 0:
            self.pic = pygame.image.load('Ressources/Level0Icon.png')
        self.pic = pygame.transform.scale(self.pic, [128,128])
        self.X = self.Xpos*pygame.display.get_surface().get_width()-64
        self.Y = self.Ypos*pygame.display.get_surface().get_height()-64
        self.pressed = False

    def update(self, screen):
        screen.blit(self.pic, [self.X, self.Y])
        Mx, My = pygame.mouse.get_pos()
        if self.X < Mx and self.X+128 > Mx and self.Y < My and self.Y+128 > My:
            self.color = [255,255,225]
            self.pressed = True
        else:
            self.color = [200,200,200]
            self.pressed = False
        pygame.draw.rect(screen, self.color, [self.X, self.Y, 128, 128], int(self.color[0]/50))

    def delete(self):
        for i in range(255,0,-5):
            self.color = [i,i,i]

class titleText:
    def __init__(self, name, text, font, size, Xpos, Ypos):
        self.name = name
        self.text = text
        self.size = size
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.color = [255,255,255]
        self.image = pygame.font.Font(font, size).render(text, True, self.color)
        self.X = self.Xpos*pygame.display.get_surface().get_width()-self.image.get_width()/2
        self.Y = self.Ypos*pygame.display.get_surface().get_height()-self.image.get_height()/2
        self.pos = True
        self.i = 0

    def update(self, screen):
        if self.i < 10:
            self.i+=1
        else:
            self.i=0
            if self.pos:
                self.pos = False
            else:
                self.pos = True
        if self.pos:
            screen.blit(self.image, [self.X, self.Y])
        else:
            screen.blit(self.image, [self.X, self.Y+10])

    def delete(self):
        for i in range(255,0,-5):
            self.color = [i,i,i]
            self.image = pygame.font.Font('Ressources/font.TTF').render(text, True, self.color)

class character:
    def __init__(self, name):
        self.name = name
        self.idle = [pygame.image.load('Ressources/character/idle(1).png'), pygame.image.load('Ressources/character/idle(2).png')]
        self.left = []
        self.right = []
        self.image = pygame.transform.scale(self.idle[0], [64,128])
        self.pic = 0
        self.progress = 0
        self.anim = self.idle
        self.death = []
        self.Xpos = 0
        self.Ypos = 0

    def update(self, screen):
        if self.progress < 10:
            self.progress += 1
        else:
            self.progress = 0
            if self.pic > len(self.anim)-1:
                self.pic = 0
            else:
                self.image = pygame.transform.scale(self.anim[self.pic], [64,128])
                self.pic += 1
        screen.blit(self.image, [self.Xpos, self.Ypos])

    def delete(self):
        for i in range(255,0,-5):
            self.alpha = i

    def setXpos(self, Xpos):
        self.Xpos = Xpos*pygame.display.get_surface().get_width()-self.image.get_width()/2

    def setYpos(self, Ypos):
        self.Ypos = Ypos*pygame.display.get_surface().get_height()-self.image.get_height()/2

    def getXpos(self, Xpos):
        return self.Xpos/pygame.display.get_surface().get_width()+self.image.get_width()/2

    def getYpos(self, Ypos):
        return self.Ypos/pygame.display.get_surface().get_height()+self.image.get_height()/2
        
    def kill(self):
        self.anim = self.death

    def setAnimIdle(self):
        self.anim = self.idle

    def setAnimLeft(self):
        self.anim = self.left

    def setAnimRight(self):
        self.anim = self.right

class titleCharacter:
    def __init__(self, name, Xpos, Ypos, size):
        self.name = name
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.size = size
        self.anim = [pygame.transform.scale(pygame.image.load('Ressources/character/idle(1).png'), [size, size*2]), pygame.transform.scale(pygame.image.load('Ressources/character/idle(2).png'), [size, size*2])]
        self.pic = False
        self.time = 0
        self.image = self.anim[0]
        self.X = Xpos*pygame.display.get_surface().get_width()-size/2
        self.Y = Ypos*pygame.display.get_surface().get_height()-size

    def update(self, screen):
        if self.time < 10:
            self.time += 1
        else:
            self.time = 0
            if self.pic:
                self.image = self.anim[0]
                self.pic = False
            else:
                self.image = self.anim[1]
                self.pic = True
        screen.blit(self.image, [self.X, self.Y])

    def delete(self):
        pass

class text:
    def __init__(self, name, text, Xpos, Ypos, color, size, font='Ressources/font.TTF'):
        self.name = name
        self.image = pygame.font.Font(font, size).render(text, True, color)
        self.Xpos = Xpos*pygame.display.get_surface().get_width()-self.image.get_width()/2
        self.Ypos = Ypos*pygame.display.get_surface().get_height()-self.image.get_height()/2

    def update(self, screen):
        screen.blit(self.image, [self.Xpos, self.Ypos])

    def delete(self):
        pass

class image:
    def __init__(self, name, image, Xpos, Ypos, Xsize, Ysize):
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(image), [Xsize, Ysize])
        self.Xpos = Xpos*pygame.display.get_surface().get_width()-self.image.get_width()/2
        self.Ypos = Ypos*pygame.display.get_surface().get_height()-self.image.get_height()/2

    def update(self, screen):
        screen.blit(self.image, [self.Xpos, self.Ypos])

    def delete(self):
        pass

class template:
    def __init__(self, name):
        self.name = name

    def update(self, screen):
        pass

    def delete(self):
        pass