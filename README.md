# 교실 속 디지털혁신을 위한 파이썬 기초와 코딩 작업 가이드

> **2026 마전초 AI 디지털 활용 연수** · 강사: 이태학

학교 선생님들을 대상으로 한 **파이썬 기초 문법**과 **AI를 활용한 코딩 작업 플로우(Git/GitHub 버전관리 포함)** 연수 교육자료 저장소입니다.
연수 슬라이드(PPTX), 실습용 예제 코드, AI 코딩 프롬프트 규칙, IDE 실행 설정이 함께 들어 있습니다.

---

## 📁 폴더 구성

```
majeon_code/
├── 교실 속 디지털혁신을 위한 파이썬기초와 코딩 작업가이드.pptx   # 본 연수 슬라이드 (84장)
├── Git 계정 생성 및 PULL, PUSH 수행 가이드.pptx                # Git/GitHub 보조 가이드 (12장)
├── main.py              # 메인 프로그램 파일 (Hello, World! — 실습 시작점)
├── calc.py              # 실습 예제: 파이썬 간단 계산기
├── prompt/              # 학습자료: AI 코딩용 프롬프트 규칙
│   ├── coding rule.txt  #   코드 작성 규칙
│   ├── commit rule.txt  #   커밋 작성 규칙
│   └── push rule.txt    #   PUSH 규칙
├── .vscode/launch.json  # IDE(통합개발환경) 실행·디버깅 설정 (F5 실행)
└── .gitignore           # GitHub 업로드 제외 목록 (.venv/, .venvwin/, .vscode/)
```

> `.venv/`(Mac), `.venvwin/`(Windows) 파이썬 가상환경 폴더는 각자 PC에서 생성하며 저장소에는 올라가지 않습니다.

---

## 📚 연수 구성

### PART 01. 파이썬 기초 문법
참고교재: *윤성우의 열혈 파이썬 기초편*

| 주제 | 주요 내용 | 교실 속 실전 예시 |
|---|---|---|
| 코딩이란? | 고급/저급 언어, 컴파일러(C)와 인터프리터(Python), IDE | — |
| 기본 작성 원칙 | 콜론(`:`) + 공백 4칸 들여쓰기, 대소문자 구분, 주석(`#`) | 합격 여부 출력 |
| 단일 자료형 | `int`, `float`, `str` | — |
| 복수 자료형 | 리스트 `[]`, 튜플 `()`, 딕셔너리 `{}` | 학급 성적 데이터 구조화 |
| 입력과 형변환 | `input()`은 항상 `str` → `int()`/`float()` 변환 | 교실 간식비 더치페이 계산기 |
| 연산자 | 산술(`//`, `%`, `**`), 복합대입(`+=`), 비교, 논리(`and`/`or`/`not`) | 동전 교환기 · 무료배송 판별 |
| 조건문 | `if-else` vs `if-elif-else`, 조건 작성 순서의 중요성 | 미세먼지 경보 알림기 |
| 반복문 | `for`(횟수 정해짐) vs `while`(종료 조건만 정해짐), `range()` | 합격자 집계 · 저금통 목표 달성 |
| 루프 제어 | `break`, `continue` | 키오스크 메뉴 주문 루프 |
| 함수 | `def`, 타입 힌트(`a: int -> int`), `return` | BMI 계산기 |
| 객체지향 | 클래스(주조틀)와 객체(실체물), 절차지향과의 비교 | 교실 스마트 램프 제어 |
| 예외처리 | `IndentationError`/`NameError`/`TypeError`, `try-except` | 숫자 맞히기 입력 검증기 |

### PART 02. 코딩 작업 가이드
코딩 작업 흐름을 **자동차 수리 공정**(견인 → 검사 → 수리 → 검증 → 사용)에 빗대어 설명하고, 이를 **버전관리(VCS, 체크포인트 관리 도구)** 와 연결합니다.

