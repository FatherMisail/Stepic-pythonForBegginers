import random


right_border = 1000


def is_valid_digit(m):
    return m.isdigit() and 1 <= int(m) <= right_border


def play():
    n = random.randint(1, right_border)

    try_counter = 0
    while True:
        print(f'Введите число в диапазоне [1, {right_border}]: ', end='')
        m = input()

        if not is_valid_digit(m):
            print(f'А может быть все-таки введем целое число от 1 до {right_border}?')
            continue

        m = int(m)
        try_counter += 1
        if m > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue

        if m < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue

        if m == n:
            print('Вы угадали, поздравляем!')
            print(f'Попыток: {try_counter}')
            break


def main():
    global right_border

    print('Добро пожаловать в числовую угадайку!')

    game_continue = True
    while game_continue:
        while True:
            print('Укажите правую границу: ', end='')
            b = input()
            if is_valid_digit(b):
                right_border = int(b)
                play()
                break

        while True:
            print('Еще разок?! (Д/Н): ', end='')
            ans = input()
            if ans == 'Н':
                game_continue = False
                break
            elif ans == 'Д':
                right_border = 1000
                break

            print(f'А может быть все-таки введем <Д> или <Н>?')
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

main()
