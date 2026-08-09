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
│       └── partials/        # Componentes reutilizáveis
│           └── footer.html     
│           └── navbar.html
│       ├── base.html
│       ├── index.html
│       ├── como_funciona.html
│       ├── mapa.html
│       ├── contato.html
│       └── materiais.

│
├── static/                  # Arquivos estáticos globais (CSS, JS, Imagens)
│   ├── css/
│   │   └── style.css
│   └── img/   
│   └── js/
│   │   └── mapa.js

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
- [ X ] **Página de Contato:** Estruturação do formulário de atendimento e suporte ao usuário.
- [ X ] **Página do Mapa:** Construção da interface que abrigará o mapa interativo para localização dos pontos de descarte.
- [ ] **CSS Global & Responsividade:** Implementação de estilização e design responsivo, garantindo uma interface moderna e fluida em dispositivos móveis e desktop.

####  2. Banco de Dados & Persistência
- [ ] **Migração para Django Models:** Substituição do arquivo estático (`siteinfos.py`) por modelos nativos do Django ORM para gestão no `/admin`.
- [ ] **Modelagem dos Pontos de Coleta:** Criação do modelo `PontoColeta` para armazenamento georreferenciado (latitude, longitude, endereço e materiais aceitos).
- [ ] **Migrations & Django Admin:** Execução das migrações (`makemigrations`/`migrate`) e registro dos modelos no `admin.py`.

####  3. Integração do Mapa Interativo (JavaScript + API)
- [ ] **Endpoint JSON:** Criação de view interna consultando `PontoColeta.objects.all()` para entregar dados em formato JSON.
- [ ] **Consumo via JS (Leaflet.js):** Implementação do script `static/js/mapa.js` com `fetch()` para plotagem dinâmica dos marcadores.

####  4. Ambiente de Produção & PostgreSQL
- [ ] **Integração com PostgreSQL:** Configuração do driver e migração do banco SQLite para PostgreSQL.
- [ ] **Ajustes para Deploy:** Configuração das variáveis de ambiente em `settings.py` e entrega de arquivos estáticos.

---

### 🎯 Boas Práticas Aplicadas

* **Conventional Commits:** Histórico do Git padronizado (`feat:`, `fix:`, `chore:`, `docs:`).
* **DRY (Don't Repeat Yourself):** Reutilização de blocos estruturais de dados globais (como o Footer) injetados via contexto nas Views.
* **Clean Code:** Nomes significativos, funções enxutas e eliminação de código morto/legado do Flask (`app.py`).
* **Acessibilidade (A11y) & HTML Semântico:** Estruturação com tags semânticas (`<ol>`, `<li>`), atributos de acessibilidade (`aria-label`) e rótulos vinculados explicitamente a cada campo (`<label for="...">`).

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
    source venv/bin/activate # No Linux / MacOS
3. **Instale as Dependencias:**
   ```bash
   pip install -r requirements.txt
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
