import string

def generate_matrix(keyword):
    matrix = [[' ' for _ in range(5)] for _ in range(5)]
    keyword = keyword.upper()
    keyword_chars = []
    seen = set()
    
    for char in keyword:
        if char not in seen:
            keyword_chars.append(char)
            seen.add(char)
    
    if len(keyword_chars) > 25:
        raise ValueError("Keyword no longer than 25 chars")
    
    random_chars = [char for char in string.ascii_uppercase if char not in keyword_chars and char != 'J']
    random_chars.sort()  

    index = 0
    for i in range(5):
        for j in range(5):
            if index < len(keyword_chars):
                matrix[i][j] = keyword_chars[index]
                index += 1
            else:
                matrix[i][j] = random_chars.pop(0)  

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def prepare_text(text):
    text = text.upper().replace(' ', '')
    text = text.replace('J', 'I')
    result = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            result.append(text[i:i + 2])
            i += 2
        else:
            result.append(text[i] + 'X')
            i += 1
    return result

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)

def encrypt(matrix, text):
    result = []
    for pair in text:
        pos1 = find_position(matrix, pair[0])
        pos2 = find_position(matrix, pair[1])
        if pos1[0] == pos2[0]:  
            result.append(matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5])
        elif pos1[1] == pos2[1]:  
            result.append(matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]])
        else:  
            result.append(matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]])
    return ' '.join(result)

def main():
    text = input("Enter the plain text: ")
    keyword = input("Enter the keyword: ")
    matrix = generate_matrix(keyword)
    print("\nMatrix:")
    print_matrix(matrix)
    prepared_text = prepare_text(text)
    print("\nPrepared text:", ' '.join(prepared_text))
    encrypted_text = encrypt(matrix, prepared_text)
    print("\nEncrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
