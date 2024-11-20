import math
class Circle():
    def __init__(self,radius:float="1.0", color:str="red") -> None:
        self.radius=radius
        self.color=color
    def getRadius(self) -> float:
        return self.radius
    def setRadius(self,radius:float) -> None:
        if radius > 0:
            self.radius == radius
        else:
            self.radius == 1.0 
    def getColor(self) -> str:
        return self.color
    def setColor(self,color:str) -> None:
        self.color=color
    def __str__(self) -> str:
        return f"Circleeeeee[rad={self.radius},color={self.color}]"
    def getArea(self) -> float:
        return math.pi*(self.radius**2)

class Cylinder():
    def __init__(self, height:float="1.0", color = str, radius=float):
        Circle.__init__(self,radius,color)
        self.height = height
    def getHeight(self):
        return self.height
    def setHeight(self,height:int):
        self.Height = height 
    def __str__(self):
        return f"Cylinder[height={self.height}, Radius={self.getRadius()}, Color={self.getColor}]"
    def getVolume(self):
        return self.getHeight()*self.getarea()
    
print(str(Cylinder(height=5,radius=5,color="a")))