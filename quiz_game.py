from quiz_data import get_default_quizzes
from storage import load_state, save_state
from quiz import Quiz
import random

class QuizGame:
    def __init__(self):
        self.quizzes, self.best_score = load_state()

    def save(self):
        return save_state(self.quizzes, self.best_score)

    def show_menu(self):
        print("\n========================================")
        print("        Python 기초 퀴즈 게임")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def get_number(self, prompt, minimum, maximum):
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

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        total = self.get_number(
            f"몇 문제를 푸시겠습니까? (1~{len(self.quizzes)}): ",
            1,
            len(self.quizzes)
        )

        score = 0

        print(f"\n퀴즈를 시작합니다! (총 {total}문제)")

        shuffled_quizzes = random.sample(self.quizzes, total)

        for index, quiz in enumerate(shuffled_quizzes, start=1):
            print(f"\n---------- 문제 {index} ----------")
            quiz.display()

            answer = self.get_number("정답 입력 (1~4): ", 1, 4)

            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다! 정답은 {quiz.answer}번입니다.")

        percentage = round(score / total * 100)

        print("\n========================================")
        print(f"결과: {total}문제 중 {score}문제 정답! ({percentage}점)")
        print("========================================")

        if self.best_score is None or percentage > self.best_score:
            self.best_score = percentage
            print("새로운 최고 점수입니다!")

        self.save()

    def add_quiz(self):
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

        answer = self.get_number("정답 번호 (1~4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))

        self.save()
        print("퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

        print("----------------------------------------")

    def show_best_score(self):
        if self.best_score is None:
            print("\n아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"\n최고 점수: {self.best_score}점")

    def run(self):
        try:
            while True:
                self.show_menu()
                number = self.get_number("선택: ", 1, 5)

                if number == 1:
                    self.play_quiz()

                elif number == 2:
                    self.add_quiz()

                elif number == 3:
                    self.show_quiz_list()

                elif number == 4:
                    self.show_best_score()

                elif number == 5:
                    self.save()
                    print("게임을 종료합니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            self.save()
            print("\n데이터를 저장하고 안전하게 게임을 종료합니다.")