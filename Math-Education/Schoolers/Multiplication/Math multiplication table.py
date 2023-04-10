from random import randint

class Table:
    @staticmethod
    def check_answer(answer):
        if randint(1, 10) * randint(1, 10) == answer:
            return True
        return False

    def push_to_lable(self):
        pass

