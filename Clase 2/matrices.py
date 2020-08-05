matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print (matriz[2][1]) # el primero es la lista y el segundo la posicion en la lista
print(len(matriz)) #tamaño de la matriz (cantidad de listas)
print (len(matriz[1]))#Tamaño de la lista 1 (cantidad de numeros)
#---------------------------------------
# Para mostrar cada elemento de una lista
# Metodo 1
for i in range (len(matriz)): # matriz en i es cada linea
    print ("se muestra los elementos de la lista", i)
    for j in range (len(matriz[i])): # la j hace referencia a cada elemento de la lista
        print(matriz[i][j])
#-----------------------------------
# Metodo 2 (mas facil)
for lista in matriz: # cada linea dentro de la matriz
    print (lista)
    for elemento in lista:
        print (elemento)
#-----------------------------------
#-----------------------------------
# Para mostrar todas las listas

# Metodo 1
for i in range (len(matriz)):
    print (matriz[i])

# Metodo 2
for lista in matriz:
    print (lista) 
#------------------------------------

lista = [2,3,45,67,1,5,87,98,89]
print (lista [2:6]) # desde la posicion 2 hasta la posicion 6
print(lista[2:-2]) # menos las ultimas dos posiciones
print (lista[:6]) #desde el comienzo hasta antes del numero 6
print (lista [:]) #para mostrar todo

print (matriz [0] [1:3])# desde la posicion 0 hasta el 1 y antes del numero 3
print (matriz [1][:4]) #Hasta antes de la posicion 4. Desde el hacia la derecha no se muestra nada
# EL DE LA IZQUIERDA ES CERRADO Y EL DE LA DERECHA ES ABIERTO
