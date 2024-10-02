
criaturas = [
    "Ceto", "Tifón", "Equidna", "Dino", "Pefredo", "Enio", "Escila", "Caribdis", 
    "Euríale", "Esteno", "Medusa", "Ladón", "Águila del Cáucaso", "Quimera", 
    "Hidra de Lerna", "León de Nemea", "Esfinge", "Dragón de la Cólquida", "Cerbero", 
    "Cerda de Cromión", "Ortro", "Toro de Creta", "Jabalí de Calidón", "Carcinos", 
    "Gerión", "Cloto", "Láquesis", "Átropos", "Minotauro de Creta", "Harpías", 
    "Argos Panoptes", "Aves del Estínfalo", "Talos", "Sirenas", "Pitón", 
    "Cierva de Cerinea", "Basilisco", "Jabalí de Erimanto"
]
dioses = [
    "Teseo", "Heracles", "Atalanta", "Hermes", "Medea", "Apolo", 
    "Zeus", "Argos Panoptes", "Perseo", "Belerofonte", "Edipo"
]

Lcriaturas = [
    {"nombre": "Ceto", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Tifón", "derrotado_por": "Zeus", "descripcion": ""},
    {"nombre": "Equidna", "derrotado_por": "Argos Panoptes", "descripcion": ""},
    {"nombre": "Dino", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Pefredo", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Enio", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Escila", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Caribdis", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Euríale", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Esteno", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Medusa", "derrotado_por":None, "descripcion": ""},
    {"nombre": "Ladón", "derrotado_por": "Heracles", "descripcion": ""},
    {"nombre": "Águila del Cáucaso", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Quimera", "derrotado_por": "Belerofonte", "descripcion": ""},
    {"nombre": "Hidra de Lerna", "derrotado_por":  "Heracles", "descripcion": ""},
    {"nombre": "León de Nemea", "derrotado_por":  "Heracles", "descripcion": ""},
    {"nombre": "Esfinge", "derrotado_por": "Edipo", "descripcion": ""},
    {"nombre": "Dragón de la Cólquida", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Cerbero", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Cerda de Cromión", "derrotado_por": "Teseo", "descripcion": ""},
    {"nombre": "Ortro", "derrotado_por": "Heracles", "descripcion": ""},
    {"nombre": "Toro de Creta", "derrotado_por": "Teseo", "descripcion": ""},
    {"nombre": "Jabalí de Calidón", "derrotado_por": "Atalanta", "descripcion": ""},
    {"nombre": "Carcinos", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Gerión", "derrotado_por": "Heracles", "descripcion": ""},
    {"nombre": "Cloto", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Láquesis", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Átropos", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Minotauro de Creta", "derrotado_por": "Teseo", "descripcion": ""},
    {"nombre": "Harpías", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Argos Panoptes", "derrotado_por": "Hermes", "descripcion": ""},
    {"nombre": "Aves del Estínfalo", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Talos", "derrotado_por":  "Medea", "descripcion": ""},
    {"nombre": "Sirenas", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Pitón", "derrotado_por": "Apolo", "descripcion": ""},
    {"nombre": "Cierva de Cerinea", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Basilisco", "derrotado_por": None, "descripcion": ""},
    {"nombre": "Jabalí de Erimanto", "derrotado_por": None, "descripcion": ""}
]

from tp_arbol import BinaryTree

tree_crituras = BinaryTree()
for criatura in Lcriaturas:
    tree_crituras.insert_node(criatura["nombre"], criatura)

"""Value = Criatura | Other_Value = Dios"""

tree_crituras.inorden_with_defeated()

"""Cargar breve descripción de la criatura"""
tree_crituras.add_description("Talos", "Talos era un gigante de bronce en la mitología griega, encargado de proteger la isla de Creta. Patrullaba la isla lanzando rocas o quemando a los invasores con su calor.")
print(tree_crituras.search("Talos").other_value["descripcion"])

"""Mostrar infomacion de Talos"""
print()
tree_crituras.show_creature("Talos")

"""3 dioses que derrotaron mayor cantidad de Criaturas"""
print()
print("3 dioses que derrotaron mayor cantidad de Criaturas:")
print(tree_crituras.dios_more_common())

"""Criaturas derrotadas por Heracles"""
tree_crituras.defeated_by("Heracles")

"""Criaturas que no han sido derrotadas"""
print()
print("Criaturas que no han sido derrotadas")
tree_crituras.not_defeated()

"""Agrego el campo de capturado por a la lista Lcriaturas"""
for criatura in Lcriaturas:
        criatura["capturado_por"] = ""


"""Agregar dioses que capturaron a las criaturas"""
tree_crituras.add_captured_by("Cerbero", "Heracles")
tree_crituras.add_captured_by("Toro de Creta", "Heracles")
tree_crituras.add_captured_by("Cierva de Cerinea", "Heracles")
tree_crituras.add_captured_by("Jabalí de Erimanto", "Heracles")

"""Busqueda por coincidencia"""
print()
print("Buscando criatura...")
criatura = "Cerbero"
criaturaBuscada = tree_crituras.search(criatura)
if criaturaBuscada is not None:
      print(f"{criaturaBuscada.value}: ")
      print(f"Descripcion: {criaturaBuscada.other_value['descripcion']}")
      print(f"Derrotado por: {criaturaBuscada.other_value['derrotado_por']}")
      print(f"Capturado por: {criaturaBuscada.other_value['capturado_por']}")
else:
      print("No se encontro la criatura 'Cerbero'")

"""Mostrar criaturas capturadas por Heracles"""
print()
eliminado = tree_crituras.delete_node("Basilisco")
if eliminado is not None:
      print(f"Criatura eliminada: {eliminado}")
else:
      print("No se encontro la criatura")

eliminado = tree_crituras.delete_node("Sirenas")
if eliminado is not None:
      print(f"Criatura eliminada: {eliminado}")
else:
      print("No se encontro la criatura")

"""Modificar las Aves del Estinfalo y agregar que fueron varias derrotadas por Heracles"""
tree_crituras.add_defeated_by("Aves del Estínfalo", "Heracles")
tree_crituras.add_description("Aves del Estínfalo", "Derrotadas muchas veses por el dios Heracles")
tree_crituras.show_creature("Aves del Estínfalo")

"""Modificar criatura Ladon por Dragon Ladon"""
if tree_crituras.change_name("Ladón", "Dragón Ladón") is not None:
      print("Criatura modificada correctamente")
tree_crituras.show_creature("Dragón Ladón")

"""Mostrar listado by_level"""
print()
tree_crituras.by_level_criaturas()


"""Mostrar criaturas capturadas por Heracles"""
print()
print("Criaturas capturadas por Heracles:")
tree_crituras.captured_by("Heracles")

