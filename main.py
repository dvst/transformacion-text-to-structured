from readplaintext.read_plaintext import read_text_file
from database.texttosqlite import write_to_sqlite

# NICE TO HAVE
# - hacer uso de argparse para recibir el path del archivo como argumento

if __name__ == "__main__":
    file_path = "extracto_202406_cuenta.txt"
    content = read_text_file(file_path)
    write_to_sqlite(content)

    print(content)
