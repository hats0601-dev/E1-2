import sys
import time
import tracemalloc

from quiz import Quiz


def main():
    total = 1000

    tracemalloc.start()

    start = time.perf_counter()

    quizzes = [
        Quiz(
            f"성능 테스트 문제 {i}",
            ["선택지 1", "선택지 2", "선택지 3", "선택지 4"],
            1
        )
        for i in range(1, total + 1)
    ]

    creation_time = time.perf_counter() - start

    start = time.perf_counter()

    target = "성능 테스트 문제 1000"
    found = next(
        (quiz for quiz in quizzes if quiz.question == target),
        None
    )

    search_time = time.perf_counter() - start

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"문제 수: {len(quizzes)}개")
    print(f"생성 시간: {creation_time:.6f}초")
    print(f"검색 시간: {search_time:.6f}초")
    print(f"검색 성공: {found is not None}")
    print(f"현재 추적 메모리: {current / 1024:.2f}KB")
    print(f"최대 추적 메모리: {peak / 1024:.2f}KB")


if __name__ == "__main__":
    main()