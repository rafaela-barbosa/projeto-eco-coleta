from django.shortcuts import render
from .siteinfos import Banner, CardSecao, Secao, FooterIconeItem, FooterSocialItem, FooterLinkItem, FooterDivs


# --- DADOS FOOTER ---
contato_email = FooterIconeItem('contato@ecocoleta.com.br', 'envelope', url='mailto:contato@ecocoleta.com.br')
contato_endereco = FooterIconeItem('Rio de Janeiro/RJ', 'location-dot')
contato_telefone = FooterIconeItem('(21) 99999-8888', 'phone')

social_insta = FooterSocialItem('Instagram', 'instagram', 'https://instagram.com')
social_facebook = FooterSocialItem('Facebook', 'facebook', 'https://facebook.com')
social_xtwitter = FooterSocialItem('X', 'x-twitter', 'https://x.com')

link_home = FooterLinkItem('Início', '/')
link_como_funciona = FooterLinkItem('Como Funciona', '/como-funciona')
link_mapa = FooterLinkItem('Pontos de Coleta', '/mapa')
link_materiais = FooterLinkItem('Materiais', '/materiais')

footerdiv01 = FooterDivs('Redes Sociais')
footerdiv01.add_items(social_insta, social_facebook, social_xtwitter)

footerdiv02 = FooterDivs('Links Rápidos')
footerdiv02.add_items(link_home, link_como_funciona, link_materiais, link_mapa)

footerdiv03 = FooterDivs('Contato')
footerdiv03.add_items(contato_endereco, contato_telefone, contato_email)

lista_footerdivs = [footerdiv01, footerdiv02, footerdiv03]

# --- DADOS PÁGINA HOME ---
banner = Banner(
    'img/banner.jpeg',
    'Transforme seu descarte em um ato de amor ao planeta',
    'O EcoColeta conecta você aos pontos de coleta seletiva mais próximos, tornando a reciclagem mais fácil acessível e eficiente para todos. Faça parte dessa transformação e ajude a construir um futuro mais sustentável.',
    'Buscar Ponto próximo'
)

cardBeneficio01 = CardSecao('location-dot', 'Encontre pontos de coleta Próximos', 'Localize facilmente os pontos de coleta seletiva mais próximos de você, economizando tempo e facilitando o descarte correto dos seus resíduos.')
cardBeneficio02 = CardSecao('earth-americas', 'Contribua para um mundo sustentável', 'Cada item reciclado corretamente representa um passo importante na preservação dos recursos naturais e na redução da poluição ambiental.')
cardBeneficio03 = CardSecao('book-open-reader', 'Aprenda sobre separação de resíduos', 'Acesse informações detalhadas sobre como separar corretamente seus resíduos, maximizando o potencial de reciclagem de cada material.')

secao01 = Secao('Benefícios do EcoColeta', 'Descubra como nossa plataforma pode facilitar sua jornada rumo a habitos mais sustentáveis e contribuir para um planeta mais saudável.')
secao01.add_cards(cardBeneficio01, cardBeneficio02, cardBeneficio03)

cardMaterial01 = CardSecao('file-lines', 'Papel', 'Inclui jornais, revistas, caixas de papelão, envelopes e papel de escritório. Devem estar limpos e secos para reciclagem')
cardMaterial02 = CardSecao('bottle-water', 'Plástico', 'Garrafas PET, embalagens de produtos de limpeza, sacolas e outros plásticos. Devem estar limpos e sem resíduos.')
cardMaterial03 = CardSecao('glass-water', 'Vidro', 'Garrafas, potes e frascos de vidro. Devem ser separados por cor e sem tampas metálicas para melhor reciclagem.')
cardMaterial04 = CardSecao('wrench', 'Metal', 'Latas de alumínio, conservas, tampas metálicas e outros objetos metálicos pequenos podem ser reciclados.')
cardMaterial05 = CardSecao('computer', 'Eletrônicos', 'Equipamentos eletrônicos, pilhas e baterias requerem descarte especial em pontos de coleta específicos.')

secao02 = Secao('Materiais Recicláveis', 'Conheça os diferentes tipos de materiais que podem ser reciclados e como descartá-los corretamente para garantir um processo de reciclagem eficiente.')
secao02.add_cards(cardMaterial01, cardMaterial02, cardMaterial03, cardMaterial04, cardMaterial05)

lista_secao = [secao01, secao02]


# --- DADOS PÁGINA MATERIAIS ---
card_vidro = CardSecao('wine-glass', 'Vidro', 'Garrafas, potes e frascos. Remova as tampas e lave para retirar resíduos orgânicos.')
card_plastico = CardSecao('recycle', 'Plástico', 'Embalagens PET, potes de comida e produtos de limpeza. Atenção: não reciclamos adesivos.')
card_papel = CardSecao('file-lines', 'Papel e Papelão', 'Jornais, revistas e caixas. O papel deve estar seco e sem restos de comida ou fita adesiva.')
card_metal = CardSecao('faucet-drip', 'Metal', 'Latas de alumínio e aço. Amasse as latas para facilitar o transporte e armazenamento.')

secao_materiais = Secao('Guia de Materiais Recicláveis', 'Entenda o que pode ser descartado em nossos pontos de coleta e como preparar cada item.')
secao_materiais.add_cards(card_vidro, card_plastico, card_papel, card_metal)


# --- DADOS PAGINA COMO_FUNCIONA ---
secao_como_funciona = Secao('Passo a Passo para Reciclar', 'Aprenda como utilizar nossa plataforma e descartar seus resíduos de forma responsável em apenas 3 etapas.')
card_passo1 = CardSecao('magnifying-glass', '1. Localize', 'Use nosso mapa para encontrar o ponto de coleta mais próximo da sua casa.')
card_passo2 = CardSecao('hand-sparkles', '2. Prepare', 'Separe os materiais por tipo e certifique-se de que estão limpos e secos.')
card_passo3 = CardSecao('truck-moving', '3. Descarte', 'Leve os resíduos até o local indicado e faça sua parte pelo planeta!')
secao_como_funciona.add_cards(card_passo1, card_passo2, card_passo3)


def home(request):
    context = {
        'banner_info': banner,
        'secoes': lista_secao,
        'footerdivs': lista_footerdivs
    }
    return render(request, 'index.html', context)

def materiais(request):
    context = {
        'secao': secao_materiais,
        'footerdivs': lista_footerdivs
    }
    return render(request, 'materiais.html', context)

def como_funciona(request):
    context = {
        'secao': secao_como_funciona,
        'footerdivs': lista_footerdivs
    }
    return render(request, 'como_funciona.html', context)

def mapa(request):
    context = {
        'footerdivs': lista_footerdivs
    }
    return render(request, 'mapa.html', context)

def contato(request):
    context = {
        'footerdivs': lista_footerdivs
    }
    return render(request, 'contato.html', context)