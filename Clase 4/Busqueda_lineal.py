import random  as r
import time as t

def crear_lista():
    size_list= int (input("ingrese el tamaño de la lista : "))
    lista  = [r.randint(1,1000000) for i in range (size_list)]

    return lista

def busqueda_lineal(lista, objetivo):
    encontrado = False

    for elemento in lista:
        if elemento == objetivo:
            encontrado = True
            break #rompe el ciclo

    return encontrado

def busqueda_lineal_original(lista, objetivo):
    encontrado = False

    for i in range (len(lista)):
        if lista[i] == objetivo:
            encontrado = True
            break

    return encontrado


# lista_objetivo = crear_lista()
# print(lista_objetivo)
# numero = int (input("ingrese un numero a  buscar : "))
# inicio = t.time()
# busqueda_lineal (lista_objetivo, numero)
# print (t.time()- inicio)

# inicio = t.time()
# busqueda_lineal_original (lista_objetivo, numero)
# print(t.time()- inicio)