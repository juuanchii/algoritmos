from lista import search, by_name, by_house, remove, show_list_list, show_list

super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
  }
]


super_heroes.sort(key=by_house)

#Punto A
if remove(super_heroes, 'nombre', "Linterna Verde") != None:
    print(f"Linterna verde se removio de la lista")

#Punto B
indexWolverine = search(super_heroes, 'nombre', "Wolverine")
if indexWolverine is not None:
    print(f"El anio de aparicion de Wolverine fue {super_heroes[indexWolverine]['año_aparicion']}")

#Punto C
def cambiar_casa_comic(nombre_heroe, nueva_casa_comic):
  index_heroe = search(super_heroes, 'nombre', nombre_heroe)
  if index_heroe is not None:
    super_heroes[index_heroe]["casa_comic"] = nueva_casa_comic
    print(f"{nombre_heroe} cambio de casa comic a {nueva_casa_comic}")

#Punto D
def print_bibliografia_con_armadura_traje():
  for i in range(len(super_heroes)):
    if 'traje' in super_heroes[i]['biografia'] or 'armadura' in super_heroes[i]['biografia']:
      print(i, super_heroes[i]['nombre'], super_heroes[i]['biografia'])

#Punto E
def mostrar_heroes_aterior_a(anio_limite):
    print("Los heroes que aparecieron antes del año", anio_limite, "son: ")
    for i in range(len(super_heroes)):
        if super_heroes[i]['año_aparicion'] < anio_limite:
            print(i+1, super_heroes[i]['nombre'], super_heroes[i]['año_aparicion'])   

#Punto F
def mostrar_casa_de(heroe):
  index_heroe = search(super_heroes, 'nombre', heroe)
  if index_heroe is not None:
    print(f"La casa de {heroe} es {super_heroes[index_heroe]['casa_comic']}")

#Punto G
def mostrar_informacion_de(heroe):
    index_heroe = search(super_heroes, 'nombre', heroe)
    if index_heroe is not None:
        print(f"--Informacion del super heroe {heroe}:")
        print(f"    -Posicion {index_heroe}")
        print(f"    -Año de aparicion: {super_heroes[index_heroe]['año_aparicion']}")
        print(f"    -Casa comic: {super_heroes[index_heroe]['casa_comic']}")
        print(f"    -Biografia: {super_heroes[index_heroe]['biografia']}")
                  
#Punto H
def print_heroes_con_BSM():
  for index, heroe in enumerate(super_heroes):
      if heroe['nombre'].startswith(('B', 'S', 'M')):
        print(index, heroe['nombre'])

def cant_heroes_en_casa_comic(casa):
    cant = 0
    for heroe in super_heroes:
        if heroe['casa_comic'] == casa:
            cant += 1
    if cant > 0:
        print(f"Hay {cant} de superheroes en la casa {casa}")

#cambiar_casa_comic('Doctor Strange', 'Marvel Comics')
#mostrar_heroes_aterior_a(1963)
#mostrar_casa_de("Capitana Marvel")
#mostrar_casa_de("Mujer Maravilla")
#mostrar_informacion_de("Flash")
#mostrar_informacion_de("Green Arrow")
#cant_heroes_en_casa_comic("Marvel Comics")
#show_list('heroes', super_heroes)