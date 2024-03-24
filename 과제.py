# 야구게임
# 1. 컴퓨터가 무작위로 0~9 숫자 중에서 3개 유일한 정수를 선택
# 2. 사용자는 0~9 숫자 중 3개를 입력하고 정답을 확인
# 3. 컴퓨터는 아래와 같은 룰로 정답에 대한 힌트를 제공
#     3-1. 컴퓨터가 선택한 숫자이면서 위치까지 일치하면 "Strike"
#     3-2. 컴퓨터가 선택한 숫자이지만 위치가 다르면 "Ball"
#     3-3. 컴퓨터가 선택한 숫자가 아니면 "Out"
# 4. 사용자는 10회까지 정답을 맞출 기회가 있음



import random



def baseball_game():
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number_list)
    number_computer_pick = []
    for i in range(3):
        number_computer_pick.append(number_list.pop())
    return number_computer_pick

def check_hint(number_computer_pick, number_user_pick):
    strike = 0
    ball = 0
    out = 0
    for i in range(3):
        if number_user_pick[i] in number_computer_pick:
            if number_user_pick[i] == number_computer_pick[i]:
                strike += 1
            else:
                ball += 1
        else:
            out += 1
    return strike, ball, out

print("야구게임을 시작합니다!")
print("0~9 숫자 3개를 띄어쓰기 없이 입력해주세요. 예) 123")
number_computer_pick = baseball_game()

max_tries = 10
for tries in range(max_tries):
    number_user_pick = list(map(int, input(f"\n남은 기회: {max_tries - tries}회\n숫자 3개를 입력하세요: ")))
    if len(set(number_user_pick)) != 3 or any(num < 0 or num > 9 for num in number_user_pick):
        print("잘못된 입력입니다. 0~9 숫자 3개를 띄어쓰기 없이 입력해주세요.")
        continue

    strike, ball, out = check_hint(number_computer_pick, number_user_pick)
    print(f"\n{strike}스트라이크, {ball}볼, {out}아웃")

    if strike == 3:
        print(f"\n정답입니다! {tries + 1}번 만에 맞추셨습니다. 게임을 종료합니다.")
        break

    if tries == max_tries - 1:
        print(f"\n아쉽습니다. 정답은 {number_computer_pick}였습니다.")