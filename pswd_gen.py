import random, math


def is_nat(n):
    return n.isdigit() and int(n) >= 0


def gen(pswd_cnt, pswd_len, chars):
    pswds = []
    al = []
    al.extend(chars)
    random.shuffle(al)
    for _ in range(pswd_cnt):
        pswd = []
        new_pswd_len = pswd_len + math.floor(pswd_len ** (1 / 3) * random.random() * 3)
        for _ in range(new_pswd_len):
            pswd.append(random.choice(al))
        random.shuffle(pswd)
        pswds.append(''.join(pswd))

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

    print(*gen(pswd_cnt, pswd_len, chars), sep='\n')


main()
