# ES LA MAS RAPIDA
def busqueda_binaria (lista, comienzo, final,objetivo):
    if comienzo > final :
        return False
    medio = (comienzo + final) //2
    if lista [medio] == objetivo:
        return True
    elif lista[medio]< objetivo:
        return busqueda_binaria (lista,medio+1,final,objetivo)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo)

# numero = int (input("ingrese un numero : "))
# lista = [9,8,14,2,3,5,22]
# lista_ordenada = sorted (lista)
# print(lista_ordenada)
# encontrado = busqueda_binaria (lista_ordenada,0,len(lista_ordenada),numero)

# if encontrado == True :
#     print ("El numero existe")
# else:
#     print ("El numero no existe")
