"""
Mini NPU Simulator

메인 실행 파일
"""

from loader import load_json
from matrix import input_matrix
from analyzer import (
    analyze_json,
    performance_test,
    judge,
    benchmark
)
from mac import mac


DATA_FILE = "data.json"


def user_mode():
    """
    3x3 사용자 입력 모드
    """

    print("\n=== Filter A (Cross) ===")
    filter_a = input_matrix(3)

    print("\n=== Filter B (X) ===")
    filter_b = input_matrix(3)

    print("\n=== Pattern ===")
    pattern = input_matrix(3)

    score_a = mac(pattern, filter_a)
    score_b = mac(pattern, filter_b)

    result = judge(score_a, score_b)

    print("\n========== RESULT ==========")

    print(f"A Score : {score_a}")
    print(f"B Score : {score_b}")
    print(f"Result  : {result}")

    avg = benchmark(pattern, filter_a)

    print(f"\nAverage MAC Time : {avg:.6f} ms")


def json_mode():
    """
    data.json 분석 모드
    """

    try:
        data = load_json(DATA_FILE)

    except FileNotFoundError:
        print("data.json 파일을 찾을 수 없습니다.")
        return

    analyze_json(data)

    performance_test(data)


def menu():

    while True:

        print("\n==============================")
        print(" Mini NPU Simulator")
        print("==============================")
        print("1. User Input (3x3)")
        print("2. Analyze data.json")
        print("0. Exit")

        choice = input("Select : ")

        if choice == "1":
            user_mode()

        elif choice == "2":
            json_mode()

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    menu()