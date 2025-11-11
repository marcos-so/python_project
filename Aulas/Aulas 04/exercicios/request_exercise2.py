import requests

BASE_URL = 'https://api.disneyapi.dev/character'


class Disney:
    def __init__(self, character_id: int):
        self.id = character_id
        info = self.chamar_personagem()
        self.url = info.get('url', '')
        self.name = info.get('name', 'Desconhecido')
        self.image_url = info.get('imageUrl', '')
        self.films = info.get('films', [])
        self.short_films = info.get('shortFilms', [])
        self.tv_shows = info.get('tvShows', [])
        self.video_games = info.get('videoGames', [])
        self.park_attractions = info.get('parkAttractions', [])
        self.allies = info.get('allies', [])
        self.enemies = info.get('enemies', [])

    def chamar_personagem(self) -> dict:
        '''
        Faz a requisição para a API Disney e retorna as informações do personagem como um dicionário

        Função
        -------
        Esta função tem como objetivo trazer as informaçOes do personagem da Dinsey através de uma request na API associada a variável BASE_URL.

        Retorna
        -------

        A função retorna um dicionário contendo as informações do personagem obtidas da API Disney.

        Exemplo
        ------
        >>> dicionario:dict = self.chamar_personagem()
        '''

        try:
            response = requests.get(f'{BASE_URL}/{self.id}', timeout=10)
            response.raise_for_status()
            return response.json().get('data', {})
        except (requests.RequestException, ValueError):
            return {}

    def __str__(self) -> str:
        sections = [
            f'Nome: {self.name}',
            f'Imagem: {self.image_url}',
            'Filmes:',
            *[f'    {film}' for film in self.films],
            'Video Games:',
            *[f'    {game}' for game in self.video_games]
        ]
        return '\n'.join(sections)


if __name__ == '__main__':
    try:
        personagem = Disney(309)
        print(personagem)
    except KeyboardInterrupt:
        print('\nEncerrado pelo usuário.')
