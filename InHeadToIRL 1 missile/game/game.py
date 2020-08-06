from   pygame.locals import *
import pygame
import random
import sys
sys.path.append("..")

from constantes import *





class Missile:

    def __init__(self):

        pygame.init()

        self.x = None
        self.y = None

        self.missilePicture = pygame.image.load(MISSILE_CONSTANTES).convert()
        self.defaultCoord   = None

        self.endMissile = None

    def recuperateCoordMissile(self):
        coord = []
        with open(LABY_CONSTANTE, "r") as file:

            for nbLine, ligne in enumerate(file):
                for NoCase, sprite in enumerate(ligne):

                    x = NoCase * CONSTANTE_SIZE_SPRITE
                    y = nbLine * CONSTANTE_SIZE_SPRITE

                    if sprite in ("M"):
                        return x, y

    def setterEndMissile(self, coord):
        self.endMissile = coord

    def assignateCoordMissile(self, x, y):

        self.x = x
        self.y = y

        self.defaultCoord = (x, y)


    def missileMoving(self):

        self.x -= (1 * CONSTANTE_SIZE_SPRITE)


    def displayingMissile(self, window):

        window.blit(self.missilePicture, (self.x, self.y))


    def getterCoordMissile(self):

        return self.x, self.y


    def setterReinitMissile(self):

        self.x, self.y = self.defaultCoord
        

    def reinitMissile(self, coord):

        if self.endMissile == coord:
            self.x = self.defaultCoord[0]
            self.y = self.defaultCoord[1]
            return True

        elif coord is None:
            self.x = self.defaultCoord[0]
            self.y = self.defaultCoord[1]
            return True


    def recupAndDetectMissile(self):
        return self.speed




class Personage:

    def __init__(self):

        pygame.init()

        self.top    = pygame.image.load(PERSO_CONSTANTES[1]).convert()
        self.bot    = pygame.image.load(PERSO_CONSTANTES[4]).convert()
        self.right  = pygame.image.load(PERSO_CONSTANTES[2]).convert()
        self.left   = pygame.image.load(PERSO_CONSTANTES[3]).convert()
        self.noMove = pygame.image.load(PERSO_CONSTANTES[0]).convert()

        self.x = None
        self.y = None

        self.xDeparture = None
        self.yDeparture = None


    def loadPositionDefaultPerso(self, coordDefaultPerso):

        self.x          = coordDefaultPerso[0][0]
        self.y          = coordDefaultPerso[0][1]
        self.xDeparture = coordDefaultPerso[0][0]
        self.yDeparture = coordDefaultPerso[0][1]


    def reinitPerso(self):

        self.x = self.xDeparture
        self.y = self.yDeparture


    def displayingPerso(self, window):
        window.blit(self.noMove, (self.x, self.y))


    def persoReinit(self, coordMissile):

        if coordMissile == (self.x, self.y) or\
           coordMissile == (self.x + CONSTANTE_SIZE_SPRITE, self.y) or\
           coordMissile == (self.x - CONSTANTE_SIZE_SPRITE, self.y) or\
           coordMissile == (self.x, self.y + CONSTANTE_SIZE_SPRITE) or\
           coordMissile == (self.x, self.y - CONSTANTE_SIZE_SPRITE):
            return True

        return False


    def persoReinit1(self, coordMissile):

        if coordMissile == (self.x, self.y): return True
        return False


    def persoMovement(self):

        movement = random.choice(["droite", "gauche", "bas", "haut"])
        return movement


    def movePerso(self, movement):

        if   movement in ("droite"):self.x +=  1 * (CONSTANTE_SIZE_SPRITE * 1)
        elif movement in ("gauche"):self.x += -1 * (CONSTANTE_SIZE_SPRITE * 1)
        elif movement in ("bas")   :self.y += -1 * (CONSTANTE_SIZE_SPRITE * 1)
        elif movement in ("haut")  :self.y +=  1 * (CONSTANTE_SIZE_SPRITE * 1)

    def movePerso2(self, movement):

        if   movement in ("droite"):self.x +=  1 * (CONSTANTE_SIZE_SPRITE * 2)
        elif movement in ("gauche"):self.x += -1 * (CONSTANTE_SIZE_SPRITE * 2)
        elif movement in ("bas")   :self.y += -1 * (CONSTANTE_SIZE_SPRITE * 2)
        elif movement in ("haut")  :self.y +=  1 * (CONSTANTE_SIZE_SPRITE * 2)


    def getterPosPerso(self):
        return self.x, self.y





class Game:

    """Class for gameplay"""

    def __init__(self, nameWindow):

        pygame.init()

        self.window = pygame.display.set_mode((CONSTANTE_WINDOW * 2, CONSTANTE_WINDOW))
        self.background = pygame.image.load(CONSTANTE_BACKGROUND).convert()

        self.mdis = self.mdis = pygame.image.load("pictures/shot.png").convert()
        self.wall = pygame.image.load(WALL_CONSTANTES).convert()

        self.fileLaby = LABY_CONSTANTE

        self.noMove = None

        self.defaultCoordPersonage = []
        self.coordWall = []

        

    def displayingWindow(self):

        self.window.blit(self.background, (0,0))
        self.window.blit(self.background, (CONSTANTE_WINDOW, 0))


    def getterWindow(self):
        return self.window


    def generatingMap(self, window):
        """Put wall of the labyrinth (1) and recompense (R)"""

        with open(self.fileLaby, "r") as file:

            for nbLine, ligne in enumerate(file):
                for NoCase, sprite in enumerate(ligne):

                    x = NoCase * CONSTANTE_SIZE_SPRITE
                    y = nbLine * CONSTANTE_SIZE_SPRITE

                    if   sprite == "1": window.blit(self.wall, (x, y))
                    elif sprite == "P": self.defaultCoordPersonage.append((x, y))
                    elif sprite == "I": window.blit(self.mdis, (x, y))



    def getterPersonnageInitCoord(self):

        return self.defaultCoordPersonage
