class registro:
    __vTemp = float
    __vHum = float
    __vPres = float


    def __init__(self, temp, hum, pres):
        self.__vTemp = temp
        self.__vHum = hum
        self.__vPres = pres


    def getTemp(self):
        return self.__vTemp

    def getHum(self):
        return self.__vHum

    def getPres(self):
        return self.__vPres
