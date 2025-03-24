# 숫자 두개를 입력을 받아서
# +, -, *, /를 출력하는 프로그램을 만들어 보자
  a =int ("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        break  # 올바른 숫자를 입력하면 루프 종료
    except ValueError:
        print("숫자를 정확히 입력해주세요!")

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

# 0으로 나누는 경우 예외 처리
if num2 != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("0으로 나눌 수 없습니다!")