import math

# Aprendiendo objetos

class Punto:
    def mover(self, x, y):
        self.x = x
        self.y = y

    def reiniciar(self):
        self.mover(0, 0)

    def calcular_distancia(self, otro_punto):
        return math.sqrt(
            (self.x - otro_punto.x)**2 +
            (self.y - otro_punto.y)**2)

punto1 = Punto()
punto2 = Punto()

punto1.reiniciar()
punto2.mover(5,0)


print(punto1.x, punto1.y)
print(punto2.x, punto2.y)

print(punto1.calcular_distancia(punto2))
