import re

class ConversorCesar:
    def __init__(self):
        pass

    def cifrar(self, texto):
        resultado = re.fullmatch(r'([a-zA-Z]*)', texto)

        if not resultado:
            raise Exception("Texto deve conter somente letras do alfabeto")

        cifra = ''
        for i in range(0, len(texto)):
            letra = texto[i]
            code = ord(letra)
            if code == 88 or code == 120 or code == 89 or code == 121 or code == 90 or code == 122:
                code = code - 23
            else: 
                code = code + 3
            letraAux = chr(code)
            cifra = cifra + letraAux
        return cifra

    def decifrar(self, cifra):
        resultado = re.fullmatch(r'([a-zA-Z]*)', cifra)

        if not resultado:
            raise Exception("Cifra deve conter somente letras do alfabeto")

        texto = ''
        for i in range(0, len(cifra)):
            letra = cifra[i]
            code = ord(letra)
            if code == 65 or code == 66 or code == 67 or code == 97 or code == 98 or code == 99:
                code = code + 23 
            else: 
                code = code - 3
            letraAux = chr(code)
            texto = texto + letraAux
        return texto

if __name__ == "__main__":
    conversor = ConversorCesar()
    cifrado = conversor.cifrar("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    print(cifrado)
    texto = conversor.decifrar(cifrado)
    print(texto)

    