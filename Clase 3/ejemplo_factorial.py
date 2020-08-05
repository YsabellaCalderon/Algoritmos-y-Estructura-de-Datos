import time

def factorial (n):
  acumulado = 1
  while (n>1):
    acumulado = acumulado*n
    n = n-1
  return acumulado

def factorial_r(n):
  if n == 1 :
    return 1
  return n*factorial_r(n-1)

incial= time.time()
factorial(800)
final= time.time()
print ('el tiempo de demora fue {} para el metodo normal'.format(final-incial))
print(final-incial)
incial= time.time()
factorial_r(800)
final= time.time()
print ('el tiempo de demora fue {} para el metodo recursivo'.format(final-incial))