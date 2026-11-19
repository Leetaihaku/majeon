def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


def main():
    print("=== 파이썬 간단 계산기 ===")

    while True:
        # try:

        num1 = float(input("\n첫 번째 숫자를 입력하세요: "))
        operator = input("연산자를 입력하세요 (+, -, *, /): ").strip()
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("지원하지 않는 연산자입니다. (+, -, *, / 중 선택)")
            continue

        # 결과가 정수 형태면 소수점 제거 후 출력 (예: 5.0 -> 5)
        formatted_result = int(result) if result.is_integer() else result
        print(f"결과: {num1} {operator} {num2} = {formatted_result}")

        # except ValueError as e:
        #     if "could not convert string to float" in str(e):
        #         print("오류: 올바른 숫자를 입력해 주세요.")
        #     else:
        #         print(f"오류: {e}")

        again = input("\n계속 계산하시겠습니까? (y/n): ").strip().lower()
        if again != "y":
            print("계산기를 종료합니다.")
            break


if __name__ == "__main__":
    main()
