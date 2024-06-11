class Vehicle:

    def __init__(self, speed, initial_location):
        self.__speed = speed
        self.__initial_location = initial_location

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, new_speed):
        self.__speed = new_speed

    def getInitialLocation(self):
        return self.__initial_location

    def setInitialLocation(self, new_location):
        self.__initial_location = new_location


ego = Vehicle(30, [0,0,0])
print(ego.getInitialLocation())