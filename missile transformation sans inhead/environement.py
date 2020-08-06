from   pygame.locals import *
import pygame

from constantes import *


class Map:

    def __init__(self):

        self.labyFile  = LABY_CONSTANTE
        self.coordWall = []

        self.wall       = None
        self.window     = None
        self.background = None


    def generateWindow(self):

        pygame.init()
        
        self.window       = pygame.display.set_mode((CONSTANTE_WINDOW, CONSTANTE_WINDOW))
        self.background   = pygame.image.load(CONSTANTE_BACKGROUND).convert()
        self.noBackground = pygame.image.load(CONSTANTE_NO_BACKGROUND).convert()
        self.wall         = pygame.image.load(WALL_CONSTANTES).convert()


    def displayingBackground(self, background):
        if background is True:
            self.window.blit(self.background, (0,0))
        else:
            self.window.blit(self.noBackground, (0,0))


    def getterWindow(self):
        return self.window



    def recuperateWallCoord(self):
        """Put wall of the labyrinth (1) and recompense (R)"""

        with open(self.labyFile, "r") as file:

            for nbLine, ligne in enumerate(file):
                for NoCase, sprite in enumerate(ligne):

                    x = NoCase * CONSTANTE_SIZE_SPRITE
                    y = nbLine * CONSTANTE_SIZE_SPRITE

                    if   sprite == "1":
                        coord = (x, y)
                        self.coordWall.append(coord)


    def displayingWall(self):

        [self.window.blit(self.wall, coord)
         for coord in self.coordWall]


    def getterCoordWall(self):
        return self.coordWall
            

    def eventPygame(self, nbTciks):

        if nbTciks != None:
            pygame.time.Clock().tick(nbTciks)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
