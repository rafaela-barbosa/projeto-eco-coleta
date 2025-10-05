## EcoColeta: Plataforma de Mapeamento de Pontos de Coleta Seletiva
[![Status do Projeto](https://img.shields.io/badge/Status-Em%20Construção-orange.svg)](url-nao-obrigatoria)

Projeto desenvolvido em **Python com o framework Flask** para a disciplina Projeto Integrador do curso de Análise e Desenvolvimento de Sistemas.

O principal objetivo deste projeto é fornecer uma plataforma web informativa e interativa para conectar usuários a pontos de coleta seletiva de resíduos.

---
### ⚙️ Arquitetura e Escolhas Técnicas (Dia 1: Estrutura Base)

O projeto segue um design modular focado na **Separação de Preocupações (SoC)** e utiliza a estrutura de templates do Flask para garantir escalabilidade e manutenção.

#### 1. Separação de Preocupações (SoC)

A lógica do sistema foi dividida em camadas claras:

* **`app.py` (Controlador/View):** Define as rotas e a lógica de aplicação. É responsável por instanciar os objetos de dados e passá-los para os templates.
* **`siteinfos.py` (Modelo/Dados):** Esta camada simula o banco de dados. Contém a definição das classes e as instâncias com o conteúdo do site para a Home Page.

#### 2. Estrutura de Diretórios e Estático

* **`templates/`:** Contém todos os arquivos HTML (templates Jinja2).
* **`static/`:** Contém os ativos públicos, como CSS e imagens.
* **`.gitignore`:** Configurado para ignorar o ambiente virtual e caches do Python/IDEs, garantindo um repositório limpo.

#### 3. Geração de Conteúdo Dinâmico (Escolha Robusta)

* **Técnica Preferida:** Utilização de **`loop for` aninhados** do Jinja2 (`{% for secao in secoes %}` e `{% for card in secao.get_cards() %}`).
* **Justificativa Técnica (Priorizando Robustez):** Esta abordagem foi escolhida em **preferência à injeção de HTML estático** (como o filtro `| safe` do Jinja2).
    * O uso de *loops* mantém a **Separação de Preocupações**, onde o Python (`siteinfos.py`) gerencia *apenas* os dados e o HTML (`index.html`) *apenas* a apresentação.

---
### 🛠️ Próximos Passos (Roadmap de Desenvolvimento)

O projeto está sendo desenvolvido em fases. Os próximos passos incluem:

1.  **Fase Atual (Estrutura Concluída):** Finalização da documentação técnica e da arquitetura Flask/Jinja2.
2.  **Estilização (CSS):** Implementação completa do design (Banner, Navbar, Cards e Footer), focando na experiência visual e responsividade.
3.  **Páginas Secundárias:** Criação das interfaces para as páginas de **Mapa** e **Contato**.
4.  **Funcionalidade Principal:** Implementação da biblioteca de mapas e integração final com dados (simulados ou reais).

---
### 🤖 Como Executar o Projeto Localmente

1.  **Clone o Repositório:**
    ```bash
    git clone SUA_URL_DO_GITHUB
    cd projeto-eco-coleta
    ```
2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate   # No Windows PowerShell/CMD
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install Flask
    ```
4.  **Execute a Aplicação:**
    ```bash
    flask run
    ```

O projeto estará acessível em `http://127.0.0.1:5000/`.
