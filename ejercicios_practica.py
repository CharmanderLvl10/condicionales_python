#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: Ejercicio 2 de la Clase Numero 3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Alejandro Villaboa"
__email__ = "alejandrocesarv@gmail.com"
__version__ = "Clase numero 3"

def ej1():
    print('Ejercicio 1 de práctica con números')

    # Realice un programa que solicite por consola 2 números
    # Calcule la diferencia entre ellos e informe por pantalla
    # si el resultado es positivo, negativo o cero.

    numero_1 = float(input('Ingrese su primer numero:\n'))
    numero_2 = float(input('Ingrese su segundo numero:\n'))

    resultado_1 = numero_1 / numero_2

    if resultado_1 > 0:
        print('El resultado de {} y {} es positivo'.format(numero_1, numero_2))

    elif resultado_1 < 0:
        print('El resultado de {} y {} es negativo'.format(numero_1, numero_2))

    else:
        print('El resultado de {} y {} es cero'.format(numero_1, numero_2))


def ej2():
    print('Ejercicio 2 de práctica con números')

    # Realice un programa que solicite el ingreso de tres números
    # enteros, y luego en cada caso informe si el número es par
    # o impar.
    # Para cada caso imprimir el resultado en pantalla.
    
    numero_1 = int(input('Ingrese su primer numero entero:\n'))
    numero_2 = int(input('Ingrese su segundo numero entero:\n'))
    numero_3 = int(input('Ingrese su tercer numero entero:\n'))

    if (numero_1 % 2) == 0: 
        print('El primer número {} es par'.format(numero_1))
    else:
        print('El primer número {} es impar'.format(numero_1))
        
    if (numero_2 % 2) == 0:
        print('El segundo número {} es par'.format(numero_2))
    else:
        print('El segundo número {} es impar'.format(numero_2))

    if (numero_3 % 2)== 0:
        print('El tercer número {} es par'.format(numero_3))
    else:
        print('El tercer número {} es impar'.format(numero_3))


def ej3():
    print('Ejercicios 3 de práctica con números')

    # Realice una calculadora, se ingresará por línea de comando dos números
    # Luego se ingresará como tercera entrada al programa el símbolo de la operación
    # que se desea ejecutar
    # - Suma (+)
    # - Resta (-)
    # - Multiplicación (*)
    # - División (/)
    # - Exponente/Potencia (**)
    # Se debe efectuar el cálculo correcto según la operación ingresada por consola
    # Imprimir en pantalla la operación realizada y el resultado
    

    numero_1 = float(input('Ingrese su primer numero:\n'))
    print('Ingrese su operacion:\n')
    print('Suma (+)')
    print('Resta (-)')
    print('Multiplicación (*)')
    print('División (/)')
    print('Exponente/Potencia (**)\n')
    calculo_1 = str(input())
    numero_2 = float(input('Ingrese su segundo numero:\n'))


    if calculo_1 == '+':
        resultado_1 = numero_1 + numero_2
        print('La suma de {} y {} es:\n{}\n'.format(numero_1, numero_2, resultado_1))

    elif calculo_1 == '-':
        resultado_2 = numero_1 - numero_2
        print('La resta de {} y {} es:\n{}\n'.format(numero_1, numero_2, resultado_2))

    elif calculo_1 == '*':
        resultado_3 = numero_1 * numero_2
        print('La multiplicacion de {} y {} es:\n{}\n'.format(numero_1, numero_2, resultado_3))

    elif calculo_1 == '/':
        resultado_4 = numero_1 / numero_2
        print('La division de {} y {} es:\n{}\n'.format(numero_1, numero_2, resultado_4))

    elif calculo_1 == '**':
        resultado_5 = numero_1 ** numero_2
        print('El exponente de {} y {} es:\n {}\n'.format(numero_1, numero_2, resultado_5))


