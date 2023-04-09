import operator
from random import randint


class Examples:
    @staticmethod
    def checking_examples(example: str, answer: int or float):
        """
        Метод проверки решения примера. Если ответ правильный, возвращаем True
        :param example:
        :param answer:
        :retype bool:
        """
        if eval(example) == answer:
            return True
        else:
            return False

    @staticmethod
    def example_gen_addition() -> str:
        """
        Метод генерации примера сложения
        До 20
        :return:
        """
        return f'{randint(1, 10)} + {randint(1, 10)}'

    @staticmethod
    def example_generation_multiply() -> str:
        """
        Метод генерации умножения
        До 25
        :return:
        """
        return f'{randint(1, 5)} * {randint(1, 5)}'

    @staticmethod
    def example_generation_division() -> str:
        """
        Функция генерации деления
        До 6
        :return:
        """

        # Переменные делимого и делиителя
        dividend: int = randint(1, 6)
        divider: int = randint(1, 6)

        # Гарантируем что результат будет целым числом
        while dividend % divider != 0:
            dividend = randint(1, 10)
            divider = randint(1, 10)

        return f'{dividend} // {divider}'

    @staticmethod
    def example_subtraction_generator() -> str:
        """
        Медот генерации вычитания
        До 5
        :return:
        """
        minuend: int = randint(1, 5)
        subtrahend: int = randint(1, 5)

        while minuend <= subtrahend:
            minuend: int = randint(1, 5)
            subtrahend: int = randint(1, 5)

        return f'{randint(1, 5)} - {1, 5}'

