from flask import Flask, render_template
import routes.cadastrar_paciente as pacientes
import routes.cadastrar_medico as medicos
import routes.pesquisar_paciente as pesquisa_pac

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paciente_cadastro')
def pagina_paciente():
    return render_template('paciente_cadastro.html')

@app.route('/medico_cadastro')
def pagina_medico():
    return render_template('medico_cadastro.html')

@app.route('/cadastrar_paciente', methods=['POST'])
def cadastrar_paciente_route():
    return pacientes.cadastrar_paciente()

@app.route('/cadastrar_medico', methods=['POST'])
def cadastrar_medico_route():
    return medicos.cadastrar_medico()

@app.route("/pesquisar_paciente")
def pesquisar_paciente_route():
    return pesquisa_pac.abrir_tela_pesquisa()

@app.route("/pesquisar_paciente", methods=['POST'])
def processar_pesquisa_route():
    return pesquisa_pac.processar_pesquisa()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)