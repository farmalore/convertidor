def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario





print("conversor Binario <-> Decimal") #Desde aca se muestra un menu con 2 opciones para el usuario
print("1)Binario a Decimal")   #Opcion 1 si quiere hacer la conversion de Binario a Decimal
print("2)Decimal a Binario")   #Opcion 2 si quiere hacer la conversion de Decimal a Binario

opcion = input("Elige una opcion (1 o 2):")

if opcion == "1": #si la opcion elegida por el usuario es el "1" se ejecutara esta parte
    binario = input("Ingrese su numero en binario: ") #Se le pide al usuario ingresar un numero binario
    decimal = binario_a_decimal(binario) #llamada a la funcion binario_a_decimal para convertirlo en decimal(este calculo le pedi ayuda a la ia)
    print(f"El nuemro Binario {binario} en Decimal es: {decimal}") #imprime el resultado

elif opcion == "2": #si la opcion elegida por el usuario es el "2" se ejecutara esta parte
    decimal = int(input("Ingrese su numero en decimal: ")) #se le pide al usuario ingresar un numero en decimal
    binario = decimal_a_binario(decimal) #llamada a la funcion decimal_a_binario para convertirlo a binario (este calculo le pedi ayuda a la ia)
    print(f"El numero Decimal {decimal} en Binario es: {binario}") #imprime el resultado
else: #si la opcion elegida por el usuario no es ni "1 o 2" saltara el siguiente mensaje ne pantalla
    print("Opcion no valida. Elige 1 o 2")