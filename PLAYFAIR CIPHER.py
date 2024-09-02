def generate_matrix(keyword):
    # Remove duplicates and create the matrix
    keyword = "".join(dict.fromkeys(keyword.replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    
    for char in keyword + alphabet:
        if char not in matrix:
            matrix.append(char)
    
    # Create 5x5 matrix
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def prepare_message(message):
    # Replace J with I and make pairs
    message = message.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0

    while i < len(message):
        a = message[i]
        b = message[i + 1] if (i + 1) < len(message) else "X"
        
        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2
            
    if len(pairs[-1]) == 1:
        pairs[-1] += "X"
    return pairs
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None
def encrypt_decrypt_pair(pair, matrix, encrypt=True):
    a, b = pair
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    if row_a == row_b:
        col_a = (col_a + 1) % 5 if encrypt else (col_a - 1) % 5
        col_b = (col_b + 1) % 5 if encrypt else (col_b - 1) % 5
    elif col_a == col_b: 
        row_a = (row_a + 1) % 5 if encrypt else (row_a - 1) % 5
        row_b = (row_b + 1) % 5 if encrypt else (row_b - 1) % 5
    else:  
        col_a, col_b = col_b, col_a
    return matrix[row_a][col_a] + matrix[row_b][col_b]
def playfair_cipher(message, keyword, encrypt=True):
    matrix = generate_matrix(keyword)
    pairs = prepare_message(message)
    result = ""
    for pair in pairs:
        result += encrypt_decrypt_pair(pair, matrix, encrypt)
    return result
keyword = input("Enter keyword: ").upper().replace("J", "I")
message = input("Enter message: ")
encrypted_message = playfair_cipher(message, keyword, encrypt=True)
print("Encrypted Message:", encrypted_message)
decrypted_message = playfair_cipher(encrypted_message, keyword, encrypt=False)
print("Decrypted Message:", decrypted_message)



-------------------------------------------------------------------------------------------------------------------```````````>>>

