##Ejercicio 04
import random
nivel= 0
num1=0
num2=0
sumaUsuario=0
puntos=0

print("Bienvenido a la practica de sumas, elija su dificultad: ")
print("1- Facil , 2- Intermedio, 3- Dificil")
nivel = int(input("Ingrese un número para escojer el nivel"))

if (nivel==1):
    for x in range(10):
        num1=random.randint(0,25)
        num2=random.randint(0,25)
        print("¿Cuánto es la suma de los siguientes numeros? ",num1," + ",num2)
        sumaUsuario=int(input("Ingrese su resultado: "))
        if(sumaUsuario == (num1+num2)):
            puntos+=1
elif(nivel==2):
    for x in range(10):
        num1=random.randint(26,75)
        num2=random.randint(26,75)
        print("¿Cuánto es la suma de los siguientes numeros? ",num1," + ",num2)
        sumaUsuario=int(input("Ingrese su resultado: "))
        if(sumaUsuario == (num1+num2)):
            puntos+=1
elif(nivel==3):
    for x in range(10):
        num1=random.randint(76,150)
        num2=random.randint(76,150)
        print("¿Cuánto es la suma de los siguientes numeros? ",num1," + ",num2)
        sumaUsuario=int(input("Ingrese su resultado: "))
        if(sumaUsuario == (num1+num2)):
            puntos+=1
print("Fin de las sumas!")
print("El puntaje final fue: ",puntos,"/10"," acertadas, felicitaciones!")