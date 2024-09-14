class object:
    def __init__(self, name, mass, velocity, position):
        self.name = name
        self.mass = mass
        self.velocity = velocity # [vx, vy]
        self.position = position # [x, y]
        self.acceleration = [0,0] # Acceleration always starts at 0

obj = object("P", 2, 3, [4, 6])
print(obj.name, "is at position:", obj.position)

