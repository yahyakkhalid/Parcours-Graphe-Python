from src.pile import Pile
from src.file import File

def parcours_profondeur(graph):
    pile = Pile()
    traite = set()  # les sommets traités
    parcours = ''
    for sommet in graph:
        if sommet not in traite:
            traite.add(sommet)  # marquer le sommet comme traité
            pile.empiler(sommet)
            while not pile.estVide():
                pile.visualiser()  # etat de la pile
                sommet_pile = pile.sommet()
                nbr_successeurs_traite = 0
                # visiter le premier successeur non traité
                for successeur in graph[sommet_pile]:
                    if successeur not in traite:
                        traite.add(successeur) # marquer le sommet comme traité
                        pile.empiler(successeur)
                        break  # traiter un seul sommet à la fois
                    else:
                        nbr_successeurs_traite += 1
                # si tous les successeurs du sommet sont traités
                # ou le sommet n'a aucun successeurs
                # i.e: nbr_successeurs_traite == 0 et len(sommet) == 0
                if nbr_successeurs_traite == len(graph[sommet_pile]):
                    pile.depiler()
                    # traitement
                    parcours += str(sommet_pile) + ' '
    print("Les sommets traités:", traite)
    return "resultat: " + parcours


def parcours_largeur(graph):
    file = File()
    traite = set()  # les sommets traités
    parcours = ''
    for sommet in graph:
        if sommet not in traite:
            file.enfiler(sommet)
            while not file.estVide():
                file.visualiser()  # etat de la file
                sommet_file = file.tete()
                traite.add(sommet_file) # marquer le sommet comme traité
                # visiter tous les successeurs non encore traité
                for successeur in graph[sommet_file]:
                    if successeur not in traite:
                        traite.add(successeur) # marquer le sommet comme traité
                        file.enfiler(successeur)
                file.defiler()
                # traitement
                parcours += str(sommet_file) + ' '
    print("Les sommets traités:", traite)
    return "resultat: " + parcours
