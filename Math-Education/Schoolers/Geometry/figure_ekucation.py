from view import detect_shape
import os
from random import choice


class Geometry:
    """
    Класс для игры в геометрию

    Атрибуты:
        - image (str): Путь к директории с изображениями фигур

    Методы:
        - __init__(): Конструктор класса
        - check_answer(answer: str) -> bool: Проверяет правильность ответа пользователя
        - choices_img() -> str: Возвращает случайное изображение из директории image
    """
    def __init__(self) -> None:
        """
        Конструктор класса Geometry

        Аргументы:
        Нет

        Возвращает:
        Нет
        """
        self.image: str = os.path.abspath(rf'D:\Hac\Math-Education\Schoolers\Geometry\{self.choices_img()}')
    
    def check_answer(self, answer: str) -> bool:
        """
        Проверяет правильность ответа пользователя

        Аргументы:
            - answer (str): Ответ пользователя
        Возвращает:
            - bool: True, если ответ правильный, иначе False
        """
        if detect_shape(image_path=rf'{self.image}{os.sep()}{self.choice_img()}') == answer:
            return True

        return False

    def choices_img(self) -> str:
        return choice(os.listdir(self.image))


a = Geometry()
a.check_answer(answer='None')