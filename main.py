from parcours import parcours_profondeur, parcours_largeur

# representation du graph par une liste d'adjacences
graph1 = {
    0: [1],
    1: [4, 5],
    2: [0, 3],
    3: [1, 7],
    4: [],
    5: [7],
    6: [3],
    7: [5, 6, 8],
    8: [5]
}

print("# Parcours en profondeur")
print(parcours_profondeur(graph1))
print()
print("# Parcours en largeur")
print(parcours_largeur(graph1))
