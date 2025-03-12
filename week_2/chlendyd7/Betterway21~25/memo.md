### 파이썬 클로저(Closure) 는 함수가 정의될 때 그 함수가 참조하는 변수들이 그 함수 외부에 있어도 여전히 그 변수들에 접근할 수 있는 기능을 의미합니다. 이는 내부 함수가 외부 함수의 변수를 기억하는 구조로, 주로 함수형 프로그래밍에서 유용하게 사용됩니다

### 파이썬의 함수는 일급 시민 객체이다: 함수가 프로그래밍 언어에서 객체로 취급된다. 함수가 변수에 할당될 수 있고 다른 함수의 인자로도 전달, 반환 값으로도 사용 될 수 있다

## 파이썬 인터프리터는 변수를 참조 할 때 다음 순서로 영역을 뒤짐
1. 현재 함수의 영역
2. 현재 함수를 둘러싼 영역
3. 현재 코드가 들어 있는 영역(global scope)
4. 내장 영역

변수에 값을 대입하는 것은 다른 방식으로 동작
변수가 현재 영역에 이미 정의되 있다면 그 변수의 값만 새로운 값으로 바뀐다


아래와 같이 함수의 인자에 대해서 *언패킹을 해서 사용 가능하다
```
def log(message, *values):  # 달라진 유일한 부분
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는 ', [1, 2])
log('안녕 ')  # 훨씬 좋다
```

그런데 *에 들어가는 인자의 개수가 처리하기 좋고 충분히 작다는 경우에만 사용하라
```
def my_generator():
    for i in range(100000):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)
```
위와 같이 사용한다면 메모리를 다 잡아 먹을 것이다

```
def remainder(number, divisor):
    return number % divisor
```

위치 기반 인자를 지정하려면 키워드 인자보다 앞에 지정해야 한다.

remainder(number=20, 7) X
remainder(20, divisor=7) O

```
my_kwargs = {
    'number': 20,
    'divisor': 7,
}

assert remainder(**my_kwargs) == 6
```
위의 예시와 같이 딕셔너리를 풀어서 사용할 수 있다

```
my_kwargs = {
    'divisor': 7,
}

assert remainder(number=20, **my_kwargs) == 6
```
섞어서도 사용이 가능하다. 그러나 중복은 있으면 안된다

```
my_kwargs = {
    'number': 20,
}

other_kwargs = {
    'divisor': 7,
}

assert remainder(**my_kwargs, **other_kwargs) == 6
```
섞어서도 사용이 가능하다

```
def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

print_parameters(alpha=1.5, beta=9, 감마=4)
```
아무 인자나 받는 함수를 만들 수도 있다

위 키워드 인자를 사용하면 

def log(message, when=datetime.now()):
    print(f'{when}: {message}')

log('안녕!')
sleep(0.1)
log('다시 안녕!')

위와 같이 default 인자를 설정하면 함수 첫 호출 시 when이 정해지고 원하는 방식으로 동작하지 않는다

def log(message, when=None):
    """메시지와 타임스탬프를 로그에 남긴다.

    Args:
        message: 출력할 메시지.
        when: 메시지가 발생한 시각(datetime).
            디폴트 값은 현재 시간이다.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

위와 같이 none을 활용해서 사용하는게 바람직하다


위치 인수(positional-only), 키워드 인수(keyword-only)

키워드 인수로는 전달할 수 없습니다
위치 인수로는 전달할 수 없고, 반드시 키워드 인수로만 전달