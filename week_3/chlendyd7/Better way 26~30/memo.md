## 26. `functools.wraps`를 사용해 데코레이터를 정의하라

데코레이터를 만들 때, 데코레이터가 감싸고 있는 원래 함수를 찾을 수 없게 되는 문제가 발생할 수 있다. 이는 데코레이터 함수가 실행되면서 기존 함수의 위치를 잃어버리기 때문이다.

이를 방지하기 위해 `functools.wraps`를 사용하여 함수의 중요한 메타데이터를 복사해야 한다.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("함수가 호출되기 전 실행")
        result = func(*args, **kwargs)
        print("함수가 호출된 후 실행")
        return result
    return wrapper

@my_decorator
def say_hello():
    "이 함수는 인사를 합니다."
    print("안녕하세요!")

print(say_hello.__name__)  # say_hello
print(say_hello.__doc__)   # 이 함수는 인사를 합니다.
```

## 27. `map`과 `filter` 대신 컴프리헨션을 사용하라

파이썬에서는 리스트 컴프리헨션을 사용하여 `map`과 `filter`의 기능을 더욱 직관적으로 구현할 수 있다.

```python
# map 사용
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

# 리스트 컴프리헨션 사용 (더 직관적)
squares = [x ** 2 for x in numbers]
```

```python
# filter 사용
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 리스트 컴프리헨션 사용 (더 가독성 좋음)
even_numbers = [x for x in numbers if x % 2 == 0]
```

## 28. 컴프리헨션 내부에 제어 하위 식을 세 개 이상 사용하지 말라

컴프리헨션에서 너무 많은 중첩된 제어문을 사용하면 코드의 가독성이 떨어진다. 따라서, 도우미 함수나 명시적인 `for` 루프를 사용하는 것이 더 좋다.

### ❌ 안 좋은 예제 (너무 복잡한 컴프리헨션)
```python
flat = [
    x for sublist1 in my_lists
    for sublist2 in sublist1
    for x in sublist2
]
```

### ✅ 좋은 예제 (명시적 `for` 루프 사용)
```python
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
```

또한, 필터링이 필요한 경우도 가독성이 중요한 경우는 `for` 루프를 직접 사용하는 것이 좋다.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
```

## 29. 대입식을 사용해 컴프리헨션 안에서 반복 작업을 피하라

바다 코끼리 관련 내용으로 list comprehension 내 사용 할 경우 if 문과 같이 뒷쪽에 체크 시 값이 원하는 상황이 안된다

혹은 마지막 값이 저장 될 수 있으니 주의를 요한다

[영호님의 정리]

## 30. 리스트를 반환하기보다는 제너레이터를 사용하라

리스트를 반환하는 대신 제너레이터를 사용하면 메모리 사용량을 줄이고 효율적인 데이터 처리가 가능하다.

### ✅ 제너레이터 사용 예제
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5
```

### ✅ 파일을 읽을 때 제너레이터 활용
```python
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file("big_file.txt"):
    print(line)
```

제너레이터는 `yield`를 만나면 현재 실행 상태를 저장하고 제어권을 반환하며, 이후 `next()`나 `for` 루프가 호출되면 **이전 상태를 복원하고 `yield` 다음 줄부터 실행을 재개**한다.

[더 자세한 내용 보기](https://chlendyd7.notion.site/Generator-191933ef874080328004c4a97a918970?pvs=4)



#### 새로운 맴버 추가

