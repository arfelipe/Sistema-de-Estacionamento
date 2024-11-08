import sqlite3

class Banco:
    def create_table_placas(self):
        conexao = sqlite3.connect('estacionamento.db')
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS placas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa TEXT NOT NULL,
                entrada DATETIME DEFAULT CURRENT_TIMESTAMP,
                saida DATETIME DEFAULT NULL
            )
        ''')
        conexao.commit()
        conexao.close()

    def create_table_vagas(self):
        conexao = sqlite3.connect('estacionamento.db')
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vagas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ocupada BOOLEAN DEFAULT 0
            )
        ''')
        conexao.commit()
        conexao.close()

    def add_col_saida(self):
        conexao = sqlite3.connect('estacionamento.db')
        cursor = conexao.cursor()
        cursor.execute("ALTER TABLE placas ADD COLUMN saida DATETIME")
        conexao.commit()
        conexao.close()

    def create_table_planos(self):
        conexao = sqlite3.connect('estacionamento.db')
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS planos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                preco FLOAT
            )
        ''')
        conexao.commit()
        conexao.close()
