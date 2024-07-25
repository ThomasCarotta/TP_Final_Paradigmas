def numeros():
    numeros = []
    for i in range(48, 57):
        num = chr(i)
        numeros.append(num)
    return numeros

def letras():
    letras = []
    for i in range(97, 123):
        min = chr(i)
        letras.append(min)
    for i in range(65, 91):
        mas = chr(i)
        letras.append(mas)
    return letras
