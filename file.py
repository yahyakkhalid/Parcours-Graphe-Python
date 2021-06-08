class File:
    def __init__(self):
        self.file = []

    def enfiler(self, element):
        self.file.insert(0, element)

    def defiler(self):
        if self.estVide():
            raise Exception("La file est vide!")
        self.file.pop()

    def tete(self):
        if self.estVide():
            raise Exception("La file est vide!")
        return self.file[-1]

    def taille(self):
        return len(self.file)

    def estVide(self):
        return self.taille() == 0

    def visualiser(self):
        chaine = ''
        taille = self.taille()
        for i in range(taille):
            chaine += str(self.file[-(i+1)])
            if i < taille-1:
                chaine += " -> "
        print("La file: " + chaine)

    def vider(self):
        del self.file