```
 REMOTE ADD & PULL ──▶ Architecting ──▶ Coding ──▶ Run & Debug ──▶ COMMIT & PUSH
   (Git & GitHub)        (설계)        (By AI:       (실행·디버깅)     (Git & GitHub)
                                    Gemini & Claude code)  ★시간 최대 소요 지점
```

1. **저장소 생성** – GitHub에서 Repository 생성 (이름, 공개 여부, README, `.gitignore`)
2. **저장소 연결 및 다운로드** – 로컬 폴더 생성 → `git init` → `git remote add` → `git pull`
3. **설계** – 순서도로 모듈(함수·클래스)과 연결관계, 입출력 인자 및 자료형 정리 ([diagrams.net](https://app.diagrams.net/) 권장)
   - AI에게 아이디어 도움은 OK, **이해 없이 코드를 그대로 붙여넣기는 금지**
4. **코딩** – AI가 코드 작성, 사용자는 코드 검수 및 업데이트 판단 (`prompt/coding rule.txt` 활용)
5. **실행 테스트 및 에러 수정** – `F5` 실행, `F9` 중단점, `F10` 한 단계씩 실행, WATCH로 변수 값 확인
6. **커밋 및 원격지 업데이트** – IDE 소스 제어 패널에서 Commit → Push

### PART 03. FAQ & QnA
환경설정 팁, AI 토큰 효율적 사용법, 추천 AI 모델, **API 키·토큰을 코드에 직접 넣지 말 것**, 문법 학습법, AI가 짠 코드 검증 방법 등.

---

## 🚀 실습 환경 준비

### 1. 사전 준비
- **GitHub 계정** 만들기: <https://github.com/signup>
- **Git** 설치: <https://git-scm.com/install> (Mac은 터미널에서 `git` 입력 시 설치 안내)
- **IDE**: CURSOR 설치 후 GitHub 계정으로 로그인
- **Python 3** 설치

### 2. Git 최초 설정 (한 번만)
```bash
git --version
git config --global user.name "홍길동"
git config --global user.email "me@mail.com"
```

### 3. 저장소 내려받기
IDE에서 바탕화면에 `majeon` 폴더를 만들어 연 뒤, 터미널(Git Bash)에서:
```bash
pwd                                   # 현재 위치 확인
git init                              # 깃 저장소 시작
git remote add origin https://github.com/{내 아이디}/{저장소 이름}.git   # 원격지 등록(개별 주소)
git pull origin main                  # 원격지 내용 다운로드
```
또는 `git clone https://github.com/{내 아이디}/{저장소 이름}.git` 으로 한 번에 복사할 수 있습니다.

> 첫 PUSH 시 비밀번호 대신 **Personal access token (classic)** 이 필요합니다.
> GitHub 프로필 → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token (classic)

### 4. 파이썬 가상환경 만들기
```bash
# Windows (Git Bash)
py -m venv .venvwin

# Mac
python3 -m venv .venv
```
`.vscode/launch.json`은 OS에 따라 위 가상환경의 파이썬을 자동으로 사용하도록 설정되어 있습니다.

### 5. 실행
IDE에서 파일을 열고 **`F5`** (설정명: *Python: 현재 파일*), 또는 터미널에서:
```bash
python main.py
python calc.py
```
현재 예제는 표준 라이브러리만 사용하므로 별도 패키지 설치가 필요 없습니다.

---

## 🧪 예제 코드

### `main.py`
`Hello, World!`를 출력하는 최소 구조의 시작 파일입니다. `def main()` + `if __name__ == "__main__":` 패턴을 보여줍니다.
연수 중 AI에게 *"숫자 2개 받아서 계산기 역할 수행하는 python main.py 짜서 코드 편집기로 출력해."* 와 같이 요청해 내용을 채워 나가는 실습 대상입니다.

> 참고: 첫 줄의 `from ast import main`은 아래 `def main()`에 의해 덮어써져 실제로는 사용되지 않습니다.

### `calc.py` — 파이썬 간단 계산기
사칙연산 함수(`add`, `subtract`, `multiply`, `divide`)를 **타입 힌트**와 함께 정의하고, `while` 반복으로 계속 계산할 수 있는 예제입니다.

```
=== 파이썬 간단 계산기 ===

첫 번째 숫자를 입력하세요: 10
연산자를 입력하세요 (+, -, *, /): /
두 번째 숫자를 입력하세요: 4
결과: 10.0 / 4.0 = 2.5

계속 계산하시겠습니까? (y/n): n
계산기를 종료합니다.
```

**디버깅 실습 포인트**: `try-except` 블록이 의도적으로 주석 처리되어 있습니다.
숫자가 아닌 값을 입력하거나 `0`으로 나누면 프로그램이 에러로 종료되는 것을 확인한 뒤, 디버깅 모드(`F9`, `F10`, WATCH)로 원인을 추적하고 주석을 해제해 예외처리를 적용해 보세요.

---

## 🤖 AI 코딩 프롬프트 규칙 (`prompt/`)

AI(Gemini, Claude code 등)에게 코드 작성을 요청할 때 프롬프트에 함께 붙여 넣어, 일관된 품질의 결과물을 얻기 위한 규칙입니다.

| 파일 | 내용 |
|---|---|
| `coding rule.txt` | 코드 구조 순서(`from` import → `import` → 본문 → 직접실행 문), **모든 자료형 명기**, 필요 패키지는 `requirements.txt`에 버전과 함께 명기, 변경 내용 한국어 설명을 `temp/update.txt`에 작성 |
| `commit rule.txt` | 커밋 설명을 **사용자 요청 → 업데이트 목표 → 업데이트 내용 → 업데이트 결과** 형식의 개조식으로 정리 |
| `push rule.txt` | `config/github.py`에 기재된 저장소 주소의 `main` 브랜치로 PUSH |

> `requirements.txt`, `temp/update.txt`, `config/github.py`는 규칙에 따라 실습 중 생성되는 파일로, 초기 저장소에는 포함되어 있지 않습니다.

---

## 🔁 매일 반복 루틴 (Git 핵심 명령어)

| 명령어 | 언제 | 의미 |
|---|---|---|
| GitHub → New repository | 최초 1회 | 저장소 만들기 |
| `git config --global ...` | 최초 1회 | 이름·이메일 등록 |
| `git clone 주소` | 최초 1회 | 저장소를 내 PC로 복사 |
| `git pull` | 작업 시작 전 | 최신 내용 받기 |
| `git add .` | 작업 후 | 변경 파일 담기 |
| `git commit -m "..."` | 작업 후 | 변경 기록 저장 |
| `git push` | 작업 후 | GitHub로 올리기 |

- 상태 확인은 언제든 `git status`
- PUSH가 거절(rejected)되면 → `git pull` 후 다시 `git push`
- 충돌(conflict) 시 → 표시된 파일을 직접 고친 뒤 add → commit → push

---

## ⚠️ 유의사항

- **토큰·API 키를 코드에 직접 넣지 마세요.** 공개 저장소에 올라가면 크롤링 봇에 탐지되어 요금 폭탄을 맞을 수 있습니다. 환경변수로 관리하세요.
- AI가 작성한 코드는 **한 번에 조금씩, 이해한 범위 내에서만** 반영하세요. 줄별 주석·설명을 요청하면 검수에 도움이 됩니다.
- 문법은 따로 암기하기보다 직접 타이핑하며 체화하는 것을 권장합니다.

---

## 🔗 관련 링크

- 연수 단체 톡방 (카카오톡 오픈채팅): <https://open.kakao.com/o/ghuxbIXi>
- 연수 설문조사: <https://forms.gle/tXu9GzYSJECVLio68>
- 순서도 작성 도구: <https://app.diagrams.net/>
- Git 설치: <https://git-scm.com/install>
