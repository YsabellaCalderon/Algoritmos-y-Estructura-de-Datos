# EJEMPLO 1 
import time 

tiempo_inicial = time.time() #funcion que da el tiempo actual
print  ("hola a todos")
tiempo_final = time.time ()
print(tiempo_final-tiempo_inicial)

tiempo_inicial = time.time() 
acumulador = 0 
for i in range (100000):
    acumulador += 1
print  ("hola a todos")
tiempo_final = time.time ()
print(tiempo_final-tiempo_inicial)

x= int (input('ingrese cantidad a acumular : '))
tiempo_inicial = time.time()
acumulador= 0
for i in range (x):
  acumulador +=1
tiempo_final = time.time()
print(tiempo_final-tiempo_inicial)



x= int (input('ingrese cantidad a acumular : '))
tiempo_inicial = time.time()
acumulador= 0
for i in range (x):
  for j in range (x):
   acumulador +=1
tiempo_final = time.time()
print (acumulador)
print(tiempo_final-tiempo_inicial)



