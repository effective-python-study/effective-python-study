26. functools.wrap을 사용해 데코레이터를 정의하라:
데코레이터를 만들 때 데코레이터가 감싸고 있는 원래 함수를 찾을 수 없다. 데코리에터 함수가 실행되며 기존의 함수의 위치를 잃어버리기 때문이다
그래서 functools의 wraps를 사용해서 함수의 중요한 메타데이터를 복사해야한다

27. map과 filter 대신 컴프리헨션을 사용하라
파이썬 list 내부에 조건식을 정의하는 기법
실무에서도 자주 사용하는 기법

28. 컴프리헨션 내부에 제어 하위 식을 세 개 이상 사용하지 말라

# bad code
flat = [
    x for sublist1 in my_lists
    for sublist2 in sublist1
    for x in sublist2
    ]

# good code
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]

위와 같은 코드를 작성할꺼면 도우미 함수나 for문을 직접적으로 사용하는게 더 가독성에 좋다

29. 대입식을 사용해 컴프리헨션 안에서 반복 작업을 피하라
    29는 잘 모르겠어서 한번 더 볼 예정

30. 리스트를 반환하기보다는 제너레이터를 사용하라

제너레이터와 yield가 만나면 파이썬은 현재 실행 상태를 저장하고 제어권을 반환

그 뒤 다음 next()나 for 루프가 호출되면 이전 상태를 복원하고 yield 다음 줄부터 실행을 재개


