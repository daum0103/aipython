# 아스키 코드 그림 출력하기

# 만약에 1을 입력하면 1번에 캐릭터 출력
# 만약에 2를 입력하면 2번 캐릭터 출력
# 3을 입력하면 3번 캐릭터 출력
# 잘못 입력하면 잘못 입력했다고 출력

# 아스키 코드 그림 출력하기
def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    
    for line in cat:
        print(line)

for i in range(5):
    #print(i)
    print_cat()

#print_cat()
    
def print_dog():
    dog = [
        " / \\__",
        "(    @\\___",
        " /         O",
        "/   (_____/",
        "/_____/   U"
    ]

    for line in dog:
        print(line)

def print_rabbit():
    rabbit = [
        "  (\\_/)",
        "  (o o)",
        "  ( > )"
    ]
    
    for line in rabbit:
        print(line)

print("그림 출력 프로그램")
print("=====================")
print("1. 고양이")
print("2. 강아지")
print("3. 토 끼")
print("=====================")
n = int(input("선택: "))
# 만약에 1을 입력하면 1번에 캐릭터 출력
if n == 1:
    print("고양이 그림")
    print_cat()
# 만약에 2를 입력하면 2번 캐릭터 출력
elif n == 2:
    print("강아지")
    print_dog()
    # 3을 입력하면 3번 캐릭터 출력
elif n == 3:
    print("토 끼")
    print_rabbit()
# 잘못 입력하면 잘못 입력했다고 출력
else: 
    print("잘못 입력")

# 동물그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오

# 위 프로그램을 완성한 사람은 프로그램이 계속(무한)반복하게 하고 
# 만약에 0을 입력하면 종료 되는 프로그램을 만드시오

# 함수로 만들기
def play():
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 종료")
    print("=====================")
    n = int(input("선택: "))

    if n == 1:
        print("고양이 그림")
        print_cat()
    elif n == 2:
        print("강아지 그림")
        print_dog()
    elif n == 3:
        print("토끼 그림")
        print_rabbit()
    elif n == 0:
        print("프로그램 종료!")
        break
    else:
        print("잘못 입력")

# 프로그램 5번 반복
for i in range(5):
    print(f"{i+1}번째 실행")
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("=====================")
    n = int(input("선택: "))

    if n == 1:
        print("고양이 그림")
        print_cat()
    elif n == 2:
        print("강아지 그림")
        print_dog()
    elif n == 3:
        print("토끼 그림")
        print_rabbit()
    else:
        print("잘못 입력")

# 무한반복
while True:
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 종료")
    print("=====================")
    n = int(input("선택: "))

    if n == 1:
        print("고양이 그림")
        print_cat()
    elif n == 2:
        print("강아지 그림")
        print_dog()
    elif n == 3:
        print("토끼 그림")
        print_rabbit()
    elif n == 0:
        print("프로그램 종료!")
        break
    else:
        print("잘못 입력")