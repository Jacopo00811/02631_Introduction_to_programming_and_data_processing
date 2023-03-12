# This is a my first Python script.
# Francesco Ceccuti - 26/09/2021 rev. 0

reflectance = [1.7, 1.6, 1.3, 1.3, 2.8, 1.4, 2.8, 2.6, 1.6, 2.7]
#reflectance = [11.5, 3.2, 4.3, 3.6, 2.8, 1.6, 3.8, 2.6, 2.6, 1.7]
clusterAssignments = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cluster_old = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
differenza = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

Somma_indice_pari = 0
Somma_indice_dispari = 0
Cont_indice_pari = 0
Cont_indice_dispari = 0
Media_indice_pari = 0
Media_indice_dispari = 0
Somma_cluster_1 = 0
Somma_cluster_2 = 0
Cont_indice_cluster_1 = 0
Cont_indice_cluster_2 = 0
Media_cluster_1 = 0
Media_cluster_2 = 0

N=len(reflectance)

i = 0
j = 1

# calcolo la media degli elementi di indice pari e di indice dispari

for indice in range(N):
    if i<N:
        Somma_indice_pari = Somma_indice_pari + reflectance[i]
  #      print(reflectance[i])
        i= i+2
        Cont_indice_pari = Cont_indice_pari + 1
    if j<N:
        Somma_indice_dispari = Somma_indice_dispari + reflectance[j]
  #      print(reflectance[j])
        j= j+2
        Cont_indice_dispari = Cont_indice_dispari + 1

Media_indice_pari = Somma_indice_pari/Cont_indice_pari
Media_indice_dispari = Somma_indice_dispari/Cont_indice_dispari

# assegno alle medie dei cluster 1 e 2 il valore della media degli elementi di indice pari e di indice dispari

Media_cluster_1 = Media_indice_pari
Media_cluster_2 = Media_indice_dispari

print(Media_cluster_1)
print(Media_cluster_2)

# costruisco il primo clusterAssignments utilizzando la media degli elementi di indice pari e di indice dispari

for indice in range(N):
  #  print(indice)
    if abs(reflectance[indice] - Media_cluster_1) < abs(reflectance[indice] - Media_cluster_2):
      clusterAssignments[indice] = 1
    else:
      clusterAssignments[indice] = 2

print(clusterAssignments)

while True:
    # pongo il clusterAssignments in cluster_old

    for indice in range(N):
        cluster_old[indice] = clusterAssignments[indice]
    print(cluster_old)

    # ricalcolo la media degli elementi del cluster 1 e del cluster 2

    for indice in range(N):
        # print(indice)
        if clusterAssignments[indice] == 1:
            Somma_cluster_1 = Somma_cluster_1 + reflectance[indice]
            Cont_indice_cluster_1 = Cont_indice_cluster_1 + 1
        else:
            Somma_cluster_2 = Somma_cluster_2 + reflectance[indice]
            Cont_indice_cluster_2 = Cont_indice_cluster_2 + 1

    Media_cluster_1 = Somma_cluster_1 / Cont_indice_cluster_1
    Media_cluster_2 = Somma_cluster_2 / Cont_indice_cluster_2
    print(Media_cluster_1)
    print(Media_cluster_2)

    # ridefinisco il clusterAssignments utilizzando la media degli elementi del cluster 1 e del cluster 2

    for indice in range(N):
        #  print(indice)
        if abs(reflectance[indice] - Media_cluster_1) < abs(reflectance[indice] - Media_cluster_2):
            clusterAssignments[indice] = 1
        else:
            clusterAssignments[indice] = 2
    print(clusterAssignments)

    # verifico se clusterAssignments = cluster_old; se lo è termino il while con break e restituisco clusterAssignments

    somma = 0
    for indice in range(N):
        differenza[indice] = cluster_old[indice] - clusterAssignments[indice]
        somma = somma + differenza[indice]
        # print(somma)
    print(differenza)

    if somma != 0:
        continue
    break

print(clusterAssignments)
# return clusterAssignments
