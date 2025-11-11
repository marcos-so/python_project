# Dada a lista numeros = , use uma list comprehension para
# criar uma nova lista contendo apenas os números que são maiores que 8.


numbers = [5,12,67,6,4,9,8,21,7,3,45,2]

def greater_than(numbers:int, greaterThan:int=8) -> list:
    return [num for num in numbers if num > greaterThan]

if __name__ == '__main__':
    # greater = int(input('Informe o valor de comparação: '))
    # numbers = greater_than(list(range(1, int(input('Informe o tamanho da lista(de 1 até n):')) + 1)), greater)

    resultado = sorted(greater_than(numbers))
    print(f'Resultado: {resultado}')