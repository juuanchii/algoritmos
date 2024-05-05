#Ejercicio 5 - Pasar numeros romanos a decimal.

def valor_romano(romano):
    if romano == 'I':
        return 1
    elif romano == 'V':
        return 5
    elif romano == 'X':
        return 10
    elif romano == 'L':
        return 50
    elif romano == 'C':
        return 100
    elif romano == 'D':
        return 500
    elif romano == 'M':
        return 1000
    else:
        return 0


def romano_a_decimal(romano):
    if not romano:
        return 0
    if len(romano) == 1:
        return valor_romano(romano)
    if valor_romano(romano[0]) < valor_romano(romano[1]):
        return valor_romano(romano[1]) - valor_romano(romano[0]) + romano_a_decimal(romano[2:])
    else:
        return valor_romano(romano[0]) + romano_a_decimal(romano[1:])

numero_romano = "XXIV"
numero_decimal = romano_a_decimal(numero_romano)
print(numero_romano, 'en decimal es: ', numero_decimal)


#Ejercicio 22 - Usando la Fuerza
    
mochila = ['sable de luz',
            'equipo de supervivencia',
            'comunicador',
            'herramientas',
            'mapas',
            'medicamentos']
    
cont = 0

def usar_la_fuerza(mochi):  
    if mochi == []:
        return 0
    elif mochi[-1:] == ['sable de luz']:
        return cont
    else:
        return cont + 1 + usar_la_fuerza(mochi[:-1])


contadorDeFuerza = usar_la_fuerza(mochila)
if contadorDeFuerza > 0:
    print('Enconraste el sable de luz luego de sacar ', contadorDeFuerza,'objetos')
else:
    print('el sable de luz no esta en la mochila')