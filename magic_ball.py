import random

answers = [

        "Бесспорно",
        "Предрешено",
        "Никаких сомнений",
        "Определённо да",
        "Можешь быть уверен в этом",

        "Мне кажется - да",
        "Вероятнее всего",
        "Хорошие перспективы",
        "Знаки говорят - да",
        "Да",

        "Пока неясно, попробуй снова",
        "Спроси позже",
        "Лучше не рассказывать",
        "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять",

        "Даже не думай",
        "Мой ответ - нет",
        "По моим данным - нет",
        "Перспективы не очень хорошие",
        "Весьма сомнительно",
]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут, странник?')
name = input()
print(f'Привет, {name}')

while True:
    print('О чем ты бы хотел знать?')
    qst = input()

    print(random.choice(answers))
    print(f'{name}, тЫ ХОЧЕШЬ ЧТО-ЛИБО УЗНАТЬ У МЕНЯ ЕЩЕ?')
    qst = input()

    if qst == 'Н':
        print('Возвращайся, если возникнут вопросы!')
        break
