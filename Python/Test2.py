class Objet:
    @property
    def Couleur(self):
        return self._couleur
    @Couleur.setter
    def Couleur(self, value):
        self._couleur = value

    def __init__(self, couleur="Beige"):
        self.Couleur = couleur

    def __str__(self):
        return self.Couleur

    def Methodedeclasse():
        print("Yolo")

class chaise(Objet):
    def __init__(self):
        base.__init__()



ob = Objet()
print(ob)
Objet.Methodedeclasse()