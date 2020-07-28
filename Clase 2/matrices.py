matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print (matriz[2][1])
print(len(matriz))
print (len(matriz[1]))

print ("Metodo 1")
for i in range (len(matriz)):
    print ("se muestra los elementos de la lista", i)
    for j in range (len(matriz[i])):
        print(matriz[i][j])

print ("Metodo 2")
for lista in matriz:
    print (lista)
    for elemento in lista:
        print (elemento)

lista = [2,3,45,67,1,5,87,98,89]
print (lista [2:6])
print(lista[2:-2]) # menos la ultima posicion 
print (lista[:]) #desde el comienzo hasta la coordenada que yo quiera 
print (lista [:]) #para mostrar todo

print (matriz [0] [1:3])
print (matriz [1][:4]) #desde el 4 hacia la derecha no hay nada