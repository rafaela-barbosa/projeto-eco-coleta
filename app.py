from flask import Flask, render_template
from siteinfos import Banner, Secao, CardSecao

app = Flask(__name__)


banner = Banner()
banner.set_titulo('Transforme seu descarte em um ato de amor ao planeta')
banner.set_frase('O EcoColeta conecta você aos pontos de coleta seletiva mais próximos, tornando a reciclagem mais fácilacessível e eficiente para todos. Faça parte dessa transformação e ajude a construir um futuro mais sustentável.')
banner.set_img('img/banner.jpeg')
banner.set_botao('Buscar Ponto próximo')

cardBeneficio01 = CardSecao()
cardBeneficio01.set_icone('location-dot')
cardBeneficio01.set_titulo('Encontre pontos de coleta Próximos')
cardBeneficio01.set_descricaoCard('Localize facilmente os pontos de coleta seletiva mais próximos de você, economizando tempo e facilitando o descarte correto dos seus resíduos.')

cardBeneficio02 = CardSecao()
cardBeneficio02.set_icone('earth-americas')
cardBeneficio02.set_titulo('Contribua para um mundo sustentável')
cardBeneficio02.set_descricaoCard('Cada item reciclado corretamente representa um passo importante na preservação dos recursos naturais e na redução da poluição ambiental.')

cardBeneficio03 = CardSecao()
cardBeneficio03.set_icone('book-open-reader')
cardBeneficio03.set_titulo('Aprenda sobre separação de resíduos')
cardBeneficio03.set_descricaoCard('Acesse informações detalhadas sobre como separar corretamente seus resíduos, maximizando o potencial de reciclagem de cada material.')

cardMaterial01 = CardSecao()
cardMaterial01.set_icone('file-lines')
cardMaterial01.set_titulo('Papel')
cardMaterial01.set_descricaoCard('Inclui jornais, revistas, caixas de papelão, envelopes e papel de escritório. Devem estar limpos e secos para reciclagem')

cardMaterial02 = CardSecao()
cardMaterial02.set_icone('bottle-water')
cardMaterial02.set_titulo('Plástico')
cardMaterial02.set_descricaoCard('Garrafas PET, embalagens de produtos de limpeza, sacolas e outros plásticos. Devem estar limpos e sem resíduos.')

cardMaterial03 = CardSecao()
cardMaterial03.set_icone('glass-water')
cardMaterial03.set_titulo('Vidro')
cardMaterial03.set_descricaoCard('Garrafas, potes e frascos de vidro. Devem ser separados por cor e sem tampas metálicas para melhor reciclagem.')

cardMaterial04 = CardSecao()
cardMaterial04.set_icone('wrench')
cardMaterial04.set_titulo('Metal')
cardMaterial04.set_descricaoCard('Latas de alumínio, conservas, tampas metálicas e outros objetos metálicos pequenos podem ser reciclados.')

cardMaterial05 = CardSecao()
cardMaterial05.set_icone('computer')
cardMaterial05.set_titulo('Eletrônicos')
cardMaterial05.set_descricaoCard('Equipamentos eletrônicos, pilhas e baterias requerem descarte especial em pontos de coleta específicos.')


secao01 = Secao()
secao01.set_h1('Benefícios do EcoColeta')
secao01.set_descricao('Descubra como nossa plataforma pode facilitar sua jornada rumo a habitos mais sustentáveis e contribuir para um planeta mais saudável.')
secao01.add_cards(cardBeneficio01)
secao01.add_cards(cardBeneficio02)
secao01.add_cards(cardBeneficio03)

secao02 = Secao()
secao02.set_h1('Materiais Recicláveis')
secao02.set_descricao('Conheça os diferentes tipos de materiais que podem ser reciclados e como descartá-los corretamente para garantir um processo de reciclagem eficiente.')
secao02.add_cards(cardMaterial01)
secao02.add_cards(cardMaterial02)
secao02.add_cards(cardMaterial03)
secao02.add_cards(cardMaterial04)
secao02.add_cards(cardMaterial05)

lista_secao = [secao01, secao02]



@app.route("/")
def home():
    return render_template('index.html', secoes = lista_secao, banner_info = banner)

@app.route("/mapa")
def mapa():
    return render_template('mapa.html')

@app.route("/como-funciona")
def como_funciona():
    return render_template('como_funciona.html')

@app.route("/materiais")
def materiais():
    return render_template('materiais.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')




if __name__ == '__main__':
    app.run(debug=True)