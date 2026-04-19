from flask import request, redirect, url_for
import mysql.connector
from mysql.connector import Error

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

def cadastrar_medico():
    print("Rota /cadastrar_medico chamada")
    print(request.form)
    try:
        med_nome = request.form['med_nome']
        med_sobrenome = request.form['med_sobrenome']
        crm = request.form['crm']
        med_data_nasc = request.form['med_data_nasc']
        med_telefone = request.form['med_telefone']
        med_email = request.form['med_email']
        data_admissao = request.form['data_admissao']
        data_demissao = request.form['data_demissao']
        med_endereco = request.form['med_endereco']
        med_numero = request.form['med_numero']
        med_cep = request.form['med_cep']
        med_bairro = request.form['med_bairro']
        med_cidade = request.form['med_cidade']
        med_estado = request.form['med_estado']

        conn = get_db_connection()
        if not conn:
            return "Erro de conexão com o banco", 500

        cursor = conn.cursor()
        sql = """
            INSERT INTO Medicos 
            (med_nome, med_sobrenome, crm, med_data_nasc, med_telefone, med_email, 
             data_admissao, data_demissao, med_endereco, med_numero, med_cep, med_bairro, med_cidade, med_estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            med_nome, med_sobrenome, crm, med_data_nasc,
            med_telefone, med_email, data_admissao, data_demissao,
            med_endereco, med_numero, med_cep, med_bairro, med_cidade, med_estado
        )
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