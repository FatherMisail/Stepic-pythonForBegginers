def crypt(lang, k, msg):
    cipher = []

    for c in msg:
        base = ''
        if lang == 'ru':
            n = ord('Я') - ord('А') + 1
            if ord('а') <= ord(c) <= ord('я'):
                base = ord('а')
            elif ord('А') <= ord(c) <= ord('Я'):
                base = ord('А')
        elif lang == 'en':
            n = ord('Z') - ord('A') + 1
            if ord('a') <= ord(c) <= ord('z'):
                base = ord('a')
            elif ord('A') <= ord(c) <= ord('Z'):
                base = ord('A')

        if base != '':
            x = ord(c) - base
            y = (x + k) % n
            cipher.append(chr(y + base))
        else:
            cipher.append(c)

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

    lang = ''
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
        msg = input().strip()

    res = ''
    if ct_dct == 0:
        res = crypt(lang, int(k), msg)
    elif ct_dct == 1:
        res = decrypt(lang, int(k), msg)

    print(f'Результат: {res}')

main()
