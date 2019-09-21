class ConversorCesar:
    def __init__(self):
        pass

    def cifrar(self, texto):
        cifra = ''
        for i in range(0, len(texto)):
            letra = texto[i]
            code = ord(letra)
            if code == 88:
                code = 65
            elif code == 89:
                code = 66
            elif code == 90:
                code = 67
            else: 
                code = code + 3
            letraAux = chr(code)
            cifra = cifra + letraAux
        return cifra

    def decifrar(self, cifra):
        texto = ''
        for i in range(0, len(cifra)):
            letra = cifra[i]
            code = ord(letra)
            if code == 65:
                code = 88
            elif code == 66:
                code = 89
            elif code == 67:
                code = 90
            else: 
                code = code - 3
            letraAux = chr(code)
            texto = texto + letraAux
        return texto

if __name__ == "__main__":
    conversor = ConversorCesar()
    cifrado = conversor.cifrar("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(cifrado)
    texto = conversor.decifrar(cifrado)
    print(texto)

    