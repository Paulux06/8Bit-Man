import pygame
from threading import Thread

class refresher(Thread):
    def __init__(self, screen, scene, fps=60):
        Thread.__init__(self)
        self.screen = screen 
        self.scene = scene
        self.refresh = True
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.quit = False
        self.canRefresh = True
        self.framerate = 0
        self.dispFPS = False
        self.font = pygame.font.SysFont('serif', 10)

    def run(self):
        while self.refresh:
            if self.canRefresh:
                self.screen.fill((0,0,0))
                self.framerate = self.clock.get_fps()
                for item in self.scene:
                    item.update(self.screen)
                if self.dispFPS:
                    self.screen.blit(self.font.render(str(int(self.framerate)), True, [0,255,0]), [0,0])
                pygame.display.flip()
                self.clock.tick(self.fps)