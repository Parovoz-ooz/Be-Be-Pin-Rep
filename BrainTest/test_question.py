import sqlite3
import os


def testing() -> None:
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'user_data.db'))
    print(data_path)
    connect = sqlite3.connect(data_path)

    question = {
        'Шел человек в город и по дороге догнал 3-х своих знакомых. Сколько человек шло в город?': '4',
        'Тройка лошадей пробежали 5 км. По сколько км пробежала каждая лошадь?': '5',
        'Вставь пропущенное буквы в слове Ж...знь': 'и',
        'Составь слово из слогов Ку Жи Нй Пя Бы': 'Кубы'
    }

    results = list()

    for i_quest, i_answer in question.items():
        print(i_quest)
        if input('Ответ: ') == i_answer:
            results.append(1)
        else:
            results.append(0)

    results.append(int((results.count(1) / len(results)) * 100))

    print(connect.execute("""SELECT * FROM users WHERE id=1""").fetchall())

    connect.execute(f"""UPDATE users SET brain={results[-1:]} WHERE id=1""")


testing()