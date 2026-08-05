"""
loader.py

JSON 파일을 읽고 필터와 패턴 데이터를 관리하는 모듈
"""

import json
from utils import normalize_label, validate_same_size


def load_json(path):
    """
    JSON 파일을 읽어 딕셔너리 형태로 반환한다.

    Args:
        path (str): data.json 경로

    Returns:
        dict
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_filters(data):
    """
    JSON에서 filters 데이터를 반환한다.

    Returns:
        dict
    """
    return data.get("filters", {})


def get_patterns(data):
    """
    JSON에서 patterns 데이터를 반환한다.

    Returns:
        dict
    """
    return data.get("patterns", {})


def extract_size(pattern_key):
    """
    패턴 키에서 크기를 추출한다.

    예)
    size_5_1  -> size_5
    size_13_4 -> size_13
    """

    parts = pattern_key.split("_")

    if len(parts) < 2:
        return None

    return f"size_{parts[1]}"


def get_filter_pair(filters, size_key):
    """
    해당 크기의 Cross/X 필터를 반환한다.

    Returns
        (cross_filter, x_filter)
    """

    if size_key not in filters:
        return None, None

    current = filters[size_key]

    cross_filter = current.get("cross")
    x_filter = current.get("x")

    return cross_filter, x_filter


def prepare_case(pattern_key, pattern_data, filters):
    """
    하나의 테스트 케이스를 분석 가능한 형태로 준비한다.

    Returns
        success(bool)
        result(dict)
    """

    size_key = extract_size(pattern_key)

    if size_key is None:
        return False, "패턴 키 형식 오류"

    cross_filter, x_filter = get_filter_pair(filters, size_key)

    if cross_filter is None or x_filter is None:
        return False, "필터를 찾을 수 없음"

    pattern = pattern_data.get("input")
    expected = normalize_label(pattern_data.get("expected"))

    if not validate_same_size(pattern, cross_filter):
        return False, "Cross 필터와 크기 불일치"

    if not validate_same_size(pattern, x_filter):
        return False, "X 필터와 크기 불일치"

    return True, {
        "pattern": pattern,
        "cross_filter": cross_filter,
        "x_filter": x_filter,
        "expected": expected
    }