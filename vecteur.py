import math
class vecteur() :
    def __init__(self, x, y, z) :
        (self.x, self.y, self.z) = (x, y, z)

    def __add__(self, other) :
        return vecteur(self.x + other.x , self.y + other.y , self.z + other.z)

    def __sub__(self, other) :
        return vecteur(self.x - other.x , self.y - other.y , self.z - other.z)

    def __neg__(self) :
        return vecteur(- self.x, - self.y, - self.z)

    def __mul__(self, other) :
        return vecteur(self.x * other , self.y * other , self.z * other)

    def __rmul__(self, other) :
        return other*self

    def scalaire(self, other) :
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __abs__(self) :
        return math.sqrt(self.scalaire(self))

    def unitaire(self) :
        return vecteur(self.x , self.y, self.z) * (1.0 / abs(self))

    def vecteur2coord(self) :
        return (self.x, self.y, self.z)

    def rgb(self) :
        self.x = min(self.x, 255)
        self.x = max(self.x, 0)
        self.y = min(self.y, 255)
        self.y = max(self.y, 0)
        self.z = min(self.z, 255)
        self.z = max(self.z, 0)
        return(int(self.x), int(self.y), int(self.z))
