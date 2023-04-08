from view import detect_shape
import os
from random import choice


class Geometry:    
    def __init__(self) -> None:
        self.image: str = os.path.abspath(r'D:\Hac\Math-Education\Schoolers\Geometry\img')
    
    def check_answer(self, answer: str) -> bool:
        if detect_shape(image_path=rf'{self.image}{os.sep()}{self.choice_img()}') == answer:
            return True
        return False

    def choices_img(self) -> str:
        return choice(os.listdir(self.image))


a = Geometry()
a.check_answer(answer='None')