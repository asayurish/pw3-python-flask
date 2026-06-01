#importando o render_template
# motor para renderizar as páginas
from flask import render_template, request, redirect, url_for, flash
#importando o markup safe
from markupsafe import Markup
#importando o model game e o  sqlalchemy
from models.database import Game, Console, db, Usuario 
#importando werkzeug
from werkzeug.security import generate_password_hash

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
        
    # rota de estoque de jogos
    @app.route("/estoque-jogos", methods=['GET', 'POST'])
    # criando parametro na rota (id) para excluir um registro
    @app.route("/estoque-jogo/delete/<int:id>")
    def estoque_jogos(id=None):
        #verificando se esta sendo enviado o parametro id para a rota
        if id:
            game = Game.query.get(id) #select no banco
            #deleta o jogo no banco
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        #verificando se a requisição é do tipo POST
        if request.method == 'POST':
            # coletando os dados preenchidos no formulario
            dados_form = request.form.to_dict()
            # enviando os dados para o MODEL
            newGame = Game(
                dados_form['titulo'],
                dados_form['ano'],
                dados_form['categoria'],
                dados_form['plataforma'],
                dados_form['preco'],
                dados_form['quantidade']
            )
            #metodo do SQLAlchemy para gravar os dados no banco
            db.session.add(newGame)
            #confirmando a operação no banco
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        #selecionando todos os jogos do banco
        # SELECT * FROM GAMES
        games = Game.query.all()
        return render_template('estoque-jogos.html', games=games)
    
    @app.route('/editar-jogos/<int:id>', methods=['GET', 'POST'])
    def editar_jogos(id):
        #buscando o jogo no banco
        game=Game.query.get(id)
        #verificando se a requisição é POST
        if request.method =='POST':
            dados_form = request.form.to_dict()
            game.titulo = dados_form['titulo']
            game.ano = dados_form['ano']
            game.categoria = dados_form['categoria']
            game.plataforma = dados_form['plataforma']
            game.preco = dados_form['preco']
            game.quantidade = dados_form['quantidade']
            #confirmando as alterações no banco
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        return render_template('editar-jogos.html', game=game)
    
    
    @app.route('/estoque_consoles', methods=['GET', 'POST'])
    def estoque_consoles():

        if request.method == 'POST':

            dados_form = request.form.to_dict()

            newConsole = Console(
                nome=dados_form['nome'],
                fabricante=dados_form['fabricante'],
                ano=dados_form['ano'],
                preco=dados_form['preco'],
                quantidade=dados_form['quantidade']
            )

            db.session.add(newConsole)
            db.session.commit()

            return redirect(url_for('estoque_consoles'))

        consoles = Console.query.all()

        return render_template(
            'estoque-consoles.html',
            consoles=consoles
        )

    @app.route('/estoque_consoles/delete/<int:id>')
    def deletar_console(id):

        console = Console.query.get(id)

        if console:
            db.session.delete(console)
            db.session.commit()

        return redirect(url_for('estoque_consoles'))
    
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        #verificando se o metodo é POST
        if request.method == 'POST':
            #coletando os dados do formulário
            email = request.form['email']
            senha = request.form['senha']
            # verificando se o usuário já existe
            #buscando o usuario pelo e-mail
            usuario = Usuario.query.filter_by(email=email).first()
            #veruficando se o usuario tem valor
            if usuario:
                msg = Markup("Usuário já cadastrado. Faça o <a href='/login'>login</a>")
                flash(msg, 'danger')
                return redirect(url_for('cadastro'))
            
            #gerando o hash da senha (criptografia)
            senha_criptografada = generate_password_hash(senha, method='scrypt')
            #enviando os dados para o model
            novo_usuario = Usuario(email=email, senha=senha_criptografada)
            #cadastrando novo banco
            db.session.add(novo_usuario)
            db.session.commit()
            #gerando a mensagem de sucesso
            msgCad = Markup("Cadastro realizado com sucesso! Faça o <a href='/login'>login</a>")
            flash(msgCad, 'success')
            return redirect(url_for('cadastro'))
        return render_template('cadastro.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return render_template('login.html')
    
    