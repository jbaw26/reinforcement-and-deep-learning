from   pygame.locals import *
import pygame


from constantes   import *
from environement import *
from avatar       import *
from learning     import *



Map = Map()
Map.generateWindow()
Map.recuperateWallCoord()

window = Map.getterWindow()


Avatar = Avatar()
Avatar.setterDefaultPosition()
Avatar.displayingPerso(window)


Missile = Missile()
Missile.setterEndMissile()



LearningWhenMove  = LearningWhenMove()
LearningWhereMove = LearningWhereMove()



Missile.transformationMissile()

generation = True
inHead = True
while generation:

    Map.eventPygame(5)

    if inHead is False:
        Map.displayingBackground(True)
        Map.displayingWall()






    where = None
    while inHead:

        Map.eventPygame(where)

        Map.displayingBackground(False)
        Map.displayingWall()




        Missile.movement()
        endTraject = Missile.replaceMissileIfEnd()
        if endTraject is True:
            Avatar.setterPosition()

        Missile.displayTransformation(window)
        coordMissiles = Missile.getterMissileCoords()



        #Avatar.movement(window, move)
        Avatar.replaceAvatarIfEnd()
        coordAvatar = Avatar.getterPosition()




        whenMoveModel = LearningWhenMove.getterModel()
        if whenMoveModel == None:
            isDead = LearningWhenMove.distanceCritData(coordAvatar, coordMissiles)
            LearningWhenMove.trainMoving()
            LearningWhenMove.makeTreshold()

            if isDead is True:
                Missile.reinitMissile()
                Avatar.setterPosition() 


        missileDetection = []
        if whenMoveModel != None:

            where = None
            isDead = False
            coordAvatar = Avatar.getterPosition()
            coordMissiles = Missile.getterMissileCoords()

            for coord in coordMissiles:
                canDie = LearningWhenMove.prediction(coordAvatar, coord)

                modelWhere = LearningWhereMove.getterModel()

                if canDie == 1 and modelWhere == None:
                    missileDetection.append(coord)

                    move = Avatar.choiceAMovement()
                    Avatar.movement(window, move)

                    coordAvatar = Avatar.getterPosition()

                    isDead = coordAvatar in coordMissiles
                    if isDead is True:
                        Missile.reinitMissile()
                        Avatar.setterPosition()
                        break

                    else:
                        LearningWhereMove.recuperateData(coordAvatar, coord, move)
                        LearningWhereMove.trainning()

                        Map.displayingBackground(False)
                        Map.displayingWall()
                        [Missile.displayMissileByCoord(window, missile)
                         for missile in coordMissiles]
                        [Avatar.detectionMissile(coord, window) for coord in missileDetection]
                        Avatar.displayingPerso(window)
                        pygame.display.flip()




        if isDead is False:
            Missile.displayMissile(window)
            [Avatar.detectionMissile(coord, window) for coord in missileDetection]
            Avatar.displayingPerso(window)
            pygame.display.flip()




        whenMoveModel  = LearningWhenMove.getterModel()
        whereMoveModel = LearningWhereMove.getterModel()
        if whenMoveModel != None and whereMoveModel != None:
            Missile.reinitMissile()
            missileDetection = []
            inHead = False







    Map.displayingBackground(True)
    Map.displayingWall()




    Missile.movement()
    Missile.displayTransformation(window)

    coordMissiles = Missile.getterMissileCoords()
    coordAvatar = Avatar.getterPosition()

    missileDetection = []
    for coord in coordMissiles:
        when  = LearningWhenMove.prediction(coordAvatar, coord)
        where = LearningWhereMove.prediction(coordAvatar, coord)

        if when == 1:
            missileDetection.append(coord)

            if where != False:
                Avatar.movement(window, where)
                Avatar.displayingPerso(window)

                Map.displayingBackground(True)
                Map.displayingWall()
                [Missile.displayMissileByCoord(window, missile)
                for missile in coordMissiles]
                [Avatar.detectionMissile(coord, window) for coord in missileDetection]
                Avatar.displayingPerso(window)

                pygame.display.flip()




    for coord in coordMissiles:
        endTraject = Missile.replaceMissileIfEndByCoord(coord)
        if endTraject is True:

            LearningWhenMove.setterData()
            LearningWhereMove.setterData()
            Missile.transformationMissile()

            Avatar.setterPosition()
            Missile.reinitMissile()

            inHead = True
            break



    Map.displayingBackground(True)
    Map.displayingWall()
    [Missile.displayMissileByCoord(window, missile)
     for missile in coordMissiles]
    [Avatar.detectionMissile(coord, window) for coord in missileDetection]
    Avatar.displayingPerso(window)
    pygame.display.flip()











