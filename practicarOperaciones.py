##Ejercicio 05
import random
operacion= 0##Ejercicio 05
import random
operador= 0
num1=0
num2=0
calculoUsuario=0
puntos=0
dificultad=""
print("Bienvenido a la practica de operaciones, ingrese que operacion realizara: ")
print("'+' para sumar, '-' para la resta, '*' para multiplicacion, y '/' para dividir")
operador=input("Escriba aqui su operador: ")
print("Ahora escoja la dificultad: ")
print("1- Facil , 2- Medio, 3- Dificil")
dificultad = int(input("Escriba aqui su nivel de dificultad: "))

if (dificultad==1):
    for x in range(10):
        num1=random.randint(0,25)
        num2=random.randint(0,25)
        print("¿Cuánto es el resultado de la siguiente operacion? ",num1,operador,num2)
        calculoUsuario=int(input("Ingrese su resultado: "))
        if(calculoUsuario == (eval(f"{num1} {operador} {num2}"))):
            puntos+=1
elif(dificultad==2):
    for x in range(10):
        num1=random.randint(26,75)
        num2=random.randint(26,75)
        print("¿Cuánto es el resultado de la siguiente operacion? ",num1,operador,num2)
        calculoUsuario=int(input("Ingrese su resultado: "))
        if(calculoUsuario == (eval(f"{num1} {operador} {num2}"))):
            puntos+=1
elif(dificultad==3):
    for x in range(10):
        num1=random.randint(76,150)
        num2=random.randint(76,150)
        print("¿Cuánto es el resultado de la siguiente operacion? ",num1,operador,num2)
        calculoUsuario=int(input("Ingrese su resultado: "))
        if(calculoUsuario == (eval(f"{num1} {operador} {num2}"))):
            puntos+=1
            
print("Fin de la practica!")
print("El puntaje final fue: ",puntos,"/10"," acertadas, felicitaciones!")
num1=0
num2=0
sumaUsuario=0
puntos=0

print("Bienvenido a la practica de operaciones, elija una opcion: ")
print("1- Suma , 2- Resta, 3- Multiplicacion 4- Division")
operacion = int(input("Ingrese un número para escojer la operacion"))

if (operacion==1):
    for x in range(10):
        num1=random.randint(0,25)
        num2=random.randint(0,25)
        print("¿Cuánto es la suma de los siguientes numeros? ",num1," + ",num2)
        sumaUsuario=int(input("Ingrese su resultado: "))
        if(sumaUsuario == (num1+num2)):
            puntos+=1
elif(operacion==2):
    for x in range(10):
        num1=random.randint(26,75)
        num2=random.randint(26,75)
        print("¿Cuánto es la resta de los siguientes numeros? ",num1," - ",num2)
        sumaUsuario=int(input("Ingrese su resultado: "))
        if(sumaUsuario == (num1-num2)):
            puntos+=1
elif(operacion==3):
    for x in range(10):
        num1=random.randint(76,150)
        num2=random.randint(76,150)
        print("¿Cuánto es el producto de los siguientes numeros? ",num1," * ",num2)
        sumaUsuario=int(input("Ingrese su resultado: "))
        if(sumaUsuario == (num1*num2)):
            puntos+=1
elif(operacion==4):
    for x in range(10):
        num1=random.randint(76,150)
        num2=random.randint(76,150)
        print("¿Cuánto es la division de los siguientes numeros? ",num1," / ",num2)
        sumaUsuario=int(input("Ingrese su resultado: "))
        if(sumaUsuario == (num1/num2)):
            puntos+=1
print("Fin de la practica!")
print("El puntaje final fue: ",puntos,"/10"," acertadas, felicitaciones!")