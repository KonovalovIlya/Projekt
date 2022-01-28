def caesar(string, step, alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    out = []
    for i in list(string):
        if i in alphabet:
            i = alphabet[alphabet.index(i) + step]
            out.append(i)
        else:
            out.append(i)
    out = ''.join(out)
    return out


file_text = open('text.txt', 'w')
file_text.write('Hello\nHello\nHello\nHello\nHello\n')
file_text.close()

cipher_text = open('cipher_text.txt', 'w')
cipher_text.close()
file_text = open('text.txt', 'r')
step = 0
for string in file_text:
    step += 1
    ciphered = caesar(string, step)
    cipher_text = open('cipher_text.txt', 'a')
    cipher_text.write(ciphered)
    cipher_text.close()
