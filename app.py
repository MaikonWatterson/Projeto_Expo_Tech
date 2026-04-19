from flask import Flask, render_template, request, redirect, url_for

import routes.pacientes as pacientes
import routes.medicos as medicos

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cadastro_paciente")
def cadastro_paciente():
    return render_template("paciente_cadastro.html")


@app.route("/cadastro_medico")
def cadastro_medico():
    return render_template("medico_cadastro.html")

@app.route("/cadastrar_paciente", methods=["POST"])
def cadastrar_paciente_route():
    return pacientes.cadastrar_paciente()

@app.route("/cadastrar_medico", methods=["POST"])
def cadastrar_medico_route():
    return medicos.cadastrar_medico()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)