"""
matrix.py

행렬 입력 및 출력 관련 모듈
"""


def input_matrix(size):
    """
    사용자에게 size x size 행렬을 입력받는다.

    잘못 입력하면 다시 입력하도록 한다.
    """

    matrix = []

    print(f"\n{size}x{size} 행렬을 입력하세요.")

    while len(matrix) < size:

        row_num = len(matrix) + 1

        raw = input(f"{row_num}행 : ")

        values = raw.split()

        if len(values) != size:
            print(f"입력 형식 오류 : {size}개의 숫자를 입력하세요.")
            continue

        try:
            row = [float(x) for x in values]
        except ValueError:
            print("숫자만 입력 가능합니다.")
            continue

        matrix.append(row)

    return matrix


def print_matrix(matrix):
    """
    행렬을 보기 좋게 출력한다.
    """

    for row in matrix:
        print(" ".join(f"{value:g}" for value in row))


def matrix_size(matrix):
    """
    행렬 크기 반환
    """

    return len(matrix)


def create_empty_matrix(size):
    """
    size x size 0 행렬 생성
    """

    matrix = []

    for _ in range(size):
        matrix.append([0] * size)

    return matrix