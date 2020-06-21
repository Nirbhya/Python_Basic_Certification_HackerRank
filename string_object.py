//python string representation of object 

class Car:
    def __init__(self,ms,un):
        self.max_speed=ms
        self.speed_unit=un;
    def __repr__(self):
        return 'Car with the maximum speed of %s %s' % (self.max_speed,self.speed_unit)
class Boat:
    def __init__(self,ms):
            self.max_speed=ms
    def __repr__(self):
        return 'Boat with the maximum speed of %s knots' % (self.max_speed)
