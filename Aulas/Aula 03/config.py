class Config:

    def __init__(self, **kwargs):
        self.dict = kwargs

    def __str__(self):
        return f'Configurações: host={self.dict.get("host")}, port={self.dict.get("port")}, timeout={self.dict.get("timeout")}'

    def __repr__(self):
        return f'Config(settings={self.dict})'

    def __call__(self, key=None):
        print('Configurações Atuais:')
        if key:
            print(f'{key} = {self.dict.get(key)}')
        else:
            for k, v in self.dict.items():
                print(f'{k} = {v}')

if __name__ == '__main__':
    config = Config(host='localhost', port=8080, timeout=30)
    # config_inc = Config(host='localhost')
    # print(repr(config))
    # print(config)

    config()