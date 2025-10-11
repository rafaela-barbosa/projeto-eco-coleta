from flask import Flask, render_template
from siteinfos import Banner, Secao, CardSecao, FooterDivs, FooterIconeItem, FooterLinkItem, FooterSocialItem

app = Flask(__name__)


banner = Banner( # Padrão de set: icone, titulo, descricao, botao
    'img/banner.jpeg',
    'Transforme seu descarte em um ato de amor ao planeta',
    'O EcoColeta conecta você aos pontos de coleta seletiva mais próximos, tornando a reciclagem mais fácilacessível e eficiente para todos. Faça parte dessa transformação e ajude a construir um futuro mais sustentável.',
    'Buscar Ponto próximo')

cardBeneficio01 = CardSecao( # Padrão de set: icone, titulo, descricao
    'location-dot',
    'Encontre pontos de coleta Próximos',
    'Localize facilmente os pontos de coleta seletiva mais próximos de você, economizando tempo e facilitando o descarte correto dos seus resíduos.')
cardBeneficio02 = CardSecao(
    'earth-americas',
    'Contribua para um mundo sustentável',
    'Cada item reciclado corretamente representa um passo importante na preservação dos recursos naturais e na redução da poluição ambiental.')
cardBeneficio03 = CardSecao(
    'book-open-reader',
    'Aprenda sobre separação de resíduos',
    'Acesse informações detalhadas sobre como separar corretamente seus resíduos, maximizando o potencial de reciclagem de cada material.')
cardMaterial01 = CardSecao(
    'file-lines',
    'Papel',
    'Inclui jornais, revistas, caixas de papelão, envelopes e papel de escritório. Devem estar limpos e secos para reciclagem')
cardMaterial02 = CardSecao(
    'bottle-water',
    'Plástico',
    'Garrafas PET, embalagens de produtos de limpeza, sacolas e outros plásticos. Devem estar limpos e sem resíduos.')
cardMaterial03 = CardSecao(
    'glass-water',
    'Vidro',
    'Garrafas, potes e frascos de vidro. Devem ser separados por cor e sem tampas metálicas para melhor reciclagem.')
cardMaterial04 = CardSecao(
    'wrench',
    'Metal',
    'Latas de alumínio, conservas, tampas metálicas e outros objetos metálicos pequenos podem ser reciclados.')
cardMaterial05 = CardSecao(
    'computer',
    'Eletrônicos',
    'Equipamentos eletrônicos, pilhas e baterias requerem descarte especial em pontos de coleta específicos.')

secao01 = Secao( # Padrão de set: h1, descricao
    'Benefícios do EcoColeta',
    'Descubra como nossa plataforma pode facilitar sua jornada rumo a habitos mais sustentáveis e contribuir para um planeta mais saudável.'
)
secao01.add_cards(cardBeneficio01)
secao01.add_cards(cardBeneficio02)
secao01.add_cards(cardBeneficio03)

secao02 = Secao(
    'Materiais Recicláveis',
    'Conheça os diferentes tipos de materiais que podem ser reciclados e como descartá-los corretamente para garantir um processo de reciclagem eficiente.'
)
secao02.add_cards(cardMaterial01)
secao02.add_cards(cardMaterial02)
secao02.add_cards(cardMaterial03)
secao02.add_cards(cardMaterial04)
secao02.add_cards(cardMaterial05)

lista_secao = [secao01, secao02]

contato_email = FooterIconeItem( # Padrão de set: titulo, icone, url(opcional)
    'contato@ecocoleta.com.br','envelope', url='contato@ecocoleta.com.br')
contato_endereco = FooterIconeItem(
    'Rio de Janeiro/RJ', 'location-dot')
contato_telefone = FooterIconeItem(
    '(21) 99999-8888', 'phone')

social_insta = FooterSocialItem( # Padão de set: titulo, icone, url
    'Instagram', 'instagram', 'https://instagram.com')
social_facebook = FooterSocialItem(
    'Facebook', 'facebook', 'https://facebook.com')
social_xtwitter = FooterSocialItem(
    'X', 'x-twitter', 'https://x.com')

link_home = FooterLinkItem( # Padrão de set: titulo, icone(opcional), url
    'Início', '/')
link_como_funciona = FooterLinkItem('Como Funciona', '/como-funciona')
link_mapa = FooterLinkItem('Pontos de Coleta', '/mapa')
link_materiais = FooterLinkItem('Materiais', '/materiais')

footerdiv01 = FooterDivs('Redes Sociais')
footerdiv01.add_items(social_insta)
footerdiv01.add_items(social_facebook)
footerdiv01.add_items(social_xtwitter)
footerdiv02 = FooterDivs('Links Rápidos')
footerdiv02.add_items(link_home)
footerdiv02.add_items(link_como_funciona)
footerdiv02.add_items(link_materiais)
footerdiv02.add_items(link_mapa)
footerdiv03 = FooterDivs('Contato')
footerdiv03.add_items(contato_endereco)
footerdiv03.add_items(contato_telefone)
footerdiv03.add_items(contato_email)

lista_footerdivs = [footerdiv01, footerdiv02, footerdiv03]

@app.route("/")
def home():
    return render_template('index.html', secoes = lista_secao, banner_info = banner, footerdivs = lista_footerdivs)

@app.route("/mapa")
def mapa():
    return render_template('mapa.html', footerdivs = lista_footerdivs)

@app.route("/como-funciona")
def como_funciona():
    return render_template('como_funciona.html', footerdivs = lista_footerdivs)

@app.route("/materiais")
def materiais():
    return render_template('materiais.html', footerdivs = lista_footerdivs)

@app.route("/contato")
def contato():
    return render_template('contato.html', footerdivs = lista_footerdivs)




if __name__ == '__main__':
    app.run(debug=True)