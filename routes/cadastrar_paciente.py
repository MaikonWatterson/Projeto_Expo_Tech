from flask import Flask, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'MaikonWatterson',
    'password': 'MySQL331992saveus$',
    'database': 'Cadastro_Pesquisa'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def cadastrar_paciente():
    print("Rota /cadastrar_paciente chamada")
    print(request.form)
    try:
        pac_nome = request.form['pac_nome']
        pac_sobrenome = request.form['pac_sobrenome']
        pac_cpf = request.form['pac_cpf']
        pac_data_nasc = request.form['pac_data_nasc']
        pac_telefone = request.form['pac_telefone']
        pac_email = request.form['pac_email']
        pac_endereco = request.form['pac_endereco']
        pac_numero = request.form['pac_numero']
        pac_cep = request.form['pac_cep']
        pac_bairro = request.form['pac_bairro']
        pac_cidade = request.form['pac_cidade']
        pac_estado = request.form['pac_estado']

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO tb_paciente (pac_nome, pac_sobrenome, pac_cpf, pac_data_nasc, pac_telefone, pac_email, pac_endereco, pac_numero, pac_cep, pac_bairro, pac_cidade, pac_estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
              """
        valores = (pac_nome, pac_sobrenome, pac_cpf, pac_data_nasc, pac_telefone, pac_email, pac_endereco, pac_numero, pac_cep, pac_bairro, pac_cidade, pac_estado)
        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    except Error as e:
        print(f"Erro MySQL: {e}")
        return "Erro no banco de dados", 500
    except Exception as e:
        print(f"Erro geral: {e}")
        return "Erro interno", 500