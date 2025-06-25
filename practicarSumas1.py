##Ejercicio 03
import random
##Se usara random para arrojar valores aleatorios

num1=0
num2=0
sumaUsuario= 0
puntos= 0

print("Momento de practicar sumas, seran un total de 10 calculos!")
for x in range(10):
    num1=random.randint(1,500)
    num2=random.randint(1,500)
    print("¿Cuánto es la suma de los siguientes numeros? ",num1," + ",num2)
    sumaUsuario=int(input("Ingrese su resultado: "))
    if(sumaUsuario == (num1+num2)):
        puntos+=1
print("Fin de las sumas!")
print("El puntaje final fue: ",puntos,"/10"," acertadas, felicitaciones!")