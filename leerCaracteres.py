##Ejercicio 02
caracter = ''
vocales = 0
palabras = 0
Mpalabras= 0
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0
max_vocal=0
min_vocal=0

print("Ingrese un caracter, una palabra, o un punto '.' para finalizar: ")
caracter=input("Caracter palabra o finalizar? '.' para fin: ")

while (caracter!="."):

    if (len(caracter)>1):
        palabras+= 1
        if(caracter[0]=="M" or caracter[0]=="m"):
            Mpalabras+= 1
    if (len(caracter)==1):
        caracter= caracter.lower()

        if caracter in "aeiou":
            vocales+= 1

        if caracter == "a":
            cont_a += 1
        elif caracter == "e":
            cont_e += 1
        elif caracter == "i":
            cont_i += 1
        elif caracter == "o":
            cont_o += 1
        elif caracter == "u":
            cont_u += 1

    caracter=input("Ingrese nuevamente un caracter, una palabra, o un punto '.' para finalizar: ")

##Defino un objeto de vocales, donde a cada una se le asocia su contador, para luego consseguir sacar min y max
vocales_dict = {
    "a": cont_a,
    "e": cont_e,
    "i": cont_i,
    "o": cont_o,
    "u": cont_u
}
max_vocal = max(vocales_dict, key=vocales_dict.get)
min_vocal = min(vocales_dict, key=vocales_dict.get)

print("Resultados: ")
print("Cantidad total de vocales: ",vocales)
print("Cantidad de palabras totales: ", palabras)
print("Cantidad de palabras que empezaban con 'M' o 'm': ", Mpalabras)
print("Maxima vocal: ",max_vocal," Minima vocal: ",min_vocal)

