"""
analyzer.py

MAC 연산 결과 분석 및 성능 측정 모듈
"""

import time

from mac import mac
from loader import prepare_case, get_filters, get_patterns


EPSILON = 1e-9


def judge(score_cross, score_x):
    """
    Cross / X / UNDECIDED 판정
    """

    if abs(score_cross - score_x) < EPSILON:
        return "UNDECIDED"

    if score_cross > score_x:
        return "Cross"

    return "X"


def benchmark(pattern, filt, repeat=10):
    """
    MAC 연산 평균 시간(ms) 측정
    """

    start = time.perf_counter()

    for _ in range(repeat):
        mac(pattern, filt)

    end = time.perf_counter()

    return ((end - start) / repeat) * 1000


def analyze_case(case_name, case):
    """
    하나의 패턴 분석
    """

    score_cross = mac(case["pattern"], case["cross_filter"])
    score_x = mac(case["pattern"], case["x_filter"])

    result = judge(score_cross, score_x)

    passed = (result == case["expected"])

    return {
        "name": case_name,
        "cross_score": score_cross,
        "x_score": score_x,
        "result": result,
        "expected": case["expected"],
        "pass": passed
    }


def analyze_json(data):
    """
    data.json 전체 분석
    """

    filters = get_filters(data)
    patterns = get_patterns(data)

    total = 0
    passed = 0
    failed = []

    print("\n========== TEST RESULT ==========\n")

    for name, info in patterns.items():

        success, case = prepare_case(name, info, filters)

        total += 1

        if not success:
            print(f"{name} : FAIL ({case})")
            failed.append((name, case))
            continue

        result = analyze_case(name, case)

        state = "PASS" if result["pass"] else "FAIL"

        print(f"[{name}]")
        print(f"Cross Score : {result['cross_score']}")
        print(f"X Score     : {result['x_score']}")
        print(f"Result      : {result['result']}")
        print(f"Expected    : {result['expected']}")
        print(state)
        print()

        if result["pass"]:
            passed += 1
        else:
            failed.append((name, "Prediction mismatch"))

    print_summary(total, passed, failed)

    return total, passed, failed


def performance_test(data):
    """
    크기별 성능 측정
    """

    print("\n========== PERFORMANCE ==========\n")

    filters = get_filters(data)
    patterns = get_patterns(data)

    checked = set()

    for name, info in patterns.items():

        success, case = prepare_case(name, info, filters)

        if not success:
            continue

        size = len(case["pattern"])

        if size in checked:
            continue

        checked.add(size)

        avg = benchmark(case["pattern"], case["cross_filter"])

        print(
            f"{size}x{size} | "
            f"{avg:.6f} ms | "
            f"Operations : {size*size}"
        )


def print_summary(total, passed, failed):
    """
    최종 결과 출력
    """

    print("\n========== SUMMARY ==========")

    print(f"Total : {total}")
    print(f"PASS  : {passed}")
    print(f"FAIL  : {len(failed)}")

    if failed:

        print("\nFailed Cases")

        for name, reason in failed:
            print(f"- {name} : {reason}")