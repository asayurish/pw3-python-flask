# comentário em Python
# importando o Flask na aplicação
from flask import Flask, render_template 
# render_template renderiza as páginas html
from controllers import routes
# carregando o Flask em uma variável
# declarando variável no python
app = Flask(__name__, template_folder='views')

#__name__ é uma variável de ambiente do Python que tem o nome do módulo atual

#Eviando a variável APP (FLASK) para as rotas
routes.init_app(app)

# iniciando o servidor web (tipo apache, mas no python faz aqui mesmo)
if __name__ == '__main__':
    app.run(debug=True)
    # verificando se app for o arquivo principal, ele inicia o servidor
    # debug=True ligando modo de depuração, reinicia automático, só não funciona quando tem erro no código, aí tem que rodar manualmente
    
# main é quando se está testando se é arquivo principal, se for, dá run, que inicia o servidor.