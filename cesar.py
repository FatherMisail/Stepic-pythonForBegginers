RU_MOD = ord('Я') - ord('А') + 1
EN_MOD = ord('Z') - ord('A') + 1


def get_mod(lang):
    if lang == 'ru':
        return RU_MOD
    elif lang == 'en':
        return EN_MOD


def crypt(lang, k, msg):
    cipher = []

    n = get_mod(lang)
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


def string_crack(lang, msg):
    n = get_mod(lang)
    for i in range(1, n):
        print(f'Ключ <{i}>: ', crypt(lang, i, msg))


def main():
    while True:
        print('Введите <0> для зашифровки по ключу')
        print('Введите <1> для дешифровки по ключу')
        print('Введите <2> для дешифровки перебором: ', end='')
        ct_dct = input()
        if '0' == ct_dct or ct_dct == '1' or ct_dct == '2':
            break
    ct_dct = int(ct_dct)

    while True:
        print('Введите <ru> для обработки символов русского языка или <en> для английского.')
        print('Иные символы затронуты не будут: ', end='')
        lang = input()
        if 'ru' == lang or lang == 'en':
            break

    msg = ''
    while not msg:
        print('Введите сообщение: ', end='')
        msg = input()

    if ct_dct == 2:
        string_crack(lang, msg)
        return

    while True:
        print('Введите целое неотрицательное число-ключ: ', end='')
        k = input()
        if k.isdigit():
            break
    k = int(k)

    if ct_dct == 0:
        res = crypt(lang, k, msg)
    elif ct_dct == 1:
        res = decrypt(lang, k, msg)

    print(f'Результат: {res}')


main()
