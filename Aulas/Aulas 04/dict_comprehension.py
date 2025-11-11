lista_nomes:list = ['João', 'Maria', 'Fábio', 'Ana', 'Marcos', 'Marta']

dict_masc = {nome:'Masculino' for nome in lista_nomes if nome[-1] == 'o'}
dict_fem = {nome:'Feminino' for nome in lista_nomes if nome[-1] == 'a'}

if __name__ == '__main__':
    print(f'Dicionário Masculino: {dict_masc}')
    print(f'Dicionário Feminino: {dict_fem}')
