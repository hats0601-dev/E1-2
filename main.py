from quiz_data import get_default_quizzes
from quiz import Quiz
from quiz_data import get_default_quizzes

def show_menu():
    print("\n========================================")
    print("        Python 기초 퀴즈 게임")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")


def get_number(prompt, minimum, maximum):
    while True:
        value = input(prompt).strip()

        if not value:
            print("입력값이 비어 있습니다. 다시 입력하세요.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if minimum <= number <= maximum:
            return number

        print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")


def play_quiz(quizzes, best_score):
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return best_score

    score = 0
    total = len(quizzes)

    print(f"\n퀴즈를 시작합니다! (총 {total}문제)")

    for index, quiz in enumerate(quizzes, start=1):
        print(f"\n---------- 문제 {index} ----------")
        quiz.display()

        answer = get_number("정답 입력 (1~4): ", 1, 4)

        if quiz.check_answer(answer):
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다! 정답은 {quiz.answer}번입니다.")

    percentage = round(score / total * 100)

    print("\n========================================")
    print(f"결과: {total}문제 중 {score}문제 정답! ({percentage}점)")
    print("========================================")

    if best_score is None or percentage > best_score:
        best_score = percentage
        print("새로운 최고 점수입니다!")

    return best_score

def add_quiz(quizzes):
    print("\n새로운 퀴즈를 추가합니다.")

    while True:
        question = input("문제를 입력하세요: ").strip()
        if question:
            break
        print("문제는 비워둘 수 없습니다.")

    choices = []

    for number in range(1, 5):
        while True:
            choice = input(f"선택지 {number}: ").strip()

            if choice:
                choices.append(choice)
                break

            print("선택지는 비워둘 수 없습니다.")

    answer = get_number("정답 번호 (1~4): ", 1, 4)

    quizzes.append(Quiz(question, choices, answer))
    print("퀴즈가 추가되었습니다!")
    
def show_quiz_list(quizzes):
    if not quizzes:
        print("\n등록된 퀴즈가 없습니다.")
        return

    print(f"\n등록된 퀴즈 목록 (총 {len(quizzes)}개)")
    print("----------------------------------------")

    for number, quiz in enumerate(quizzes, start=1):
        print(f"{number}. {quiz.question}")

    print("----------------------------------------")

def show_best_score(best_score):
    if best_score is None:
        print("\n아직 퀴즈를 풀지 않았습니다.")
    else:
        print(f"\n최고 점수: {best_score}점")

def main():
    quizzes = get_default_quizzes()
    best_score = None

    try:
        while True:
            show_menu()
            number = get_number("선택: ", 1, 5)

            if number == 1:
                best_score = play_quiz(quizzes, best_score)
            elif number == 2:
                add_quiz(quizzes)
            elif number == 3:
                show_quiz_list(quizzes)
            elif number == 4:
                show_best_score(best_score)
            elif number == 5:
                print("게임을 종료합니다.")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n안전하게 게임을 종료합니다.")


if __name__ == "__main__":
    main()