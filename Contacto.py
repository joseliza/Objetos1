class Contacto:
    todos_contactos = []

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        Contacto.todos_contactos.append(self)