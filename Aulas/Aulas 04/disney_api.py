import requests
from json import loads as json_loads

# URL = 'https://api.disneyapi.dev/'

# def get_characters(page=1):
#     response = requests.get(f'{URL}character?page={page}')
#     print(response)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# if __name__ == "__main__":
#     characters = get_characters(2)
#     if characters:
#         for character in characters['data']:
#             print(f"Name: {character['name']}, Films: {', '.join(character['films'])}")
#     else:
#         print("Failed to retrieve data from the Disney API.")

## Resolução do Professor

# import requests
# from json import loads as json_loads

# BASE_URL = 'https://api.disneyapi.dev'

# FETCH = 'character'

# query = f'{BASE_URL}/{FETCH}?name=Mickey%20Mouse'
# get_all = f'{BASE_URL}/{FETCH}'
# get_by_id = f'{BASE_URL}/{FETCH}/308'

# all_chars = requests.get(query).content
# meus_chars = json_loads(all_chars)['data']
# char_1, char_2 = meus_chars
# print(char_1)
# input()
# print(char_2)

BASE_URL = 'https://api.disneyapi.dev'
FETCH = 'character'

class Disney:

    def __init__(self, id:int):
        self.id:int = id
        info = self.chamar_personagem()
        self.url:str = info.get('url')
        self.name:str = info.get('name')
        self.image_url:str = info.get('imageUrl')
        self.films:list[str] = info.get('films')
        self.short_films:list[str] = info.get('shortFilms')
        self.tv_shows:list[str] = info.get('tvShows')
        self.video_games:list[str] = info.get('videoGames')
        self.park_attractions:list[str] = info.get('parkAttractions')
        self.allies:list[str] = info.get('allies')
        self.enemies:list[str] = info.get('enemies')

    def chamar_personagem(self) -> dict:
        response:requests = requests.get(f'{BASE_URL}/{FETCH}/{self.id}')
        raw_content:bytes = response.content
        parsed_content:dict = json_loads(raw_content)['data']
        return dict(parsed_content)

if __name__ == '__main__':
    try:
        for n in range(1, 9000):
            id = n
            char = Disney(id)
            if char.name is not None:
                print(f'{id}:{char.name}')
    except KeyboardInterrupt:
        exit()