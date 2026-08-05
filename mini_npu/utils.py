"""
utils.py
공통으로 사용하는 보조 함수
"""


def normalize_label(label):
    """
    다양한 라벨을 프로그램 내부 표준 라벨로 변환한다.

    +       -> Cross
    cross   -> Cross
    Cross   -> Cross
    x       -> X
    X       -> X
    """

    label = str(label).strip().lower()

    if label in ("+", "cross"):
        return "Cross"

    if label == "x":
        return "X"

    return label


def get_size(matrix):
    """
    행렬 크기 반환
    """

    return len(matrix)


def validate_same_size(pattern, filt):
    """
    패턴과 필터의 크기가 같은지 검사한다.
    """

    if len(pattern) != len(filt):
        return False

    for row_p, row_f in zip(pattern, filt):
        if len(row_p) != len(row_f):
            return False

    return True


def average(values):
    """
    평균 계산
    """

    if not values:
        return 0

    return sum(values) / len(values)