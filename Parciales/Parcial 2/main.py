import ordenamiento_burbuja
import ordenamiento_insercion
import time
import mezcla
import random
def line_design():
  print ('#'*30)
size_list= int (input("Ingrese tamaño de la lista : "))
lista = [random.randint(300,1230) for i in range(size_list)]

lista_desordenada = lista
line_design()
print("Esta es la lista de manera desordenada")
print(lista_desordenada)
line_design()
lista_desordenada_2 = lista
lista_desordenada_3 = lista
inicio = time.time()
ordenamiento_burbuja.ordenamiento_burbuja(lista)
final_burbuja = time.time()-inicio

inicio = time.time()
ordenamiento_insercion.ordenamiento_por_insercion(lista_desordenada)
final_insercion = time.time()-inicio


inicio = time.time()
mezcla.ord_por_mezcla(lista_desordenada_2)
final_mezcla = time.time()-inicio

line_design()
print("Esta es la lista de manera ordenada")
print(lista_desordenada)
line_design()

print(f"El tiempo final de ordenamiento burbuja es {final_burbuja} y el de ordenamiento insercion {final_insercion} y el tiempo final de mezcla {final_mezcla}")
line_design()

print (f"El metodo mas eficiente es el metodo de Ordenamiento por insercion con un tiempo de {final_insercion}")