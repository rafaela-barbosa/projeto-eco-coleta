## 🌱 EcoColeta: Plataforma de Mapeamento de Pontos de Coleta Seletiva
![Status do Projeto](https://img.shields.io/badge/Status-Em%20Construção-orange.svg)

O EcoColeta é uma plataforma web desenvolvida em Python com o framework Flask como parte do Projeto Integrador do curso de Análise e Desenvolvimento de Sistemas.
A ideia surgiu a partir de um interesse pessoal em criar algo voltado à sustentabilidade, conectando tecnologia e responsabilidade ambiental.

O objetivo do projeto é centralizar informações sobre coleta seletiva e permitir que os usuários encontrem pontos de coleta próximos por meio de um mapa interativo. Além disso, a plataforma também fornece conteúdos educativos, como um guia de reciclagem, benefícios da coleta seletiva e materiais aceitos.

Inspirado em sites de prefeituras — simples, informativos e práticos — o EcoColeta busca ser um ambiente acessível, moderno e funcional, unindo informação e ação.

---
### ⚙️ Arquitetura e Escolhas Técnicas
O desenvolvimento do projeto foi planejado com foco em organização, legibilidade e escalabilidade, aplicando boas práticas de arquitetura web e Separação de Responsabilidades (SoC).


#### 🧩 Estrutura do Projeto
O diretório foi organizado desde o início para manter clareza e facilidade de manutenção:
```bash
eco-coleta/
│
├── app.py                   # Controlador principal (rotas e renderização)
├── siteinfos.py             # Simulação do banco de dados (mock de dados)
│
├── /templates               # Templates HTML (Jinja2)
│   ├── /partials            # Componentes reutilizáveis (navbar, footer)
│   ├── base.html
│   ├── index.html
│   ├── como-funciona.html
│   ├── mapa.html
│   ├── contato.html
│   └── materiais.html
│
├── /static                  # Arquivos estáticos
│   ├── style.css
│   └── /img
│
└── .gitignore
```

#### 🔄 Separação de Responsabilidades

* `app.py` → Define as rotas e conecta os dados aos templates.

* `siteinfos.py` → Armazena classes e dados simulados.

* `Templates (HTML)` → Responsáveis apenas pela estrutura e apresentação, utilizando loops aninhados do Jinja2 ({% for secao in secoes %} / {% for card in secao.get_cards() %}) para gerar o conteúdo dinamicamente.

Essa abordagem evita a injeção de HTML estático e garante um código mais limpo, modular e de fácil manutenção.


#### 💻 Tecnologias Utilizadas

* Python 3.12
* Flask (microframework web)
* Jinja2 (templates dinâmicos)
* HTML5 / CSS3 (estrutura e estilo)

---
### 🧠 Processo de Desenvolvimento

O projeto foi desenvolvido individualmente, começando com a identificação das funcionalidades essenciais (home page, páginas informativas, mapa e filtros de pesquisa).
A partir disso, foi criado um design de interface e em seguida, a estrutura de diretórios e templates base do Flask, com partials reutilizáveis (navbar, footer) e herança de templates (base.html).


#### Desafios e Aprendizados
O maior desafio até agora foi aprender e aplicar loops aninhados no Jinja2 para gerar conteúdo dinâmico sem quebrar a separação entre dados e interface. Esse aprendizado veio de muita leitura de documentação e experimentação prática, o que também ajudou a compreender melhor conceitos de arquitetura web.

---
### 🚧 Próximos Passos (Roadmap)

O projeto está sendo desenvolvido em fases. Os próximos passos incluem:

1.  Finalizar a estrutura base e a documentação técnica.
2.  Aplicar o CSS completo, garantindo uma interface moderna e responsiva.
3.  Desenvolver as páginas secundárias (Mapa e Contato).
4.  Implementar o mapa interativo, com dados simulados e posterior integração com banco de dados (MySQL).
5.  Futuramente: Incluir um blog sustentável e funcionalidades de cadastro de usuários.

---
### 🎯 Boas Práticas Aplicadas

* Código limpo e organizado.
* Nomes claros para funções e variáveis.
* Separação entre lógica, dados e apresentação (SoC).
* Estrutura pensada para evolução futura do projeto.

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


---
### 💬 Reflexão e Aprendizados

O EcoColeta me ensinou que uma boa arquitetura é a base de um projeto sólido.
Estou aprendendo cada vez mais sobre Flask, Jinja2 e versionamento com Git/GitHub, além de compreender melhor como o planejamento e a estruturação inicial tornam o desenvolvimento mais fluido e organizado.

Se um dia o projeto evoluir além da disciplina, eu gostaria que ele se tornasse uma ferramenta útil de verdade, onde as pessoas pudessem procurar pontos de coleta próximos e até indicar novos locais, ajudando na construção de cidades mais conscientes e sustentáveis. 🌎

