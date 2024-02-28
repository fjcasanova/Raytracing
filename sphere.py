from math import sqrt as racine
import numpy as np
class sphere():
    def __init__(self, centre, rayon, couleur, alpha, reflexion = 0):
        self.centre = centre
        self.rayon = rayon
        self.couleur = couleur
        self.alpha = alpha
        self.reflexion = reflexion
    def normal(self, M):
        radial =  M - self.centre
        n = radial.unitaire()
        return n

    def inter(self, depart, direction):

        a = 1
        b = - 2 * direction.unitaire().scalaire(self.centre - depart)
        c = abs(self.centre - depart)**2 - self.rayon**2

        delta = b**2 - 4 * a * c

        if delta == 0 and b < 0:
            return - b / (2 * a)
        elif delta > 0 :
            x1 = (- b - racine(delta)) / (2 * a)
            x2 = (- b + racine(delta)) / (2 * a)
            if min(x1, x2) <= 0 and max(x1, x2) > 0 :
                return max(x1, x2)
            elif min(x1, x2) > 0 :
                return min(x1, x2)
            else:
                return np.inf
        else:
            return np.inf
