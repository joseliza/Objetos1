class StringSecreto:
    '''Uso de Name Manging --> Un modo no totalmente seguro de almacenar un secreto.'''
    def __init__(self, string_plano, frase_pass):
        self.__string_plano = string_plano
        self.__frase_pass = frase_pass

    def decrypt(self, frase_pass):
        if frase_pass == self.__frase_pass:
            return  self.__string_plano
        else:
            return ''

def main ():
    string_secreto = StringSecreto("Esta es la frase secreta", "Esta es la clave")
    print(string_secreto.decrypt("Esta es la clave"))
    print(string_secreto._StringSecreto__string_plano)


if __name__ == '__main__':
    main()


