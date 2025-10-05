class Banner:
    def __init__(self):
        self.img = ''
        self.titulo = ''
        self.frase = ''
        self.botao = ''
    
    def get_img(self):
        return self.img
    def set_img(self, img):
        self.img = img
    def get_titulo(self):
        return self.titulo
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_frase(self):
        return self.frase
    def set_frase(self, frase):
        self.frase = frase
    def get_botao(self):
        return self.botao
    def set_botao(self, botao):
        self.botao = botao




class Secao:
    def __init__(self):
        self.h1 = ''
        self.descricao = ''
        self.cards = []

    def get_h1(self):
        return self.h1
    def set_h1(self, h1):
        self.h1 = h1
    def get_descricao(self):
        return self.descricao
    def set_descricao(self, descricao):
        self.descricao = descricao
    def add_cards(self, card):
        self.cards.append(card)
    def get_cards(self):
        return self.cards




class CardSecao:
    def __init__(self):
        self.icone = ''
        self.titulo = ''
        self.descricaoCard = ''
    
    def get_icone(self):
        return self.icone
    def set_icone(self, icone):
        self.icone = icone
    def get_titulo(self):
        return self.titulo
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_descricaoCard(self):
        return self.descricaoCard
    def set_descricaoCard(self, descricaoCard):
        self.descricaoCard = descricaoCard