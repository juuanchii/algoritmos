actividades = [
    ["Kylo Ren", "Cazar a Rey Skywalker", "14:36", "1000"],
    ["Snoke", "Supervisar la construcción de la nueva base Starkiller", "10:00", "200"],
    ["Capitán Phasma", "Entrenar nuevas unidades de Stormtroopers", "12:15", "300"],
    ["Capitán Phasma", "Patrullar la base", "15:45", "150"],
    ["Capitán Phasma", "Supervisar la logística de armas", "19:00", "200"],
    ["Capitán Phasma", "Organizar la defensa de la base", "21:00", "250"],
    ["General Hux", "Planear la invasión de la resistencia", "09:45", "500"],
    ["General Hux", "Asegurar la lealtad de los sistemas imperiales", "16:00", "350"],
    ["General Pryde", "Coordinar ataques en sistemas exteriores", "11:30", "150"],
    ["General Pryde", "Inspeccionar la flota de destructores estelares", "18:20", "100"]
]
"""Encargado - Operacion - Hora - Stormtroopers"""


from heap import HeapMax

starKiller = HeapMax()

for operacion in actividades:
    if operacion[0] in ['Kylo Ren', 'Snoke']:
        starKiller.arrive(operacion, 3)
    if operacion[0][:7] in ['Capitán']:
        starKiller.arrive(operacion, 2)
    if operacion[0][:7] in ['General']:
        starKiller.arrive(operacion, 1)

"""opcionalmente se podrán agregar operaciones luego de atender una"""
nueva_actividad = ["Capitán C", "Comandar el ataque a la flota rebelde", "08:30", "400"]

actividad_completada = starKiller.atention()[1]
print()
print(f"Actividad {actividad_completada[1]} COMPLETADA! -> Encargado {actividad_completada[0]}  -> hora {actividad_completada[2]} -> Stormtroopers: {actividad_completada[3]}")
print()

starKiller.arrive(nueva_actividad, 2)
print("Nueva actividad... actividades pendientes: ")
# for operacion in starKiller.sort():
#     print(f"Prioridad {operacion[0]} Encargado: {operacion[1][0]} - Operación: {operacion[1][1]} - Hora: {operacion[1][2]} - Stormtroopers: {operacion[1][3]}")

print()
operacion_Phasma = ["Capitán P", "Revisión de intrusos en el hangar B7", "17:30", "25"]

for i in range(len(starKiller.elements)):
    operacion = starKiller.atention()[1]
    print(f"Actividad {operacion[1]} COMPLETADA! -> Encargado {operacion[0]}")

    if operacion[0][:7] == 'Capitán' and i == 5:
        starKiller.arrive(operacion_Phasma, 2)
        print("\n================================================")
        print("Nueva actividad para el capitán Phastam agregada ")
        print("================================================")
        break

print()
print("Actividades pendientes... ")
while len(starKiller.elements) > 0:
    operacion = starKiller.atention()[1]
    print(f" {operacion[1]} -> Encargado {operacion[0]}  -> Hora: {operacion[2]} -> Stormtroopers: {operacion[3]}")

