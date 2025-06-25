##Ejercicio 01
print("Ingrese un año y se determinara si es bisiesto o no")
age=int(input("Ingrese el año"))
if(age%4==0 and (age % 100 != 0 or age % 400 == 0)):
    print("El año ",age," es bisiesto")
else:
    print("El año no es bisiesto")