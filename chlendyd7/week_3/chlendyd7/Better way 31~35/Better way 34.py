import math

#math.pi = 원주율(π, 파이)
# sin = 높이/빗변

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps  # 한 스텝당 라디안 크기 계산
    for step in range(steps):
        radians = step * step_size    # 현재 step을 라디안으로 변환
        fraction = math.sin(radians)  # sin 함수 적용
        output = amplitude * fraction # sin 값을 amplitude로 스케일링
        yield output  # 결과를 제너레이터로 반환

def transmit(output):
    if output is None:
        print(f'출력: None')
    else:
        print(f'출력: {output:>5.1f}')

def run(it):
    for output in it:
        transmit(output)

# run(wave(3.0, 8))

def my_generator():
    received = yield 1
    print(f'받은 값= {received}')

# send에 관해서 링크 참조
# https://chlendyd7.notion.site/iterator-send-value-1bc933ef874080e3a69cc7ba31cbb1d0?pvs=4
it = iter(my_generator())
output = next(it)
print(f'출력값 = {output}')

try:
    next(it)
except StopIteration:
    pass

print('=============================')

it = iter(my_generator())
output = it.send(None) # next 대신 사용한건가?
# 최초로 send를 호출할 때 인자로 전달할 수 있는 유일한 값은 None뿐이다
# (다른 값을 전달하면 실행 시점에 ‘TypeError: can’t send non-None value to a just-started generator

print(f'출력값 = {output}')

try:
    it.send('안녕!')
except StopIteration:
    pass


def wave(amplitude, steps):
    step_size = 2 * math.pi / steps  # 한 스텝당 라디안 크기 계산
    for step in range(steps):
        radians = step * step_size    # 현재 step을 라디안으로 변환
        fraction = math.sin(radians)  # sin 함수 적용
        output = amplitude * fraction # sin 값을 amplitude로 스케일링
        yield output  # 결과를 제너레이터로 반환

import math
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield                # 초기 진폭을 받는다
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output     # 다음 진폭을 받는다

def run_modulating(it):
    amplitudes = [
        None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    # 제일 처음 None을 넣음
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

# run_modulating(wave_modulating(12))
#

# 진폭이 고정 된 경우
def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)

run(complex_wave())


def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)

# run_modulating(complex_wave_modulating())

# 링크 아랫부분 왜 list를 제너레이터로 변환해서 사용하는가에 대한 답변
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it) # 다음 입력 받기
        output = amplitude * fraction
        yield output

def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)

def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)

run_cascading()
