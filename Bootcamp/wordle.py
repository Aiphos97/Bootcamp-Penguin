palabra_de_dia = 'PASTO'
intentos = 0
grilla_intentos = []
def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    cantidad_de_letras = 5

    letras_verficadas = []
    aux=0

    for posicion in range(cantidad_de_letras):
        #Si la letra coincide con la posicion
        letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]

        la_letra_existe_en_la_palabra = palabra_ingresada[posicion] in palabra_a_encontrar
        
        
        
        if letras_son_iguales:

            letras_verficadas.append("[" + palabra_ingresada[posicion] + "]")
        
        elif la_letra_existe_en_la_palabra:
            letras_verficadas.append(f"({palabra_ingresada[posicion]})")

        else:
            letras_verficadas.append(palabra_ingresada[posicion])
        aux1=letras_verficadas.count(f"[{palabra_ingresada[posicion]}]")
        aux2=letras_verficadas.count(f"({palabra_ingresada[posicion]})")
        if((aux1>0 or aux2>1) and letras_verficadas[posicion]==f"({palabra_ingresada[posicion]})"):
            letras_verficadas[posicion] = (palabra_ingresada[posicion])
        
    return letras_verficadas

def validacion_palabra(cifras_palabra_oculta):
    palabra = input('Encuentra la palabra oculta:')
    while (not palabra.isalpha() or len(palabra)!=cifras_palabra_oculta):
        print('La palabra ingresada es invalida')
        palabra = input("Ingrese una palabra valida:")

        
    return palabra.upper()


while intentos<4:
    palabra_intento= validacion_palabra(len(palabra_de_dia))
    obtener_fila_verificada(palabra_de_dia,palabra_intento)
    grilla_intentos.append(obtener_fila_verificada(palabra_de_dia,palabra_intento))
    for iterador in grilla_intentos:
        print(iterador)
    if palabra_intento==palabra_de_dia:
        print(f'Ganaste la palabra del dia es: {palabra_de_dia}')
        break
    else:
        intentos = intentos + 1
        print(f'Le quedan {5-(intentos)} intentos')
        
    if(intentos == 5):
        print("Has perdidos el juego. te quedaste sin intentos")
        print(f'La palabra del dia era {palabra_de_dia}')