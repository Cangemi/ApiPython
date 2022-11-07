import sqlite3

try:
    conn = sqlite3.connect('database/data.db')
    conn.execute('DROP TABLE IF EXISTS tb_cliente')
    conn.execute('DROP TABLE IF EXISTS tb_device')
    conn.execute('''
        CREATE TABLE tb_cliente (
            id INTEGER PRIMARY KEY NOT NULL,
            id_device INTEGER,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            telefone1 TEXT NOT NULL,
            telefone2 TEXT NOT NULL,
            FOREING KEY (id_device) REFERENCES tb_device(id)
        );

        CREATE TABLE tb_device (
            id INTEGER PRIMARY KEY NOT NULL,
            mac  TEXT NOT NULL,
            nome TEXT NOT NULL,
            ssid TEXT NOT NULL,
            senha TEXT NOT NULL,
            lock  INTEGER
        );
    ''')
    
    conn.commit()
    print("Operacao realizada com sucesso!")
except:
    print("ERRO")
finally:
    conn.close()