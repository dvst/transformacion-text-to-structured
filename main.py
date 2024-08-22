from readplaintext.read_plaintext import read_text_file

if __name__ == "__main__":
    file_path = "extracto_202406_cuenta.txt"
    content = read_text_file(file_path)
    print(content)