from enum import Enum

class VehicleType(Enum):
    EMERGENCY = "EMERGENCY"
    EGO = "EGO"
    BICYCLE = "BICYCLE"
    MOTORBIKE = "MOTORBIKE" 
    NORMAL = "NORMAL"

class Location:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Location(x={self.x}, y={self.y}, z={self.z})"

class Vehicle:
    
    def __init__(self, speed = 0, location = Location(0,0,0), type = VehicleType.NPC, is_on_autopilot = False):
        self._speed = speed
        self._location = location
        self._type = type
        self._is_on_autopilot = is_on_autopilot

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def get_location(self):
        return self._location

    def set_location(self, x, y, z):
        self._location = Location(x, y, z)

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_autopilot_status(self):
        return self._is_on_autopilot

    def set_autopilot_status(self, bool):
        self._is_on_autopilot = bool

    def __repr__(self):
        return f"Ego(speed={self._speed}, location={self._location} type={self._type})"


class EgoVehicle(Vehicle):

    def __init__(self, speed, location):
        super().__init__(speed, location, VehicleType.EGO)

    def addCamera():
        pass

ego = EgoVehicle(30, Location(1,2,3))
print(ego)