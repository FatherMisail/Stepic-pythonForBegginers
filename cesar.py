def crypt(lang, k, msg):
    cipher = []

    n = 0
    if lang == 'ru':
        n = ord('Я') - ord('А') + 1
    elif lang == 'en':
        n = ord('Z') - ord('A') + 1

    for c in msg:
        base = -1
        if lang == 'ru':
            if 'а' <= c <= 'я':
                base = ord('а')
            elif 'А' <= c <= 'Я':
                base = ord('А')
        elif lang == 'en':
            if 'a' <= c <= 'z':
                base = ord('a')
            elif 'A' <= c <= 'Z':
                base = ord('A')

        if base == -1:
            cipher.append(c)
        else:
            x = ord(c) - base
            y = (x + k) % n
            cipher.append(chr(y + base))

    return ''.join(cipher)

def decrypt(lang, k, msg):
    return crypt(lang, -k, msg)

def main():
    while True:
        print('Введите <0> для шифровки')
        print('Введите <1> для дешифровки: ', end='')
        ct_dct = input()
        if '0' == ct_dct or ct_dct == '1':
            break
    ct_dct = int(ct_dct)

    while True:
        print('Введите <ru> для шифрования символов русского языка текста или <en> для символов английского языка.')
        print('Иные символы шифроваться не будут: ', end='')
        lang = input()
        if 'ru' == lang or lang == 'en':
            break


    while True:
        print('Введите целое неотрицательное число-ключ: ', end='')
        k = input()
        if k.isdigit():
            break
    k = int(k)

    msg = ''
    while not msg:
        print('Введите сообщение: ', end='')
        msg = input()

    if ct_dct == 0:
        res = crypt(lang, k, msg)
    elif ct_dct == 1:
        res = decrypt(lang, k, msg)

    print(f'Результат: {res}')

main()
