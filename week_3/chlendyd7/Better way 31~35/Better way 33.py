def move(period, speed):
    for _ in range(period):
        yield speed

def pause(delay):
    for _ in range(delay):
        yield 0

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta

def render(delta):
    print(f'Delta: {delta:.1f}')

def run(func):
    for delta in func():
        render(delta)

run(animate)

def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)

run(animate_composed)

import timeit

def child():
    for i in range(1_000_000):
        yield i

def slow():
    for i in child():
        yield i

def fast():
    yield from child()

baseline = timeit.timeit(
    stmt='for _ in slow(): pass',
    globals=globals(),
    number=50)
print(f'수동 내포: {baseline:.2f}s')

comparison = timeit.timeit(
    stmt='for _ in fast(): pass',
    globals=globals(),
    number=50)
print(f'합성 사용: {comparison:.2f}s')

reduction = -(comparison - baseline) / baseline
print(f'{reduction:.1%} 시간이 적게 듦')

'''
시간이 적게 드는 이유
수동 for 루프의 문제점

for i in child():
    yield i

child()에서 next()를 호출하여 값을 가져옴.
yield i를 실행하면서 다시 바깥 제너레이터 (slow())의 문맥으로 돌아감.
매번 next()와 yield 사이에서 컨텍스트 스위칭이 발생하여 성능이 저하됨.

yield from child()
Python 내부에서 C-레벨에서 child()를 직접 실행.
중간에 불필요한 next() 호출 및 yield 스위칭이 제거됨.
즉, yield from은 반복문을 Python 코드에서 실행하는 것이 아니라, Python의 내부 루프 최적화를 활용하여 실행하기 때문에 성능이 더 빠름.


3. 성능 차이를 살펴보는 예제 (디스어셈블링)
Python의 바이트코드 레벨에서 어떻게 동작하는지 살펴보겠습니다.

slow() 바이트코드
import dis
dis.dis(slow)
 7           0 LOAD_GLOBAL              0 (child)
              2 CALL_FUNCTION            0
              4 GET_ITER
        >>    6 FOR_ITER                10 (to 18)
              8 STORE_FAST               0 (i)
             10 LOAD_FAST                0 (i)
             12 YIELD_VALUE
             14 POP_TOP
             16 JUMP_ABSOLUTE            6
        >>   18 RETURN_VALUE

FOR_ITER → STORE_FAST → LOAD_FAST → YIELD_VALUE → POP_TOP → JUMP_ABSOLUTE → 반복
즉, 매 반복마다 Python이 for 문을 실행해야 함.


dis.dis(fast)

 11           0 LOAD_GLOBAL              0 (child)
              2 CALL_FUNCTION            0
              4 GET_YIELD_FROM_ITER
              6 YIELD_FROM
              8 RETURN_VALUE

'''