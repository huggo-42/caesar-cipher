from random import randint

message = str(input('Enter a message: '))

def encrypt(message: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_len = len(alphabet) - 1

    encrypted_message = ''

    key = randint(0, 25)

    for char in message:
        if char == ' ':
            continue

        idx = 0

        if (alphabet.index(char) + key) > alphabet_len:
            idx = alphabet.index(char) + key - alphabet_len
        else:
            idx = alphabet.index(char) + key + 1

        encrypted_message += alphabet[idx - 1]

    return encrypted_message

print('encrypted_message: ', encrypt(message))

