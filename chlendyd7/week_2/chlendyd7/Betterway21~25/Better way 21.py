# 변수 영역과 클로저의 상호작용 방식을 이해하라

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

# 클로저
# 위 대입문은 helper 영역 안에서 새로운 변수를 정의하는 것으로 취급되지 sort_priority 영역 안에서 기존 변수에 값을 대입하는 것으로 취급되지 않는다.
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True # 문제를 쉽게 해결할 수 있을 것 같다
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


# nonlocal을 통해 데이터가 클로저 밖에 있어서 다른 영역에 속한다는 사실을 분명히 알려준다. 위 문장은 변수를 대입 시 직접 모듈 영역(전역 영역)을 사용해야 한다고 지정하는 global 문을 보안
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        nonlocal found       # 추가함
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('발견:', found)
print(numbers)

# 그런데 nonlocal은 길어지면 어디 있는지 찾아야하니까 도우미 함수로 상태를 감싸는 편이 더 낫다.
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True