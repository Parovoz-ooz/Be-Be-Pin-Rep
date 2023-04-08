import speech_recognition as sr
import re

class Learn:
    @staticmethod
    def _record_volume():
        reco = sr.Recognizer()

        with sr.Microphone(device_index=1) as source:
            print('Слуушаем. Говорите громко и чётко')
            audio = reco.listen(source)

        try:
            return reco.recognize_google(audio, language='ru-Ru')
        except sr.UnknownValueError:
            return 'Вас не слышно'

    def alphabet(self):
        for i_sym in 'абвгдеёжзийклмнопрстуфхцчшщыэюя':
            while True:
                if self._record_volume().lower() == i_sym:
                    break

    def learning(self):
        with open('story.txt', 'r', encoding='utf-8') as story:
            for i_story in story.read().split():
                for j_story in i_story.split():
                    while True:
                        print(f'Прочитай: {j_story}')
                        if self._record_volume().lower() == j_story.lower():
                            break

                        print(f'Неправильно, скажи ещё раз')


a = Learn()
a.learning()