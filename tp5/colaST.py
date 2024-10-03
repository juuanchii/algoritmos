

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, name, planet):
        self.__elements.append({"nombre": name, "planeta": planet})

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element["nombre"], element["planeta"])

