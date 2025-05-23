import random

word_list = ['попрошайка']


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]

    return stages[tries]


def input_is_valid(s):
    if len(s) == 0:
        return False

    for c in s:
        if 'А' <= c <= 'Я' or c == 'Ё':
            continue
        return False
    return True


def find_all(c, s):
    positions = []
    i = s.find(c)
    while i != -1:
        positions.append(i)
        i = s.find(c, i + 1)

    return positions


def replace_letter(c, word_completion, word):
    wc = list(word_completion)

    for i in find_all(c, word):
        wc[i] = c

    return ''.join(wc)


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв -
    # зачем называть названные буквы - угаданными - ума не
    # приложу, но так требует задание... так, что это - все введённые буквы (даже неугаданные)
    guessed_words = []  # список уже названных слов - все введённые слова (даже неугаданные)
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))

    while not guessed and tries:
        print(word_completion)

        s = input().upper()
        if input_is_valid(s):
            if len(s) == 1:
                if s[0] in guessed_letters:
                    print('Эта буква уже использована')
                    continue
                else:
                    guessed_letters.append(s[0])

                word_completion_new = replace_letter(s[0], word_completion, word)
            else:
                if s in guessed_words:
                    print('Это слово уже использовано')
                    continue
                else:
                    guessed_words.append(s)

                if s == word:
                    word_completion_new = s
                else:
                    word_completion_new = word_completion

            if word_completion_new == word_completion:
                tries -= 1
                print(display_hangman(tries))
            else:
                word_completion = word_completion_new

            if '_' not in word_completion:
                print('Поздравляем, вы угадали слово! Вы победили!')
                guessed = True
        else:
            print('Вводите только буквы русского алфавита')

    if not guessed:
        print(word)


def main():
    while True:
        play(get_word())
        print('Еще раз? Введите <Н> если хотите прерваться и что угодно, чтобы продолжить: ', end='')
        s = input().upper()
        if s == 'Н':
            break


main()
