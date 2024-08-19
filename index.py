import math 

class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otherX, otherY):
        global distX
        global distY
        if otherX > self.x:
            distX = otherX - self.x
        else: 
            distX = self.x - otherX
        
        if otherY > self.y:
            distY = otherY - self.y
        else :
            distY = self.y  - otherY

        return (distX, distY)
    
    def pitagoras(self, cat, catT):
        h = math.hypot(cat, catT)
        return h
    def middlePoint(self, otherX, otherY):
        return((self.x+otherX )/2, (self.y+otherY) /2)





ax,ay = (-2,-.5)
bx,by = (3.5,1.5)
cx,cy = (-0.5,6)
dx,dy = (0,0)

pointB = Point(bx,by)
pointA = Point(ax,ay)
dist_xA,dist_yA = pointB.distancia(cx,cy) #Point A
dist_AB = pointB.pitagoras(dist_xA, dist_yA)

middleX_A,middleY_A = pointB.middlePoint(cx,cy)
middleX_B,middleY_B = pointB.middlePoint(ax,ay)
middleX_C,middleY_C = pointA.middlePoint(cx,cy)

print("Distancia entre puntos:")
print(dist_AB)
print("A prima:")
print('X =',middleX_A,'; Y =',middleY_A)
print("B prima:")
print('X =',middleX_B,'; Y =',middleY_B)
print("C prima:")
print('X =',middleX_C,'; Y =',middleY_C)



