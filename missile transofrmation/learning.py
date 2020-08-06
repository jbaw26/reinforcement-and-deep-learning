from scipy.spatial import distance
from sklearn.neural_network import MLPClassifier

import numpy as np

class LearningWhereMove:

    def __init__(self):

        self.lengthData = 100

        self.dataX = []
        self.dataY = []
        
        self.model = None


    def setterData(self):
        self.dataX = []
        self.dataY = []
        
        self.model = None


    def recuperateData(self, coordPerso, coordMissile, move):

        xPerso, yPerso     = coordPerso
        xMissile, yMissile = coordMissile

        axeX = 0
        axeY = 0

        if   xMissile - xPerso > 0 and yMissile == yPerso:
            axeX = -1
        elif xMissile - xPerso < 0 and yMissile == yPerso:
            axeX = 1
        elif yMissile - yPerso > 0 and xMissile == xPerso:
            axeY = -1
        elif yMissile - yPerso < 0 and xMissile == xPerso:
            axeY = 1
        elif yMissile == xMissile:
            axeX = 1
            axeY = 1
        elif xMissile == yPerso:
            axeX = -1
            axeY = -1


        #print(axeX, axeY, move, coordPerso, coordMissile, "\n")
        dicoMove = {"droite":0, "gauche":0, "haut":0, "bas":0, "none":0}
        dicoMove[move] = 1

        self.dataX.append(np.array([axeX, axeY]))
        self.dataY.append(np.array([v for k, v in dicoMove.items()]))




    def trainning(self):
        if len(self.dataX) >= self.lengthData:

            X = np.array(self.dataX)
            Y = np.array(self.dataY)

            clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                                 hidden_layer_sizes=(100, 80, 20), random_state=1)
            clf.fit(X, Y)

            scoring = clf.score(X, Y)
            self.model = clf

            print(scoring)

            
            data = [[1, 1], [0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1]]
            for i in data:
                print(self.model.predict(np.array(i).reshape(1, -1)))



    def getterModel(self):
        return self.model


    def prediction(self, coordPerso, coordMissile):

        xPerso, yPerso     = coordPerso
        xMissile, yMissile = coordMissile

        axeX = 0
        axeY = 0

        if   xMissile - xPerso > 0 and yMissile == yPerso:
            axeX = -1
        elif xMissile - xPerso < 0 and yMissile == yPerso:
            axeX = 1
        elif yMissile - yPerso > 0 and xMissile == xPerso:
            axeY = -1
        elif yMissile - yPerso < 0 and xMissile == xPerso:
            axeY = 1
        elif yMissile == xMissile:
            axeX = 1
            axeY = 1
        elif xMissile == yPerso:
            axeX = -1
            axeY = -1

        data = np.array([axeX, axeY]).reshape(1, -1)
        prediction = self.model.predict(data)

        movement = ["droite", "gauche", "haut", "bas", "none"]

        for nb, i in enumerate(prediction[0]):
            if i == 1:
                return movement[nb]

        return False




class LearningWhenMove:

    def __init__(self):

        self.lengthData = 2000

        self.dataX = []
        self.dataY = []

        self.criticLimit = None

        self.model = None


    def setterData(self):
        self.dataX = []
        self.dataY = []

        self.criticLimit = None

        self.model = None


    def distanceCritData(self, coordAvatar, coordMissiles):

        for coord in coordMissiles:

            isDead = 1 if coordAvatar == coord else 0
            dist = distance.euclidean(coordAvatar, coord)

            self.dataX.append(np.array([dist]))
            self.dataY.append(np.array(isDead))

            if isDead == 1:
                return True

        return False



    def trainMoving(self):

        if len(self.dataX) >= self.lengthData:

            X = np.array(self.dataX)
            Y = np.array(self.dataY)

            clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                                 hidden_layer_sizes=(20, 5), random_state=1)
            clf.fit(X, Y)

            scoring = clf.score(X, Y)
            self.model = clf

            print(scoring)


    def getterModel(self):
        return self.model



    def makeTreshold(self):

        if self.model != None:

            threshold = [0, 10, 20, 40, 60]
            for i in threshold:
                print(self.model.predict(np.array([i]).reshape(1, -1)))

            for i in [0, 20, 40, 60]:
                limit = self.model.predict(np.array([i]).reshape(1, -1))
                if limit != 1:
                    self.criticLimit = i
                    break

            print("with limit: ", self.criticLimit)
            for i in threshold:
                data = np.array([i - self.criticLimit]).reshape(1, -1)
                print(self.model.predict(data))



    def setterData(self):
        self.dataX = []
        self.dataY = []



    def prediction(self, coordAvatar, coordMissiles):

        predicts = []

        dist = distance.euclidean(coordAvatar, coordMissiles)

        data = np.array([dist - self.criticLimit]).reshape(1, -1)
        prediction = self.model.predict(data)

        return prediction[0]














