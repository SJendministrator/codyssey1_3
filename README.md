# Mini NPU Simulator

> Codyssey E1-3
>
> Python으로 구현한 Mini NPU(MAC 연산) 시뮬레이터

---

# 1. 프로젝트 소개

## 프로젝트 개요

본 프로젝트는 AI에서 사용하는 NPU(Neural Processing Unit)의 핵심 연산인
MAC(Multiply-Accumulate) 연산을 직접 구현한 Mini NPU 시뮬레이터이다.

사용자가 직접 3×3 필터와 패턴을 입력하여 결과를 확인할 수 있으며,
JSON 데이터셋을 이용한 대량 판정과 성능 분석도 수행한다.

외부 라이브러리를 사용하지 않고 Python 반복문만으로 MAC 연산을 구현하였다.

---

# 2. 개발 환경

|항목|내용|
|---|---|
|Language|Python 3.12|
|Library|표준 라이브러리(json, time)|
|OS|macOS|
|IDE|VSCode|
|External Library|사용하지 않음|

---

# 3. 프로젝트 구조

```text
mini_npu/
│
├── main.py
├── mac.py
├── matrix.py
├── loader.py
├── analyzer.py
├── utils.py
├── data.json
└── README.md
```

---

# 4. 실행 방법

## 프로그램 실행

```bash
python3 main.py
```

메뉴

```
1. User Input (3x3)
2. Analyze data.json
0. Exit
```

---

# 5. 구현 기능

## 1) 사용자 입력 모드

- 3×3 Cross 필터 입력
- 3×3 X 필터 입력
- 패턴 입력
- MAC 점수 계산
- 판정 결과 출력
- 평균 수행시간 출력

예시

```
Cross Score : 5.0
X Score     : 1.0

Result : Cross
```

---

## 2) JSON 분석 모드

data.json을 읽어

- 5×5
- 13×13
- 25×25

패턴을 자동 분석한다.

출력

- Cross Score
- X Score
- Result
- PASS / FAIL

---

## 3) 성능 분석

각 크기마다

- 10회 반복
- 평균 실행시간 측정

출력

```
5x5
13x13
25x25
```

연산횟수

```
N²
```

도 함께 출력한다.

---

# 6. 구현 내용

## MAC 연산

MAC(Multiply-Accumulate)은

각 위치의 값을

```
pattern × filter
```

로 곱한 뒤

모든 결과를 더하여

유사도를 계산하는 방식이다.

예시

```
0 1 0
1 1 1
0 1 0
```

×

```
0 1 0
1 1 1
0 1 0
```

↓

```
0
1
0
1
1
1
0
1
0
```

↓

```
Score = 5
```

---

## 라벨 정규화

프로그램 내부에서는

```
Cross
X
```

두 개의 라벨만 사용한다.

JSON에서 들어오는

```
+
cross
Cross
```

은 모두

```
Cross
```

로 변환한다.

```
x
X
```

은

```
X
```

로 변환한다.

이를 통해 데이터 표현이 달라도 동일하게 비교할 수 있다.

---

## 부동소수점 비교

MAC 결과는 float 값이므로

```
0.9
0.8999999999999999
```

처럼 표현되는 경우가 있다.

따라서

```
abs(a-b) < epsilon
```

정책을 적용하여

실제 값이 거의 같으면 동일한 값으로 판단하였다.

이를 통해 부동소수점 오차 때문에 잘못된 FAIL이 발생하는 문제를 방지하였다.

---

# 7. 시간복잡도

MAC 연산은

모든 원소를 한 번씩 방문한다.

필터 크기가

```
N × N
```

이라면

연산 횟수는

```
N²
```

이다.

따라서 시간복잡도는

```
O(N²)
```

이다.

실제 측정 결과에서도

5×5

↓

13×13

↓

25×25

로 갈수록 실행시간이 증가하는 것을 확인할 수 있었다.

---

# 8. 결과 리포트

## 테스트 결과

```
Total : 6

PASS : 6

FAIL : 0
```

## FAIL이 0개인 이유

프로그램 내부에서

- 라벨 정규화
- epsilon 기반 비교

를 적용하여

데이터 표현 차이와 부동소수점 오차를 모두 제거하였다.

따라서 모든 테스트가 정상적으로 PASS 되었다.

---

# 9. 트러블 슈팅

## 1. utils ImportError

### 문제

```
ImportError:
cannot import normalize_label
```

### 원인

utils.py를 저장하지 않아 Python이 빈 파일을 불러오고 있었다.

### 해결

파일 저장 후 다시 실행하여 해결하였다.

---

## 2. Dockerfile Build 실패

### 문제

```
Dockerfile cannot be empty
```

### 원인

Dockerfile 내용이 비어 있었다.

### 해결

베이스 이미지와 실행 명령을 추가한 후 정상적으로 이미지가 생성되었다.

---

## 3. 부동소수점 비교

### 문제

```
0.9

0.89999999999999
```

가 서로 다른 값으로 판정되었다.

### 해결

epsilon 비교를 적용하여 동일한 값으로 처리하였다.

---

# 10. 느낀 점

이번 프로젝트를 통해 AI에서 사용하는 MAC 연산의 원리를 직접 구현하면서
패턴 인식이 어떻게 이루어지는지 이해할 수 있었다.

또한 JSON 데이터 처리, 예외 처리, 부동소수점 비교, 성능 분석을 함께 구현하면서
단순한 알고리즘뿐 아니라 실제 프로그램을 구성하는 방법도 학습할 수 있었다.