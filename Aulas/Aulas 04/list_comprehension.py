
def jeito_antigo(numeros:list) -> list:
    final = []
    for n in numeros:
        if n % 2 == 0:
            final.append(n**2)
    return final

def jeito_novo(numeros:list) -> list:
    return [n**2 for n in numeros if n % 2 == 0]


if __name__ == '__main__':
    lista_numeros = list(range(int(input('Digite o valor final da lista: '))))

    antigo = jeito_antigo(lista_numeros)
    print(f'Antigo: {antigo}')

    novo = jeito_novo(lista_numeros)
    print(f'Novo: {novo}')