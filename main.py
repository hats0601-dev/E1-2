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


def main():
    while True:
        show_menu()

        try:
            choice = input("선택: ").strip()

            if not choice:
                print("입력값이 비어 있습니다. 다시 입력하세요.")
                continue

            number = int(choice)

            if number == 5:
                print("게임을 종료합니다.")
                break
            elif 1 <= number <= 4:
                print(f"{number}번 기능은 구현 예정입니다.")
            else:
                print("1~5 사이의 숫자를 입력하세요.")

        except ValueError:
            print("숫자를 입력하세요.")
        except (KeyboardInterrupt, EOFError):
            print("\n안전하게 게임을 종료합니다.")
            break


if __name__ == "__main__":
    main()