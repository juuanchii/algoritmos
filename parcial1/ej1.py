names = ['Juan', 'Julian', 'Maria', 'Ana', 'Julieta', 'Jose', 'Ludmila', 'Lucas', 'Caro', 'Jorge', 'Walter']

def barrido(lista):
    if len(lista) == 1:
        print(lista[0])
    else:
        print(lista[-1])
        barrido(lista[:-1])

barrido(names)