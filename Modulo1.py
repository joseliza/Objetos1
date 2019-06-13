import math

# Aprendiendo objetos


class Punto:
    'Representa un punto en coordenadas geométricas bidimensionales'
    def __init__(self, x=0, y=0):
        '''Inicializa la posición de un nuevo punto. Las coordenadas x e y pueden
        ser especificadas. Si no lo son, el punto por defecto derá el origen.'''
        self.mover(x, y)

    def mover(self, x, y):
        "Mueve el punto a una nueva localización en un espacio bidimensional."
        self.x = x
        self.y = y

    def reiniciar(self):
        "Reinicia el puntp al origen de coordenadas."
        self.mover(0, 0)

    def calcular_distancia(self, otro_punto):
        """Calcula la distancia desde este punto a un segundo punto pasado como parámetro.
        Esta función usa el Teorema de Pitágoras para calcular la distancia entre puntos. La
        distancia es devuelta como un float."""
        return math.sqrt(
            (self.x - otro_punto.x)**2 +
            (self.y - otro_punto.y)**2)


punto1 = Punto()
punto2 = Punto()

punto2.mover(5,0)


print(punto1.x, punto1.y)
print(punto2.x, punto2.y)

print(punto1.calcular_distancia(punto2))

punto3 = Punto(3)
print(punto3.x)