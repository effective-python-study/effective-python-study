#디버깅 출력에는 repr 문자열을 사용하라

print('foo 뭐시기')

my_value = 'foo 뭐시기'
print(str(my_value))
print('%s' % my_value)
print(f'{my_value}')
print(format(my_value))
print(my_value.__format__('s'))
print(my_value.__str__())

'''
문제는 어떤 값을 사람이 읽을 수 있는 형식의 문자열로 바꿔도 이 값의 실제 타입과 구체적인 구성을 명확히 알기 어렵다는 점
'''
print(5)
print('5')

int_value = 5
str_value = '5'
print(f'{int_value} == {str_value} ?')

a = '\x07'
print(repr(a))

b = eval(repr(a))
assert a == b

print(repr(5))
print(repr('5'))
# repr을 호출하는 것은 % 연산자에 %r 형식화 문자열을 사용하는 것이나 f-문자열에 !r 타입 변환을 사용하는 것과 같다.
print('%r' % 5)
print('%r' % '5')

int_value = 5
str_value = '5'
print(f'{int_value!r} != {str_value!r}')

class OpaqueClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, 'foo')
print(obj)

class BetterClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'BetterClass({self.x!r}, {self.y!r})'

obj = BetterClass(2, '뭐시기')
print(obj)

obj = OpaqueClass(4, 'baz')
print(obj.__dict__)
