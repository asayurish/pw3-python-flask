# comentário em Python
# importando o Flask na aplicação
from flask import Flask, render_template 
# render_template renderiza as páginas html

# carregando o Flask em uma variável
# declarando variável no python
app = Flask(__name__, template_folder='views')

#__name__ é uma variável de ambiente do Python que tem o nome do módulo atual

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
    
    # Criando vetor (lista)
    jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antonio']
    
    return render_template('games.html',
                           # Enviando as variáveis para a página HTML
                           titulo=titulo,
                           ano=ano,
                           categoria=categoria,
                           jogadores=jogadores)


@app.route('/consoles')
# o @ é pra especificar acho

# def serve para criar funções no Python
def consoles():
    consoles = ['PlayStation', 'Xbox Series X', 'Xbox Series S', 'Nintendo Switch', 'Nintendo Switch 2']
    
    return render_template('consoles.html',
                           consoles=consoles)


# iniciando o servidor web (tipo apache, mas no python faz aqui mesmo)
if __name__ == '__main__':
    app.run(debug=True)
    # verificando se app for o arquivo principal, ele inicia o servidor
    # debug=True ligando modo de depuração, reinicia automático, só não funciona quando tem erro no código, aí tem que rodar manualmente
    
# main é quando se está testando se é arquivo principal, se for, dá run, que inicia o servidor.