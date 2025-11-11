# > Ex 01:

# Dada a lista nomes = ['ana', 'bruno', 'carla'], use uma
# list comprehension para criar duas novas listas:

# - Uma onde cada nome esteja em letras maiúsculas.
# - Outra em CammelCase

# == nomes = ['ana', 'bruno', 'carla']
names = ['ana', 'bruno', 'carla', 'marcos', 'juliana', 'roberto', 'patricia', 'carlos', 'fernanda']

def camel_case_names(names_list: list) -> list:
    return [name.capitalize() for name in names_list]

def upper_case_names(names_list: list) -> list:
    return [name.upper() for name in names_list]


if __name__ == '__main__':
    upper_names = camel_case_names(names)
    print(f'Nomes em CamelCase: {upper_names}')
    print(f'Nomes em letras maiúsculas: {upper_case_names(names)}')