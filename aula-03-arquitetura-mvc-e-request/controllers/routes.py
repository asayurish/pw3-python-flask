#importando o render_template
# motor para renderizar as páginas
from flask import render_template

#criando a função para receber o flask (app)
def init_app(app):
    # a partir daqui virão as rotas
    @app.route('/')
    # o @ é pra especificar acho

    # def serve para criar funções no Python
    def home():
        return render_template('index.html')

    #criando a rota principal do site
    @app.route('/games')
    # o @ é pra especificar acho

    # def serve para criar funções no Python
    def games():
        #Criando variáveis para passar as informações de um jogo
        titulo = "Silk Song"
        ano = 2025
        categoria = "Metroidvania"
        
        #criando um objeto python para representar as propriedades de um jogo
        game = {
            "Título" : "Minecraft",
            "Ano" : 2012,
            "Categoria" : "Sandbox"
        }
        
        # Criando vetor (lista)
        jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antonio']
        
        return render_template('games.html',
                            # Enviando as variáveis para a página HTML
                            titulo=titulo,
                            ano=ano,
                            categoria=categoria,
                            jogadores=jogadores,
                            game=game)


    @app.route('/consoles')
    # o @ é pra especificar acho

    # def serve para criar funções no Python
    def consoles():
        consoles = ['PlayStation', 'Xbox Series X', 'Xbox Series S', 'Nintendo Switch', 'Nintendo Switch 2']
        
        return render_template('consoles.html',
                            consoles=consoles)
