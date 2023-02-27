import math

class Tg:
    def __init__(self, angle):
        self.angle = math.radians(angle)
        
    def sin(self):
        return math.sin(self.angle)
    
    def cos(self):
        return math.cos(self.angle)
    
    def tan(self):
        return math.tan(self.angle)
    
    def cosec(self):
        return 1 / self.sin()
    
    def sec(self):
        return 1 / self.cos()
    
    def cot(self):
        return 1 / self.tan()

angle = float(input("Enter the angle in degrees: "))

tg = Tg(angle)

print("Sine: ", round(tg.sin(),2))
print("Cosine: ", round(tg.cos(),2))
print("Tangent: ", round(tg.tan(),2))
print("Cosecant: ", round(tg.cosec(),2))
print("Secant: ", round(tg.sec(),2))
print("Cotangent: ", round(tg.cot(),2))
