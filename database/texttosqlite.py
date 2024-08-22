import sqlite3

def write_to_sqlite(file_content):
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        descripcion TEXT,
        sucursal TEXT,
        dcto TEXT,
        valor TEXT,
        saldo TEXT
    )
''')
    
    # FECHA	DESCRIPCIÓN	SUCURSAL	DCTO.	VALOR	SALDO
    # lines = file_content.split("\n")
    for line in file_content.split("\n"):
        contenido = line[:32]
        split_columns = contenido.split("\t")
        print(split_columns[0]) # fecha
        print(split_columns[1]) # descripcion
        print(split_columns[2]) # sucursal
        print(split_columns[3]) # dcto
        print(split_columns[4]) # valor
        print(split_columns[5]) # saldo
        c.execute('''
            INSERT INTO transactions (fecha, descripcion, sucursal, dcto, valor, saldo)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (split_columns[0], split_columns[1], split_columns[2], split_columns[3], split_columns[4], split_columns[5]))

    conn.commit()
    conn.close()