def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)


def normalize_copy(numbers):
    numbers_copy = list(numbers)
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
assert sum(percentages) == 100.0

def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result
'''

현재 코드에서 의도하지 않은 동작이 발생할 가능성이 매우 큼!
문제점을 단계별로 분석해볼게. 🚨

🔴 문제 분석
def normalize_func(get_iter):
    total = sum(get_iter())  # 🚨 첫 번째 호출
    result = []
    for value in get_iter():  # 🚨 두 번째 호출
        percent = 100 * value / total
        result.append(percent)
    return result
여기서 get_iter()를 두 번 호출하는 것이 문제야.

🔍 발생하는 문제
get_iter()는 람다 함수 lambda: read_visits(path)이므로, 실행될 때마다 새로운 제너레이터가 반환됨.
첫 번째 sum(get_iter())에서 get_iter()를 실행하면서 파일을 처음부터 끝까지 읽음 → 제너레이터 소진됨.
두 번째 for value in get_iter():에서 get_iter()를 또 호출함 → 새로운 제너레이터 반환됨(하지만 처음부터 다시 읽음).
즉, 두 번의 호출에서 서로 다른 제너레이터를 사용하게 됨.
total 값은 첫 번째 호출에서 계산된 것인데, 두 번째 호출에서는 다른 제너레이터를 사용하므로 불일치가 발생할 가능성이 있음.
'''

path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
class ReadVisits:
    # 인스턴스 변수
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0
'''
유일한 단점은 두 번 읽는 다는 것
'''
'''
컨테이너 타입이 iter에 전달되면 매번 새로운 이터레이터 객체가 반환된다?
'''


def normalize_defensive(numbers):
    if iter(numbers) is numbers:
        raise TypeError('컨테이너를 제공해야 합니다')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator):
        raise TypeError('컨테이너를 제공해야 합니다')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

visits = ReadVisits(path)
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

'''
🔹 ReadVisits가 Iterator가 아닌 이유
ReadVisits는 **이터레이터(Iterator)가 아니라 컨테이너(Container)**이기 때문이야.
왜냐하면 __iter__() 메서드를 구현하고 있지만, 이터레이터 객체 자체가 아니라, 새로운 이터레이터를 생성하여 반환하는 구조이기 때문이지.
💡 __iter__()를 호출할 때마다 새로운 이터레이터(generator)가 생성됨.
💡 ReadVisits 자체는 컨테이너 역할을 하므로, isinstance(visits, Iterator)는 False.
'''

# https://chlendyd7.notion.site/iterator-1b6933ef8740800b88ffde075a749ea8?pvs=4

visits = [15, 35, 80]
it = iter(visits)
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# normalize_defensive(it)