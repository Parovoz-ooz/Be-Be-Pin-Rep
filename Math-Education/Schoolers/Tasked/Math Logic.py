import re


class Logic:
    @staticmethod
    def __num_check(text: str) -> list:
        # Исправить str значения
        return re.findall(r'\d+(?:\.\d+)?', text)

    @validate
    def __task_description(text: str) -> str:
        pass
