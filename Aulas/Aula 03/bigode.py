lista_grande = list(range(1000000))

n = int(input("Digite um número de dígitos para serem removidos da lista(de 0 até n): "))

def bigode_nn(n):
    for i in range(n):
        lista_grande.pop(0)

def bigode_n(n):
    return lista_grande[n:]

lista = bigode_n(n)
print(lista)