def ej4():
    print('Ejercicios de práctica con cadenas')

    # Realice un programa que solicite por consola 3 palabras cualesquiera
    # Luego el programa debe consultar al usuario como quiere ordenar las palabras
    # 1 - Ordenar por orden alfabético (usando el operador ">")
    # 2 - Ordenar por cantidad de letras (longitud de la palabra)
    # Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    # e imprimir en pantalla de la mayor a la menor
    # Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    # e imprimir en pantalla de la mayor a la menor
    
    # 3 palabras cualesquiera. Ej: "Teclado, Auto y Zapatilla"
    print('Programa para ordenar palabras\nA continuacion eligar 3 palabras y luego la opcion deseada\n')

    palabra_1 = str(input('Ingrese su primer palabra:\n'))
    palabra_2 = str(input('\nIngrese su segunda palabra:\n'))
    palabra_3 = str(input('\nIngrese su tercer palabra:\n'))

    print('\n1 - Ordenar las 3 palabras por orden alfabético\n')
    print('2 - Ordenar por cantidad de letras\n')

    orden = str(input())

    # 1 - Ordenar por orden alfabético (usando el operador ">")
    if orden == '1':

        if palabra_1 < palabra_2 < palabra_3:
            print('\nLas palabras en ordena alfabetico son\n {} - {} - {}\n'.format(palabra_1, palabra_2, palabra_3))

        elif palabra_1 < palabra_2 == palabra_3:
            print('\nLas palabras en ordena alfabetico son\n {} - {} - {}\n'.format(palabra_1, palabra_2, palabra_3))

        elif palabra_2 < palabra_1 < palabra_3:
            print('\nLas palabras en ordena alfabetico son\n {} - {} - {}\n'.format(palabra_2, palabra_1, palabra_3))

        elif palabra_2 < palabra_1 == palabra_3:
            print('\nLas palabras en ordena alfabetico son\n {} - {} - {}\n'.format(palabra_2, palabra_1, palabra_3))

        elif palabra_3 < palabra_1 < palabra_2:
            print('\nLas palabras en ordena alfabetico son\n {} - {} - {}\n'.format(palabra_3, palabra_1, palabra_2))

        elif palabra_3 < palabra_1 == palabra_2:
            print('\nLas palabras en ordena alfabetico son\n {} - {} - {}\n'.format(palabra_3, palabra_1, palabra_2))
        
        else:
            print('\nLas palabras en ordena alfabetico son\n {} - {} - {}\n'.format(palabra_1, palabra_2, palabra_3))

    # 2 - Ordenar por cantidad de letras (longitud de la palabra)
    if orden == '2':

        if len(palabra_1) < len(palabra_2) < len(palabra_3):
            print('\nLas palabra cantidad de letras son\n {} - {} - {}\n'.format(palabra_1, palabra_2, palabra_3))

        elif len(palabra_1) < len(palabra_2) == len(palabra_3):
            print('\nLas palabra por cantidad de letras son\n {} - {} - {}\n'.format(palabra_1, palabra_2, palabra_3))

        elif len(palabra_2) < len(palabra_1) < len(palabra_3):
            print('\nLas palabra por cantidad de letras son\n {} - {} - {}\n'.format(palabra_2, palabra_1, palabra_3))

        elif len(palabra_2) < len(palabra_1) == len(palabra_3):
            print('\nLas palabra por cantidad de letras son\n {} - {} - {}\n'.format(palabra_2, palabra_1, palabra_3))

        elif len(palabra_3) < len(palabra_1) < len(palabra_2):
            print('\nLas palabra por cantidad de letras son\n {} - {} - {}\n'.format(palabra_3, palabra_1, palabra_2))

        elif len(palabra_3) < len(palabra_1) == len(palabra_2):
            print('\nLas palabra por cantidad de letras son\n {} - {} - {}\n'.format(palabra_3, palabra_1, palabra_2))

        else:
            print('\nLas palabra por cantidad de letras son\n {} - {} - {}\n'.format(palabra_1, palabra_2, palabra_3))

def ej5():
    print('Ejercicios de práctica con números')

    # Realice un programa que solicite ingresar tres valores de temperatura
    # De las temperaturas ingresadas por consola determinar:
    # 1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    # 2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    # 3 - ¿Cuál es el promedio de las temperaturas ingresadas?
    # En cada caso imprimir en pantalla el resultado

    # Realice un programa que solicite ingresar tres valores de temperatura   
    print('\nProgramade temperaturas\nA continuacion inegrese las temperatuas y luego la opcion deseada\n')

    print('Ingrese la primera temperatura a medir\n')
    temp_1 = int(input())
    print('\nIngrese la segunda temperatura a medir\n')
    temp_2 = int(input())
    print('\nIngrese la tercer temperatura a medir\n')
    temp_3 = int(input())

    print('\n1 - Máxima temperatura ingresada\n')
    print('2 - Mínima temperatura ingresada\n')
    print('3 - Promedio de las temperaturas ingresadas\n')
    orden = str(input())

    # 1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    if orden == '1':

        if temp_1 > temp_2 and temp_1 > temp_3:
            print('\nLa temperatura maxima es: ',temp_1,)

        elif temp_1 > temp_2 and temp_1 == temp_3:
            print('\nLa temperatura maxima es: ',temp_1,)

        elif temp_2 > temp_1 and temp_2 > temp_3:
            print('\nLa temperatura maxima es: ',temp_2,)

        elif temp_2 > temp_1 and temp_2 == temp_3:
            print('\nLa temperatura maxima es: ',temp_2,)

        elif temp_3 > temp_1 and temp_3 > temp_2:
            print('\nLa temperatura maxima es: ',temp_3,)

        elif temp_3 > temp_1 and temp_1 == temp_2:
            print('\nLa temperatura maxima es: ',temp_3)
        
        else:
            print('\nLas 3 temperaturas son iguales: ', temp_1)

    # 2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    if orden == '2':

        if temp_1 < temp_2 and temp_1 < temp_3:
            print('\nLa temperatura mínima es: ',temp_1,)

        elif temp_1 < temp_2 and temp_1 == temp_3:
            print('\nLa temperatura mínima es: ',temp_1,)

        elif temp_2 < temp_1 and temp_2 < temp_3:
            print('\nLa temperatura mínima es: ',temp_2,)

        elif temp_2 < temp_1 and temp_2 == temp_3:
            print('\nLa temperatura mínima es: ',temp_2,)

        elif temp_3 < temp_1 and temp_3 < temp_2:
            print('\nLa temperatura mínima es: ',temp_3,)

        elif temp_3 < temp_1 and temp_1 == temp_2:
            print('\nLa temperatura mínima es: ',temp_3)
        
        else:
            print('\nLas 3 temperaturas son iguales: ', temp_1)

    # 3 - ¿Cuál es el promedio de las temperaturas ingresadas?
    if orden == '3':
        from statistics import mean

        temperaturas = [temp_1, temp_2, temp_3]

        print('\nEl promedio de las 3 temperaturas es: ', mean(temperaturas))


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()