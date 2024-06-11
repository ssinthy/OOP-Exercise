class Location:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Location(x={self.x}, y={self.y} z={self.z})"

class Vehicle:

    def __init__(self, speed, initial_location=Location()):
        self._speed = speed
        self._initial_location = initial_location

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def get_location(self):
        return self._initial_location

    def set_location(self, x, y, z):
        self._initial_location = Location(x, y, z)


ego = Vehicle(30)
print(ego.get_location())
print("Done")