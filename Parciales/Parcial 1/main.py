import codigos
import time

n=0
inicio = time.time()
codigos.caso1 (n)
tiempo_caso1 = time.time() - inicio
inicio = time.time ()
codigos.caso2 (n)
tiempo_caso2 = time.time() - inicio
print (tiempo_caso1)
print (tiempo_caso2)

if tiempo_caso1>tiempo_caso2:
    print ("El mejor caso es el 2")
else:
    print ("El mejor caso es el 1")
