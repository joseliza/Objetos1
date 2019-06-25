class Contacto:
    '''Clase contacto'''
    todos_contactos = []

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        Contacto.todos_contactos.append(self)


class Vendedor(Contacto):
    '''Clase vendedor que hereda de la clase contacto'''


    def pedido(self, pedido):
        print("En una aplicación completa enviaría el pedido "
        "{} pedido a {}".format(pedido, self.nombre))
