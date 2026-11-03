import json
from pathlib import Path
from quiz import Quiz
from quiz_data import get_default_quizzes

STATE_FILE = Path(__file__).resolve().parent / "state.json"


def save_state(quizzes, best_score):
    data = {
        "quizzes": [
            {
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer,
                "hint": quiz.hint
            }
            for quiz in quizzes
        ],
        "best_score": best_score
    }

    try:
        with open(STATE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return True

    except OSError as error:
        print(f"데이터 저장에 실패했습니다: {error}")
        return False

def load_state():
    if not STATE_FILE.exists():
        print("저장 파일이 없어 기본 퀴즈를 사용합니다.")
        return get_default_quizzes(), None

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("데이터 형식이 올바르지 않습니다.")

        quiz_data = data["quizzes"]
        best_score = data["best_score"]

        if not isinstance(quiz_data, list):
            raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

        if best_score is not None and (
            type(best_score) is not int or not 0 <= best_score <= 100
        ):
            raise ValueError("최고 점수 형식이 올바르지 않습니다.")

        quizzes = []

        for item in quiz_data:
            question = item["question"]
            choices = item["choices"]
            answer = item["answer"]
            hint = item.get("hint", "")

            if not isinstance(hint, str):
                raise ValueError("힌트 데이터가 올바르지 않습니다.")

            if (
                not isinstance(question, str)
                or not question.strip()
                or not isinstance(choices, list)
                or len(choices) != 4
                or any(
                    not isinstance(choice, str) or not choice.strip()
                    for choice in choices
                )
                or type(answer) is not int
                or not 1 <= answer <= 4
            ):
                raise ValueError("퀴즈 데이터가 올바르지 않습니다.")

            quizzes.append(Quiz(question, choices, answer, hint))

        print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개)")
        return quizzes, best_score

    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as error:
        print(f"저장 파일 오류: {error}")
        print("기본 퀴즈 데이터로 복구합니다.")
        return get_default_quizzes(), None