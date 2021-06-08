class Pile:
    def __init__(self):
        self.pile = []

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        if self.estVide():
            raise Exception("La pile est vide!")
        del self.pile[-1]

    def sommet(self):
        if self.estVide():
            raise Exception("La pile est vide!")
        return self.pile[-1]

    def taille(self):
        return len(self.pile)

    def estVide(self):
        return self.taille() == 0

    def visualiser(self):
        chaine = ''
        taille = self.taille()
        for i in range(taille):
            chaine += str(self.pile[-(i + 1)])
            if i < taille-1:
                chaine += " -> "
        print("La pile: " + chaine)

    def vider(self):
        del self.pile
