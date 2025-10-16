import math

graph_distance = {
    1: {1: 0, 2: 2, 3:math.inf, 4: 6}, 
    2: {1: math.inf, 2: 0, 3: -2, 4: math.inf},
    3: {1: math.inf, 2: 5, 3: 0, 4: 5},
    4: {1: -4, 2: -1, 3: math.inf, 4: 0}
}

graph_predecesseur = {
    1: {1: 1, 2: 1, 3: 1, 4: 1}, 
    2: {1: 2, 2: 2, 3: 2, 4: 2},
    3: {1: 3, 2: 3, 3: 3, 4: 3},
    4: {1: 4, 2: 4, 3: 4, 4: 4}
}

def floyd_algoritheme(graph_distance, graph_predecesseur):
    sommets = list(graph_distance.keys())
    for k in sommets:
        for i in sommets:
            for j in sommets:
                if graph_distance[i][j] > graph_distance[i][k] + graph_distance[k][j]:
                    graph_distance[i][j] = graph_distance[i][k] + graph_distance[k][j]
                    graph_predecesseur[i][j] = graph_predecesseur[k][j]
    return graph_distance, graph_predecesseur


    

def reconstruction_chemin(graph_predecesseur, debut, fin):
    chemin = []
    if graph_predecesseur[debut][fin] is None:
        return chemin
    while fin != debut:
        chemin.append(fin)
        fin = graph_predecesseur[debut][fin]
    chemin.append(debut)
    chemin.reverse()
    return chemin


def verification_cycle_negatif(graph_distance):
    for sommet in graph_distance:
        if graph_distance[sommet][sommet] < 0:
            return True
    return False



distances, predecesseurs = floyd_algoritheme(graph_distance, graph_predecesseur)


if verification_cycle_negatif(distances):
    print("--------------------------------")
    print(" Le graphe contient un cycle negatif.")
    print("--------------------------------")
else:
    print("--------------------------------")
    print(" Aucun cycle negatif detecte.")
    print("--------------------------------")


for i in distances:
    print()
    for j in distances[i]:
        chemin = reconstruction_chemin(predecesseurs, i, j)
        print(f"De {i} a {j} : distance = {distances[i][j]}, chemin = {chemin}, predecesseur = {predecesseurs[i][j]}")
        


