"""
mac.py
MAC(Multiply-Accumulate) 연산과 판정 기능
"""

EPSILON = 1e-9


def mac(pattern, filt):
    """
    입력 패턴과 필터의 MAC 점수를 계산한다.

    Args:
        pattern (list): 입력 패턴
        filt (list): 필터

    Returns:
        float: MAC 점수
    """
    score = 0.0

    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            score += pattern[i][j] * filt[i][j]

    return score


def judge(score_cross, score_x):
    """
    두 점수를 비교하여 결과를 반환한다.

    Returns
        Cross
        X
        UNDECIDED
    """

    if abs(score_cross - score_x) < EPSILON:
        return "UNDECIDED"

    if score_cross > score_x:
        return "Cross"

    return "X"