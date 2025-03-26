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


ax,ay = (9,9)
bx,by = (3,4)
cx,cy = (7,8)
dx,dy = (0,0)

pointB = Point(bx,by)
pointA = Point(ax,ay)
dist_xBA, dist_yBA = pointB.distancia(ax,ay) #Point AB
dist_xBC, dist_yBC = pointB.distancia(cx,cy) #Point CB
dist_xAC, dist_yAC = pointA.distancia(cx,cy)
dist_AB = pointB.pitagoras(dist_xBA, dist_yBA)
dist_BC = pointB.pitagoras(dist_xBC, dist_yBC)
dist_AC = pointA.pitagoras(dist_xAC, dist_yAC)



middleX_A,middleY_A = pointB.middlePoint(cx,cy)
middleX_B,middleY_B = pointB.middlePoint(ax,ay)
middleX_C,middleY_C = pointA.middlePoint(cx,cy)

print("Distancia entre puntos:")
distancias = {
    "AB" : dist_AB, 
    "BC" : dist_BC, 
    "AC" : dist_AC
    }
print(distancias)

print("Puntos Medios:")

puntosMedios = {
    "XA" : middleX_A, 
    "XB" : middleX_B, 
    "XC" : middleX_C, 
    "YA" : middleY_A,
    "YB" : middleY_B,
    "YC" : middleY_C
    }

print(puntosMedios)



def isAlignInRect(x1,x2,x3,y1,y2,y3) :
    xDivision = (x1-x2)/(x1-x3)
    yDivision = (y1-y2)/(y1-y3)

    return xDivision == yDivision


print("Alineados en la recta:")
if(isAlignInRect(ax,bx,cx,ay,by,cy)):
    print("Si")
else:
    print("No")