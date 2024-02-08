# OSOBO VIANGHOR CHRIS 

# On définit une classe Fraction dont les attibuts privés sont : num et den
class Fraction:
    def __init__ (self, num, den):
        assert den > 0,"denominateur strictement positif"
        self.num = num
        self.den = den
        
# création d'une méthode spéciale **str (self) qui nous pertmet d'obtenir 'numerateur/denominateur' ou seulement 'numerateur' si le dénominateur vaut 1
    def __str__(self):
        if self.den == 1:
           return str(self.num)
        elif self.den !=1:
            return (str(self.num) + "/" + str(self.den))
        
# méthode de comparaison de deux fractions
    def __eq__(self, other):
        if (other,Fraction):
            return self.num * other.den == self.den * other.num
        else:
            return False
        
# Création des instances
F1, F2, F3, F4 = Fraction(3,4), Fraction(-8,1), Fraction(2,3), Fraction(21,28)

# Affichage des instances à l'aide de la méthode spéciale str
print(F1)
print(F2)
print(F3)
print(F4)

# test de comparaison
print(F1.__eq__(F2))
print(F1.__eq__(F3))
print(F1.__eq__(F4))
print(F2.__eq__(F3))
print(F2.__eq__(F4))
print(F3.__eq__(F4)) 
