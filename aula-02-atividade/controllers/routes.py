from flask import render_template, request, url_for

def init_app(app):

    # simulando banco
    listaEpisodios = [{
        "nome": "O Poder do One For All",
        "temporada": "Temporada 1",
        "duracao": "24",
        "personagens": "Midoriya, All Might",
        "descricao": "Primeiro contato com o poder"
    }]

    @app.route('/')
    def home():
        return render_template('index.html')

    # 🔥 ROTA DO CADASTRO
    @app.route('/cadhero', methods=['GET', 'POST'])
    def cadhero():

        if request.method == 'POST':
            listaEpisodios.append({
                'nome': request.form.get('nome'),
                'temporada': request.form.get('temporada'),
                'duracao': request.form.get('duracao'),
                'personagens': request.form.get('personagens'),
                'descricao': request.form.get('descricao')
            })

        return render_template('cadhero.html',
                               listaEpisodios=listaEpisodios)

    @app.route('/seasondois')
    def seasondois():
        return render_template('seasondois.html')

    @app.route('/seasonoito')
    def seasonoito():
        return render_template('seasonoito.html')