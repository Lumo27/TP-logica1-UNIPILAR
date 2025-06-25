##Ejercicio 06
import random
operacion = ""
num1 = 0
num2 = 0
sumaUsuario = 0
puntos = 0
dificultad = ""
estado = ""  ## Variable de estado para controlar la práctica y ponerle fin o seguir

print("Bienvenido a la práctica de operaciones. Elija una opción: ")
print("'+' para Suma , '-' para Resta, '*' para Multiplicación, '/' para División")
operacion = input("Ingrese el símbolo de la operación que desea practicar: ")

print("Ahora elija la dificultad: ")
print("1 - Fácil")
print("2 - Medio")
print("3 - Difícil")
dificultad = int(input("Ingrese el número correspondiente al nivel de dificultad: "))

print("En caso de querer finalizar, luego de terminar la práctica, ingrese la palabra Finalizar")

while(estado != "finalizar"):

    puntos = 0 

    if (dificultad == 1):
        for x in range(10):
            num1 = random.randint(0, 25)
            num2 = random.randint(0, 25)
            print("¿Cuánto es el resultado de la siguiente operación? ", num1, operacion, num2)
            sumaUsuario = int(input("Ingrese su resultado: "))
            if (sumaUsuario == (eval(str(num1) + operacion + str(num2)))):
                puntos += 1

    elif (dificultad == 2):
        for x in range(10):
            num1 = random.randint(26, 75)
            num2 = random.randint(26, 75)
            print("¿Cuánto es el resultado de la siguiente operación? ", num1, operacion, num2)
            sumaUsuario = int(input("Ingrese su resultado: "))
            if (sumaUsuario == (eval(str(num1) + operacion + str(num2)))):
                puntos += 1

    elif (dificultad == 3):
        for x in range(10):
            num1 = random.randint(76, 150)
            num2 = random.randint(76, 150)
            print("¿Cuánto es el resultado de la siguiente operación? ", num1, operacion, num2)
            sumaUsuario = int(input("Ingrese su resultado: "))
            if (sumaUsuario == (eval(str(num1) + operacion + str(num2)))):
                puntos += 1

    print("Fin de la práctica!")
    print("El puntaje final fue: ", puntos, "/10 acertadas. Felicitaciones!")

    estado = input("Para finalizar escriba: 'Finalizar', o presione Enter para seguir practicando: ")
    estado = estado.lower()
    if (estado == "finalizar"):
        print("Gracias por practicar!")
    else:
        print("Sigamos!")
