#importando o render_template
# motor para renderizar as páginas
from flask import render_template, request, redirect, url_for

#criando a função para receber o flask (app)
def init_app(app):
    
    #simulando um banco de dados
    
    listaGames = [{"titulo" : "CS-GO", "ano" : 2012, "categoria" : "FPS ONLINE"}]
    
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

#ROTA DE CADASTRO DE JOGOS
    # @app.route('/cadgames')
    #     def cadgames():
    #         return render_template('cadgames.html')
    
    @app.route('/cadgames', methods=['GET', 'POST'])
    # o @ é pra especificar acho

    # def serve para criar funções no Python
    def cadgames():
        #verificando se o método da requisição é POST
        if request.method == 'POST':
            #recebendo os dados do formulário e gravando na lista
            listaGames.append({'titulo' : request.form.get('titulo'), 'ano' : request.form.get('ano'), 'categoria' : request.form.get('categoria')})
            
            
        return render_template('cadgames.html',
                            listaGames = listaGames)