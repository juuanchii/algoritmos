"""Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:

a.además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;

b. listar los villanos ordenados alfabéticamente; 
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol.
."""

from cola import Queue
from lista import search
from collections import Counter

class BinaryTree:
    
    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.height = 0

    def __init__(self):
        self.root = None

    def setOtherValue(self, value):
        self.other_value = value

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            # print(f'actualizar altura de {root.value}')
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1
            # print(f'altura izq {left_height} altura der {right_height}')
            # print(f'altura de {root.value} es {root.height}')

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                # print('desbalanceado a la izquierda')
                if self.height(root.left.left) >= self.height(root.left.right):
                    # print('rotar simple derecha')
                    root = self.simple_rotation(root, True)
                else:
                    # print('rotar doble derecha')
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                # print('desbalanceado a la derecha')
                if self.height(root.right.right) >= self.height(root.right.left):
                    # print('rotar simple izquierda')
                    root = self.simple_rotation(root, False)
                else:
                    # print('rotar doble izquierda')
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None):
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    # print('lo encontre')
                    return root
                elif key < root.value:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, key)
            # else:
            #     print('no hay nada')
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux
    
    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                # print(f'izquierda de {root.value}')
                __preorden(root.left)
                # print(f'derecha de {root.value}')
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)

    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(f"nivel {node.height}", node.value, node.other_value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

    def height_tree(self):
        pendientes = Queue()
        height = 0
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            if height < node.height:
                height = node.height
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)
        return height
    
    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplaz+ar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    if root.left is None:
                        # print('a la izquierda no hay nada')
                        return root.right, value_delete
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        # return root, value_delete
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value_delete

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, value)
        return delete_value

    """ Funciones modificadas para los ejercicios """

    def inorden_villanos(self):
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value['villano'] is True:
                    print(root.value)
        
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

    def inorden_heroes_startswith(self, start):
        def __inorden_heroes_startswith(root, start):
            if root is not None:
                __inorden_heroes_startswith(root.left, start)
                if root.other_value['villano'] == False and root.value.startswith(start):
                    print(root.value)
                __inorden_heroes_startswith(root.right, start)

        if self.root is not None:
            __inorden_heroes_startswith(self.root, start)

    def count_heroes(self):
        def __count_heroes(root):
            counter = 0
            if root is not None:
                if root.other_value['villano'] is True:
                    counter = 1
                counter += __count_heroes(root.left)
                counter += __count_heroes(root.right)
            return counter

        return __count_heroes(self.root)
    
    def proximity_search(self, search_value):
            def __proximity_search(root, search_value):
                if root is not None:
                    __proximity_search(root.left, search_value)
                    if root.value.startswith(search_value):
                        print(root.value)
                    __proximity_search(root.right, search_value)

            if self.root is not None:
                __proximity_search(self.root, search_value)

    def delete_node_with_values(self, value):
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplaz+ar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            extra_data_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete, extra_data_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete, extra_data_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    extra_data_delete = root.other_value
                    if root.left is None:
                        # print('a la izquierda no hay nada')
                        return root.right, value_delete, extra_data_delete
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete, extra_data_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_value = replace_node.other_value
                        # return root, value_delete
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value_delete, extra_data_delete

        delete_value = None
        extra_data_delete = None
        if self.root is not None:
            self.root, delete_value, extra_data_delete = __delete(self.root, value)
        return delete_value, extra_data_delete

    def postorden_heroes(self):
        def __postorden_heroes(root):
            if root is not None:
                __postorden_heroes(root.right)
                if root.other_value['villano'] is False:
                    print(root.value)
                __postorden_heroes(root.left)

        if self.root is not None:
            __postorden_heroes(self.root)

    def count(self):
        def __count(root):
            counter = 0
            if root is not None:
                counter = 1
                counter += __count(root.left)
                counter += __count(root.right)
            return counter

        return __count(self.root)
    

    """ Funciones modificadas para ejercicio 23 """

    def change_other_value(self, key, ov):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    root.other_value = ov
                    # print('lo encontre')
                    return root
                elif key < root.value:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, key)
            # else:
            #     print('no hay nada')
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux
    
    def inorden_with_defeated(self):
        def __inorden_with_defeated(root):
            if root is not None:
                __inorden_with_defeated(root.left)
                print('----------------------------------------------------------------')
                print(f'    -{root.value}')
                if root.other_value["derrotado_por"] is not None:
                    print(f'        Derrotado por {root.other_value["derrotado_por"]}')
                __inorden_with_defeated(root.right)

        if self.root is not None:
            __inorden_with_defeated(self.root)

    def add_description(self, value_to_change, description):
        delete_value, extra_info = self.delete_node_with_values(value_to_change)
        extra_info['descripcion'] = description
        self.insert_node(extra_info["nombre"], extra_info)

    def show_creature(self, name):
        aux = self.search(name)
        if aux is not None:
            print('----------------------------------------------------------------')
            print(f'    -{aux.value}')
            if aux.other_value["descripcion"] is not None:
                print(f'        Descripcion: {aux.other_value["descripcion"]}')
            if aux.other_value["derrotado_por"] is not None:
                print(f'        Derrotado por: {aux.other_value["derrotado_por"]}')
            print('----------------------------------------------------------------')
        else:
            print('No se encontro el elemento')

    def array_dioses(self):
        array = []
        def __preorden(root):
            if root is not None:
                if root.other_value["derrotado_por"] is not None:
                    array.append(root.other_value["derrotado_por"])
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)
    
        return array
    
    def dios_more_common(self):
        contador = Counter(self.array_dioses())
        return contador.most_common(3)
    
    def defeated_by(self, name):
        def __preorden(root):
            if root is not None:
                if root.other_value["derrotado_por"] == name:
                    if root.other_value["derrotado_por"] is not None:
                        print('----------------------------------------------------------------')
                    print(f'    -{root.value}')
                    if root.other_value["descripcion"] is not None:
                        print(f'        Descripcion: {root.other_value["descripcion"]}')
                    if root.other_value["derrotado_por"] is not None:
                        print(f'        Derrotado por: {root.other_value["derrotado_por"]}')
                    print('----------------------------------------------------------------')
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def not_defeated(self):
        def __preorden(root):
            if root is not None:
                if root.other_value["derrotado_por"] == None:
                    if root.other_value["derrotado_por"] is not None:
                        print('----------------------------------------------------------------')
                    print(f'    -{root.value}')
                    if root.other_value["descripcion"] != "":
                        print(f'        Descripcion: {root.other_value["descripcion"]}')
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def add_captured_by(self, value_to_change, description):
        delete_value, extra_info = self.delete_node_with_values(value_to_change)
        extra_info['capturado_por'] = description
        self.insert_node(extra_info["nombre"], extra_info)
        return delete_value


    def add_defeated_by(self, value_to_change, description):
        delete_value, extra_info = self.delete_node_with_values(value_to_change)
        extra_info['derrotado_por'] = description
        self.insert_node(extra_info["nombre"], extra_info)
        return delete_value

    def change_name(self, name, new_name):
        delete_value, extra_info = self.delete_node_with_values(name)
        if delete_value is not None:
            extra_info['nombre'] = new_name
            self.insert_node(extra_info["nombre"], extra_info)        
        return delete_value
    
    def by_level_criaturas(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            partes = [f"nivel {node.height}", str(node.value)]

            # Agregar las partes opcionales si no están vacías
            if node.other_value['descripcion']:
                partes.append(f"Descripcion: {node.other_value['descripcion']}")
            if node.other_value['derrotado_por']:
                partes.append(f"Derrotado por: {node.other_value['derrotado_por']}")
            if node.other_value['capturado_por']:
                partes.append(f"Capturado por: {node.other_value['capturado_por']}")

            # Unir las partes en una sola cadena y mostrar
            print(" ".join(partes))
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

    def captured_by(self, name):
        def __preorden(root):
            if root is not None:
                if root.other_value["capturado_por"] == name:
                    if root.other_value["capturado_por"] is not None:
                        print('----------------------------------------------------------------')
                    print(f'    -{root.value}')
                    if root.other_value["descripcion"] is not None:
                        print(f'        Descripcion: {root.other_value["descripcion"]}')
                    if root.other_value["capturado_por"] is not None:
                        print(f'        Capturado por: {root.other_value["capturado_por"]}')
                    print('----------------------------------------------------------------')
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)