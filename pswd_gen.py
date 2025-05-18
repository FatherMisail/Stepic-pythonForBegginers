import random, math


def is_nat(n):
    return n.isdigit() and int(n) >= 0


def generate_password(length, chars):
    pswd = []
    new_pswd_len = length + math.floor(length ** (1 / 3) * random.random() * 3)
    al = []
    al.extend(chars)
    random.shuffle(al)

    for _ in range(new_pswd_len):
        pswd.append(random.choice(al))
    random.shuffle(pswd)

    return ''.join(pswd)


def generate_passwords(pswd_cnt, pswd_len, chars):
    pswds = []

    for _ in range(pswd_cnt):
        pswds.append(generate_password(pswd_len, chars))

    return pswds


def main():
    digits = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_."
    ambiguous_sym = 'il1Lo0O'
    chars = ''

    while True:
        print('Сколько паролей сгенерировать?')
        pswd_cnt = input()
        if is_nat(pswd_cnt):
            pswd_cnt = int(pswd_cnt)
            break

    while True:
        print('Какова примерная длинна пароля?')
        pswd_len = input()
        if is_nat(pswd_len):
            pswd_len = int(pswd_len)
            if pswd_len >= 8:
                break
            else:
                print('Длинна пароля не должна быть меньше 8 символов')

    while True:
        print('Включать ли цифры <0123456789>? Введите <Д> или <Н>:)')
        ans = input()
        if ans == 'Д':
            chars += digits
            break
        elif ans == 'Н':
            break

    while True:
        print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Введите <Д> или <Н>:)')
        ans = input()
        if ans == 'Д':
            chars += uppercase_letters
            break
        elif ans == 'Н':
            break

    while True:
        print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Введите <Д> или <Н>:)')
        ans = input()
        if ans == 'Д':
            chars += lowercase_letters
            break
        elif ans == 'Н':
            break

    while True:
        print('Включать ли символы !#$%&*+-=?@^_? Введите <Д> или <Н>:)')
        ans = input()
        if ans == 'Д':
            chars += punctuation
            break
        elif ans == 'Н':
            break

    while True:
        print('Исключать ли неоднозначные символы il1Lo0O? Введите <Д> или <Н>:)')
        ans = input()
        if ans == 'Д':
            for c in ambiguous_sym:
                chars = chars.replace(c, '')
            break
        elif ans == 'Н':
            break

    print(*generate_passwords(pswd_cnt, pswd_len, chars), sep='\n')


main()
