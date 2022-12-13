import string


def caesar_cipher_encryptor(input_string, number):
    alphabet = list(string.ascii_lowercase)
    output_string = ""
    for i in range(len(input_string)):
        index_in_alphabet = found_index(input_string[i])
        output_string = output_string + alphabet[(index_in_alphabet + number) % len(alphabet)]
    return output_string


def found_index(char):
    flag = 0
    alphabet = list(string.ascii_lowercase)
    for item in alphabet:
        if item == char:
            break
        else:
            flag = flag + 1
    return flag


print(caesar_cipher_encryptor("abc", 1))
