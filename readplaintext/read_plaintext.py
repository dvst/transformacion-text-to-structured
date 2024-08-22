def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    expected_lines = lines[14:46] + lines[57:101]
    content = ''.join(expected_lines)
    return content

if __name__ == "__main__":
    file_path = 'example.txt'  # Replace with your file path
    content = read_text_file(file_path)
    print(content)