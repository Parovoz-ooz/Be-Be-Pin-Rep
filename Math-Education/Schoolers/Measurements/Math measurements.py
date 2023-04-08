from random import choice


class Measurements:
    def __init__(self):
        self.meas_dict: dict = {
            'метр': '100 сантиметров',
            'километр': '1000 метров',
            'сантиметр': '10 миллиметров' 
        }

    def check_answer(self, answer: str):
        if answer == self.meas_dict[self.print_meas]:
            return True
        return False

    def print_meas(self):
        return choice(len(self.meas_dict))
