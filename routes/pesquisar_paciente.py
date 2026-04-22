from flask import Flask, render_template, request
import mysql.connector

app = Flask( __name__)

# Configuração do banco
db_config = {
    'host': 'localhost',
    'user': 'MaikonWatterson',
    'password': 'MySQL331992saveus$',
    'database': 'Cadastro_Pesquisa'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# ROTA 1: Abre a tela do form - GET
def abrir_tela_pesquisa():
    # Renderiza o 'form' de pesquisa vazio
    return render_template("pesquisa_paciente.html")

# ROTA 2: Processa a busca e mostra resultado- POST
def processar_pesquisa():
    #Renderiza o form e retorna os resultados
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    
    conexao = get_db_connection()
    cursor = conexao.cursor(dictionary=True)
    
    sql = """
        SELECT
            pac_nome,
            pac_sobrenome,
            pac_cpf,
            pac_data_nasc,
            pac_telefone,
            pac_email,
            data_cadastro,
            pac_endereco,
            pac_numero,
            pac_cep,
            pac_bairro,
            pac_cidade,
            pac_estado
            FROM tb_paciente
            WHERE 1=1
         """
    params = []
   
    if nome:
       sql += " AND pac_nome LIKE %s"
       params.append(f"%{nome}%")
        
    if cpf:
       sql += "AND pac_cpf = %s"
       params.append(f"%{cpf}%")
    
    resultados = []
    if params:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        
    cursor.close()
    conexao.close()
    
    return render_template(
        "paciente_resultado_pesquisa.html",
        pacientes=resultados
)
