from pila import Stack
from personaje import Personaje
from random import randint

p_episodioV = Stack()
p_episodioVII = Stack()
p_interserccion = Stack()
p_aux = Stack()

#Ejercicio 16 - Interseccion personajes de peliculas de Star Wars

episodioV = ['Luke Skywalker',
             'Princess Leia Organa',
             'Han Solo',
             'Darth Vader',
             'Yoda',
             'Obi-Wan Kenobi',
             'Chewbacca',
             'C-3PO',
             'R2-D2']

episodioVII = ['Rey',
               'Finn',
               'Kylo Ren',
               'C-3PO',
               'Leia',
               'R2-D2',
               'BB-8',
               'Chewbacca']

for elemento in episodioV:
    p_episodioV.push(elemento)

for elemento in episodioVII:
    p_episodioVII.push(elemento)

# Guardo el tamaño de la pila con mas elementos para iterarlas en el for
if p_episodioV.size() > p_episodioVII.size():
    tam_max = p_episodioV.size()
else:
    tam_max = p_episodioVII.size()

for i in range(tam_max):
    #Selecciono un personaje y lo guardo en la variable "personaje" para compararlo con todos los de la otra pila
    personaje = p_episodioV.pop() 
    #Itero y utilizo la pila p_EpisodioVII y p_aux para comparar
    if i == 0 or (i % 2) == 0:
        while p_episodioVII.size() != 0:
            if p_episodioVII.on_top() == personaje:
                p_interserccion.push(personaje)
            p_aux.push(p_episodioVII.pop())
    else:
        while p_aux.size() != 0:
            if p_aux.on_top() == personaje:
                p_interserccion.push(personaje)
            p_episodioVII.push(p_aux.pop())

print()
print("Personajes que aparecen en el episodio V y en el episodioVII")
while p_interserccion.size() != 0:
    print('- ',p_interserccion.pop())
print()
print("--------------------")

# Ejercicio 24 - Personajes de Marvel

personajes_marvel = [
    "Iron Man",
    "Capitán América",
    "Thor",
    "Hulk",
    "Black Widow",
    "Spider-Man",
    "Black Panther",
    "Doctor Strange",
    "Gamora",
    "Drax",
    "Rocket Racoon",
    "Groot",
    "Thanos",
    "Loki",
]

pila_personajes_mcu = Stack()
pila_personajes_mcu_aux = Stack()
personaje_mas_5_pelis = Stack()
personaje_c_d_g = Stack()

#Cree la clase Personaje en la que puedo crear un personaje junto con el dato de cantidad de peliculas en las que participo.
# Ese objeto lo guardo el la pila.

#La cantidad de pelis en la que participa cada personaje es aleatoria entre 1 y 10

for element in personajes_marvel:
    pila_personajes_mcu.push(element = Personaje(element, randint(1,10)))
    
cont = 0

while pila_personajes_mcu.size() != 0:
    cont += 1
    personaje = pila_personajes_mcu.pop()
    nombre_personaje = personaje.getNombre()

    #Buscando en que posicion esta Rocket Racoon
    if nombre_personaje == "Rocket Racoon":
        print(f"Rocket Raccoon se encuentra en la posicion {cont}")

    #Buscando personajes en los que aparecen mas de 5 peliculas
    if personaje.getCantPelis() > 5:
        personaje_mas_5_pelis.push(personaje)
    pila_personajes_mcu_aux.push(personaje)

    #En cuantas peliculas participa Black Widow
    if nombre_personaje == "Black Widow":
        print()
        print(f"Black Widow participo en ", personaje.getCantPelis(), " peliculas")
    
    if nombre_personaje.startswith(('C', 'D', 'G')):
        personaje_c_d_g.push(personaje)
                        

while pila_personajes_mcu_aux.size() != 0:
    pila_personajes_mcu.push(pila_personajes_mcu_aux.pop())


#Estos dos ejercicios los hago afuera del while para mostrarlos mas prolijos
print()
print("Personajes que aparecen en mas de 5 peliculas")
while personaje_mas_5_pelis.size() != 0:
    p = personaje_mas_5_pelis.pop()
    print("- ", p.getNombre(), "participo en ", p.getCantPelis(), " peliculas")

print()
print("Personajes que empiezan con C, D o G")
while personaje_c_d_g.size() != 0:
    p = personaje_c_d_g.pop()
    print("- ", p.getNombre())

