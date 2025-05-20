'''
На вход программе подаётся строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.

Формат входных данных
На вход программе подаётся строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.




Sample Input 1:  Day, mice. "Year" is a mistake!
Sample Output 1: Gdb, qmgi. "Ciev" ku b tpzahrl!

Sample Input 2:  my name is Python!
Sample Output 2: oa reqi ku Veznut!
'''

EN_MOD = 26


def crypt(k, msg):
    cipher = []

    for c in msg:
        base = -1

        if 'a' <= c <= 'z':
            base = ord('a')
        elif 'A' <= c <= 'Z':
            base = ord('A')

        if base == -1:
            cipher.append(c)
        else:
            x = ord(c) - base
            y = (x + k) % EN_MOD
            cipher.append(chr(y + base))

    return ''.join(cipher)


words = input().split()

words_lens = []
for w in words:
    cnt = 0
    for c in w:
        if c.isalpha():
            cnt += 1
    words_lens.append(cnt)

for i in range(len(words)):
    words[i] = crypt(words_lens[i], words[i])

print(' '.join(words))
