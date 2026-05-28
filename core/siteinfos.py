class Banner:
    def __init__(self, img,titulo,frase,botao):
        self.set_img(img)
        self.set_titulo(titulo)
        self.set_frase(frase)
        self.set_botao(botao)
    
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
    def __init__(self, h1, descricao):
        self.set_h1(h1)
        self.set_descricao(descricao)
        self.cards = []

    def get_h1(self):
        return self.h1
    def set_h1(self, h1):
        self.h1 = h1

    def get_descricao(self):
        return self.descricao
    def set_descricao(self, descricao):
        self.descricao = descricao

    def add_cards(self, *cards):     # *args usado para passar mais de um parâmetro
        for card in cards:
            self.cards.append(card)
    def get_cards(self):
        return self.cards


class CardSecao:
    def __init__(self, icone,titulo,descricaoCard):
        self.set_icone(icone)
        self.set_titulo(titulo)
        self.set_descricaoCard(descricaoCard)
    
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
    

class FooterDivs:
    def __init__(self, titulo):
        self.set_titulo(titulo)
        self.items = []

    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_titulo(self):
        return self.titulo
    
    def add_items(self, *itens):
        for item in itens:
            self.items.append(item)
    def get_items(self):
        return self.items


class FooterItem:
    def __init__(self, titulo,icone=None, url=None):
        self.set_titulo(titulo)
        self.set_icone(icone)
        self.set_url(url)
    
    def get_titulo(self):
        return self.titulo
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_icone(self):
        return self.icone
    def set_icone(self, icone):
        self.icone = icone
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url


class FooterLinkItem(FooterItem):
    def __init__(self,titulo,url):
        super().__init__(titulo, icone = None, url=url)
        self.item_type = 'LINK'
    
    def get_item_type(self):
        return self.item_type
    def set_item_type(self, item_type):
        self.item_type = item_type


class FooterIconeItem(FooterItem):
    def __init__(self, titulo, icone, url = None):
        super().__init__(titulo, icone, url)
        self.item_type = 'ICONE'

    def get_item_type(self):
        return self.item_type
    def set_item_type(self, item_type):
        self.item_type = item_type
    

class FooterSocialItem(FooterItem):
    def __init__(self, titulo, icone, url):
        super().__init__(titulo, icone, url)
        self.item_type = 'SOCIAL'

    def get_item_type(self):
        return self.item_type
    def set_item_type(self, item_type):
        self.item_type = item_type


