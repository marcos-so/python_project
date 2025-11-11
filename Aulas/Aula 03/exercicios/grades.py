# Escreva uma função processar_notas(notas: list) que recebe uma lista de notas (floats). A função deve remover a nota mais baixa e, em seguida, calcular e retornar a média das notas restantes.

# [sort;min;remove]

def processar_notas(notas: list) -> float:
    notas.sort()
    print(f'Notas ordenadas: {notas}')
    if len(notas) <= 1:
        return 0.0
    nota_minima = min(notas)
    notas.remove(nota_minima)
    media = sum(notas) / len(notas)
    return [media, nota_minima]

if __name__ == '__main__':
    notas = [7.5, 8.0, 6.0, 9.0, 5.5]
    media = processar_notas(notas)
    print(f'Nota mais baixa removida: {media[1]}')
    print(f'Média das notas após remover a mais baixa: {media[0]:.2f}')