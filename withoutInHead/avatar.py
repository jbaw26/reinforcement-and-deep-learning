from   pygame.locals import *
from   scipy.spatial import distance

import pygame
import random


from constantes import *


class MissileAvatar:

    def __init__(self):

        pygame.init()

        self.fileLaby       = LABY_CONSTANTE
        self.missilePicture = pygame.image.load(MISSILE_CONSTANTES).convert()

        self.x = None
        self.y = None
        self.defaultCoordX = None
        self.defaultCoordY = None
        self.windowSize = CONSTANTE_WINDOW

        self.right   = []
        self.left    = []
        self.missile = []


    def setterCoordMissile(self, coords):
        x, y = coords

        self.x = x
        self.y = y

    def setterSelfMissiles(self, listMissiles):
        self.missile = listMissiles


    def setterEndMissile(self):
        with open(self.fileLaby, "r") as file:

            for nbLine, ligne in enumerate(file):
                for NoCase, sprite in enumerate(ligne):

                    x = NoCase * CONSTANTE_SIZE_SPRITE
                    y = nbLine * CONSTANTE_SIZE_SPRITE

                    if sprite == "M":
                        self.x = x
                        self.y = y
                        self.defaultCoordX = x
                        self.defaultCoordY = y


    def movement(self):
        self.y += (1 * CONSTANTE_SIZE_SPRITE)


    def replaceMissileIfEnd(self):

        if self.x <= 0 or self.x >= self.windowSize or\
           self.y <= 0 or self.y >= self.windowSize:
            self.x = self.defaultCoordX
            self.y = self.defaultCoordY
            return True


    def replaceMissileIfEndByCoord(self, coord):
        x, y = coord

        if x <= 0 or x >= self.windowSize or\
           y <= 0 or y >= self.windowSize:
            x = self.defaultCoordX
            y = self.defaultCoordY
            return True


    def reinitMissile(self):
        self.x = self.defaultCoordX
        self.y = self.defaultCoordY


    def getterCoordinates(self):
        return (self.x, self.y)


    def transformationMissile(self):

        coords = [0, 1]

        self.right = [(random.choice(coords), random.choice(coords))
                      for i in range(random.randrange(1, 10))]

        self.left  = [(random.choice(coords), random.choice(coords))
                      for i in range(random.randrange(1, 10))]


    def displayTransformation(self, window):

        x = self.x
        y = self.y

        missileContainer = []

        for index, (xR, yR) in enumerate(self.right):
            x += (xR * CONSTANTE_SIZE_SPRITE)
            y += (yR * CONSTANTE_SIZE_SPRITE)

            window.blit(self.missilePicture, (x, y))
            missileContainer.append((x, y))


        x = self.x
        y = self.y

        for index, (xL, yL) in enumerate(self.left):
            x -= (xL * CONSTANTE_SIZE_SPRITE)
            y -= (yL * CONSTANTE_SIZE_SPRITE)

            window.blit(self.missilePicture, (x, y))
            missileContainer.append((x, y))

        missileContainer.append((self.x, self.y))
        self.missile = missileContainer


    def getterTransformation(self):
        return self.missile




    def getterMissileCoords(self):
        return self.missile

    def getterDefaultCoord(self):
        return (self.defaultCoordX, self.defaultCoordY)

    def displayMissileByCoord(self, window, coord):
        window.blit(self.missilePicture, coord)

    def displayMissile(self, window):
        window.blit(self.missilePicture, (self.x, self.y))










class Avatar:

    def __init__(self):

        pygame.init()

        self.top      = pygame.image.load(PERSO_CONSTANTES[1]).convert()
        self.bot      = pygame.image.load(PERSO_CONSTANTES[4]).convert()
        self.right    = pygame.image.load(PERSO_CONSTANTES[2]).convert()
        self.left     = pygame.image.load(PERSO_CONSTANTES[3]).convert()
        self.noMove   = pygame.image.load(PERSO_CONSTANTES[0]).convert()
        self.detected = pygame.image.load(SHOT_DETECTED).convert()
        self.death    = pygame.image.load(CONSTANTE_DEATH).convert()

        self.x = None
        self.y = None
        self.defaultCoordX = None
        self.defaultCoordY = None


        self.fileLaby    = LABY_CONSTANTE

        self.movePicture = {"droite":self.right, "gauche":self.left,
                            "haut": self.top, "bas": self.bot, "none":self.noMove}

        self.moveAxis    = {"droite":(1, 0), "gauche":(-1, 0),
                            "haut": (0, -1),  "bas": (0, 1), "none": (0, 0)}

        self.windowSize = CONSTANTE_WINDOW


    def setterDefaultPosition(self):

        with open(self.fileLaby, "r") as file:

            for nbLine, ligne in enumerate(file):
                for NoCase, sprite in enumerate(ligne):

                    x = NoCase * CONSTANTE_SIZE_SPRITE
                    y = nbLine * CONSTANTE_SIZE_SPRITE

                    if sprite == "P":
                        self.x = x
                        self.y = y
                        self.defaultCoordX = x
                        self.defaultCoordY = y


    def getterPosition(self):
        return (self.x, self.y)



    def choiceAMovement(self):
        movement = random.choice(["droite", "gauche", "haut", "bas", "none"])
        return movement



    def movement(self, window, move):

        picture = self.movePicture[move]
        window.blit(picture, (self.x, self.y))

        self.x += self.moveAxis[move][0] * CONSTANTE_SIZE_SPRITE
        self.y += self.moveAxis[move][1] * CONSTANTE_SIZE_SPRITE


    def replaceAvatarIfEnd(self):
        if self.x <= 0 or self.x >= self.windowSize or\
           self.y <= 0 or self.y >= self.windowSize:
            self.x = self.defaultCoordX
            self.y = self.defaultCoordY



    def detectionMissile(self, coordMissile, window):
        window.blit(self.detected, (coordMissile))


    def setterPosition(self):
        self.x = self.defaultCoordX
        self.y = self.defaultCoordY


    def deathPerso(self, coord):
        if coord == (self.x, self.y):
            return True

        return False
    

    def displayingPerso(self, window):
        window.blit(self.noMove, (self.x, self.y))


    def displayDeath(self, window, coord):
        window.blit(self.death, coord)




































