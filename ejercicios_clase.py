#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: Ejercicio 1 de la Clase Numero 3

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Alejandro Villaboa"
__email__ = "alejandrocesarv@gmail.com"
__version__ = "Clase numero 3"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos

    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    # Mis numeros son 5 y 2
    # Mayor
    if numero_1 > numero_2:
        print('El numero {} es mayor a {}'.format(numero_1, numero_2))
    else:
        print('El numero {} es menor a {}'.format(numero_1, numero_2))


    # Numero positivo, negativo o cero
    if numero_1 > 0:
        print('El numero {} es positivo'.format(numero_1))
    elif numero_1 == 0:
        print('El numero {} es igual a 0'.format(numero_1))
    else:
        print('El numero {} es negativo'.format(numero_1))


    # Numero mayor a 0 y menor a 100
    if (numero_1 > 0 and numero_1 < 100):
        print('El numero {} es mayor a 0 y menor a 100'.format(numero_1))
    else:
        print('El numero {} es menor a 0'.format(numero_1))


    # Numero menor a 10 o es mayor a -2
    if (numero_1 < 10):
        print('El numero {} es menor a 10'.format(numero_1))
    else:
        print('El numero {} es mayor a 10'.format(numero_1))

    if (numero_2 > -2):
        print('El numero {} es mayor a -2'.format(numero_2))
    else:
        print('El numero {} es menor a -2'.format(numero_2))


def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    # copia_texto_1 = texto_1 Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    # Mis palabras son Teclado y Auto
    # Cual palabras es mayor (alfabéticamente)
    if texto_1 > texto_2:
        print('La palabra {} es mayor alfabéticamente {}'.format(texto_1, texto_2))
    elif texto_1 > texto_2:
        print('La palabra {} es menor alfabéticamente {}'.format(texto_1, texto_2)) 


    # Compare cual de las dos palabras tiene mas letras
    if len(texto_1) > len(texto_2):
        print('{} tiene mas letras que {}'.format(texto_1, texto_2))

    elif len(texto_1) < len(texto_2):
        print('{} tiene mas letras que {}'.format(texto_2, texto_1))


    # Ver si la primera letra de la primera palabra es mayor a la primera letra de la segunda palabra
    if (texto_1[0] > texto_2[0]):
        print('La primera letra de {} es mayor alfabéticamente que {}'.format(texto_1, texto_2))
    elif (texto_1[0] < texto_2[0]):
        print('La primera letra de {} es menor alfabéticamente que {}'.format(texto_1, texto_2))
    else:
        print('La primera letra de {} y {}, son iguales'.format(texto_1, texto_2))

    
    # Verifique que copia_texto_1 es igual a texto_1
    copia_texto_1 = texto_1

    if copia_texto_1 == texto_1:
        print("{} es igual a {}".format(copia_texto_1, texto_1))
    else:
        print("{} no es igual a {}".format(copia_texto_1, texto_1))


    # Verifique que copia_texto_1 es distinta a texto_2
    if copia_texto_1 == texto_2:
        print("{} es igual a {}".format(copia_texto_1, texto_2))
    else:
        print("{} no es igual a {}".format(copia_texto_1, texto_2))


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2 es positivo
    #   --> En caso afirmativo imprima en pantalla "Resp=1"
    #   --> En caso negativo imprima en pantalla   "Resp=2"
    #   --> En caso negativo (numero_1 no es mayor a 5)

    # Verifique si el numero_2 es mayor a 5
    #   --> En caso afirmativo imprima en pantalla "Resp=3"
    #   --> En caso negativo imprima en pantalla "Resp=4"

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados


    # Verifique si el numero_1 es mayor a 5
    if numero_1 > 5:
        print('El numero {} es mayor a {}'.format(numero_1, 5))
        if numero_2 > 0:
            print('Resp=1: El numero {} es positivo'.format(numero_2))
        else:
            print('Resp=2: El numero {} es negativo'.format(numero_2))
    else:
        print('El numero {} no es mayor {}'.format(numero_1, 5))


    # Verifique si el numero_2 es mayor a 5
    if numero_2 > 5:
        print('Resp=3: El numero {} es positivo'.format(numero_2))
    else:
        print('Resp=4: El numero {} es negativo'.format(numero_2))


    # Verifique la calificación de un estudiante
    if puntaje <= 60:
        if puntaje >= 60:
            print('Su calificacion fue "D"')
            if puntaje >= 70:
                print('Su calificacion fue "C"')
                if puntaje >= 80:            
                    print('Su calificacion fue "B"')
                    if puntaje >= 90:
                        print('Su calificacion fue "A"')
    else:
        print('Su calificacion fue "F"')


def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)


    # Verifique cual cual de los dos textos es mayor alfabéticamente
    if texto_1 > texto_2:
        print('{} es mayor alfabeticamente que {}'.format(texto_1, texto_2))
    else:
        print('{} es mayor alfabeticamente que {}'.format(texto_2, texto_1))


    # Transforma esas variables tipo texto y almacénalas en nuevas variables númericas (int)
    numero_1 = int(texto_1)
    numero_2 = int(texto_2)

    if numero_1 > numero_2:
        print('{} es mayor que {}'.format(numero_1, numero_2))
    else:
        print('{} es mayor que {}'.format(numero_2, numero_1))


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
