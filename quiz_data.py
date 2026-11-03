from quiz import Quiz


def get_default_quizzes():
    return [
        Quiz(
            "Python에서 정수를 나타내는 자료형은?",
            ["str", "int", "bool", "list"],
            2
        ),
        Quiz(
            "Python에서 문자열을 나타내는 자료형은?",
            ["int", "str", "dict", "bool"],
            2
        ),
        Quiz(
            "Python에서 참(True)과 거짓(False)을 나타내는 자료형은?",
            ["list", "str", "bool", "int"],
            3
        ),
        Quiz(
            "Python에서 여러 값을 순서대로 저장하는 자료형은?",
            ["dict", "bool", "list", "int"],
            3
        ),
        Quiz(
            "Python에서 키(key)와 값(value)의 쌍으로 데이터를 저장하는 자료형은?",
            ["str", "list", "int", "dict"],
            4
        )
    ]