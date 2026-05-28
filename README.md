## 🌱 EcoColeta: Plataforma de Mapeamento de Pontos de Coleta Seletiva
![Status do Projeto](https://img.shields.io/badge/Status-Em%20Construção-orange.svg)

O EcoColeta é uma plataforma web desenvolvida em Python como parte do Projeto Integrador do curso de Engenharia de Software / Análise e Desenvolvimento de Sistemas.
A ideia surgiu a partir de um interesse pessoal em criar algo voltado à sustentabilidade, conectando tecnologia e responsabilidade ambiental.

O objetivo do projeto é centralizar informações sobre coleta seletiva e permitir que os usuários encontrem pontos de coleta próximos por meio de um mapa interativo. Além disso, a plataforma também fornece conteúdos educativos, como um guia de reciclagem, benefícios da coleta seletiva e materiais aceitos.

Inspirado em sites de prefeituras — simples, informativos e práticos — o EcoColeta busca ser um ambiente acessível, moderno e funcional, unindo informação e ação.

---

### 🔄 Evolução Arquitetural: De Flask para Django Monólito

Originalmente concebido utilizando o microframework Flask, o projeto passou por uma **refatoração estrutural completa para o framework Django**. 

**Motivação da mudança:** Garantir maior escalabilidade, segurança nativa e preparar a aplicação para a transição de dados mockados para persistência real em banco de dados utilizando o ecossistema robusto do Django ORM e do painel administrativo nativo.

#### 🧩 Nova Estrutura do Projeto (Padrão Django)
O diretório foi reorganizado seguindo a arquitetura de Apps do Django para manter clareza e facilidade de manutenção:
```bash
projeto-eco-coleta/
│
├── config/                  # Configurações do projeto Django (settings, urls)
│
├── core/                    # App principal da aplicação
│   ├── siteinfos.py         # Mock temporário de dados (classes dos cards/banners)
│   ├── views.py             # Lógica de controle e renderização (Contextos)
│   ├── urls.py              # Rotas específicas do app core
│   └── templates/           # Templates HTML estruturados para o Django DTL
│       ├── base.html
│       ├── index.html
│       ├── como_funciona.html
│       ├── mapa.html
│       ├── contato.html
│       └── materiais.html
│
├── static/                  # Arquivos estáticos globais (CSS, JS, Imagens)
│   ├── css/
│   │   └── style.css
│   └── img/

```

#### 🔄 Separação de Responsabilidades (SoC)

* **`core/views.py`** → Gerencia as requisições, injetando os objetos de dados necessários em um dicionário de contexto direcionado aos templates.
* **`core/siteinfos.py`** → Centraliza as classes estruturais (`Banner`, `Secao`, `CardSecao`, `FooterDivs`) mapeando os dados do ecossistema de forma limpa.
* **Templates (Django Template Language - DTL)** → Responsáveis estritamente pela camada de apresentação, utilizando tags nativas do Django (`{% for %}`, `{% if %}`, `{% url %}`) de forma rígida e performática, eliminando chamadas diretas de funções do Python no HTML.

#### 💻 Tecnologias Utilizadas

* Python 3.12
* Django 6.x (Framework Web Monolítico)
* Django Template Language (DTL)
* HTML5 / CSS3 / FontAwesome Icons

---

### 🚧 Próximos Passos (Roadmap)

O desenvolvimento do EcoColeta está estruturado em fases incrementais, focando na transição de dados controlados para uma aplicação dinâmica real:

####  1. Identidade Visual & Páginas Secundárias (Em Andamento)
- [ ] **CSS Global & Responsividade:** Implementação de estilização completa e design responsivo, garantindo uma interface moderna e fluida em dispositivos móveis e desktop.
- [ ] **Página de Contato:** Estruturação e estilização do formulário de atendimento e suporte ao usuário.
- [ ] **Página do Mapa:** Construção da interface que abrigará o mapa interativo para localização dos pontos de descarte.

####  2. Banco de Dados & Persistência (PostgreSQL)
- [ ] **Migração para Django Models:** Substituição do arquivo estático de configuração (`siteinfos.py`) por modelos nativos do Django ORM, permitindo o gerenciamento de banners e seções via painel administrativo (`/admin`).
- [ ] **Integração com PostgreSQL:** Configuração e migração do banco de dados para ambiente PostgreSQL em substituição ao banco de desenvolvimento.
- [ ] **Modelagem dos Pontos de Coleta:** Criação do modelo `PontoColeta` para armazenamento georreferenciado (Latitude e Longitude), endereços e tipos de materiais recicláveis aceitos.
- [ ] **API de Geolocalização:** Desenvolvimento de uma API interna que consome dados do PostgreSQL e entrega em formato JSON para renderização dinâmica de marcadores no mapa via JavaScript (Leaflet.js / Google Maps).

####  3. Funcionalidades Futuras
- [ ] **Autenticação de Usuários:** Sistema de login, cadastro e perfis utilizando o ecossistema nativo de segurança do Django.
- [ ] **Blog Sustentável:** Espaço dedicado à publicação de artigos, guias de reciclagem e conteúdos educativos sobre sustentabilidade.

---

### 🎯 Boas Práticas Aplicadas

* **Conventional Commits:** Histórico do Git padronizado (`feat:`, `fix:`, `chore:`, `docs:`).
* **DRY (Don't Repeat Yourself):** Reutilização de blocos estruturais de dados globais (como o Footer) injetados via contexto nas Views.
* **Clean Code:** Nomes significativos, funções enxutas e eliminação de código morto/legado do Flask (`app.py`).

---

### 🤖 Como Executar o Projeto Localmente

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/rafaela-barbosa/projeto-eco-coleta.git
   cd projeto-eco-coleta
2. **Crie e Ative o Ambiente Virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # No Windows PowerShell/CMD
3. **Instale as Dependencias:**
   ```bash
   pip install django
4. **Rode as Migrações Iniciais:**
   ```bash
   python manage.py migrate
5. **Execute a Aplicação:**
   ```bash
   python manage.py runserver
O projeto estará acessível em http://127.0.0.1:8000/.

---

### 💬 Reflexão e Aprendizados

A migração de arquitetura do Flask para o Django expandiu drasticamente minha percepção sobre o desenvolvimento web comercial. Lidar com as restrições e o ecossistema do Django exigiu um aprofundamento em ciclos de requisição/resposta, gerenciamento avançado de arquivos estáticos e boas práticas de acoplamento de código.

Se um dia o projeto evoluir além da disciplina, eu gostaria que ele se tornasse uma ferramenta útil de verdade, onde as pessoas pudessem procurar pontos de coleta próximos e até indicar novos locais, ajudando na construção de cidades mais conscientes e sustentáveis. 🌎
