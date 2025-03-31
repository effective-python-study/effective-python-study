class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

foo = MyObject()
assert foo.public_field == 5

assert foo.get_private_field() == 10

# foo.__private_field
# AttributeError: 'MyObject' object has no attribute '__private_field'. Did you mean: 'get_private_field'?
# 어트리뷰트를 찾을 수 없게 되있음


# 내부에서 접근은 가능
class MyOtherObject:
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71


# 하위 클래스는 부모 클래스의 비공개 필드에 접근할 수 없다
class MyParentObject:
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
baz.get_private_field()

# 자동으로 python에서 바꿔준다
baz._MyParentObject__private_field  == 71
'''
비공개 애트리뷰트에 대한 접근 구문이 실제로 가시성을 엄격하게 제한하지 않는 이유는 무엇일까? 
가장 간단한 답을 생각해보면, 파이썬의 모토로 자주 회자되는 ‘우리는 모두 책임질줄 아는 성인이다’일 것이다. 
이 말이 뜻하는 바는 우리가 하고 싶은 일을 언어가 제한하면 안 된다는 것이다
'''
print(baz.__dict__)

class MyStringClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)

foo = MyStringClass(5)
assert foo.get_value() == '5'

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)

foo = MyIntegerSubclass('5')
assert foo.get_value() == 5


class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)

foo = MyIntegerSubclass('5')
assert foo.get_value() == 5

'''
Python에서는 __(더블 언더스코어)로 시작하는 속성을 클래스 내부에서만 접근할 수 있도록 보호하기 위해 자동으로 이름을 변경(name mangling) 함.
self.__value는 내부적으로 _MyBaseClass__value로 변경됨.
'''
class MyBaseClass:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

class MyStringClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value())  # 변경됨

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        # return int(self._MyBaseClass__value)  # 이건 가능
        return int(self._MyStringClass__value)

foo = MyIntegerSubclass(5)
# foo.get_value()

class MyStringClass:
    def __init__(self, value):
        self._value = value



'''
주로 공개 API에 속한 클래스의 경우 신경 써야 하는 부분이다. 여러분이 만든 공개 API를 외부에 제공하는 경우에는 하위 클래스 작성이 여러분의 제어밖에서 일어나므로 
이런 문제가 발생해도 리팩터링이 불가능하다. 특히 애트리뷰트 이름이 흔한 이름(예: value)일 때 충돌이 자주 발생할 수 있다. 
이런 문제가 발생할 위험성을 줄이려면, 부모 클래스 쪽에서 자식 클래스의 애트리뷰트 이름이 
자신의 애트리뷰트 이름과 겹치는 일을 방지하기 위해 비공개 애트리뷰트를 사용할 수 있다.
'''
class ApiClass:
    def __init__(self):
        self._value = 5
    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'

a = Child()
print(f'{a.get()} 와 {a._value} 는 달라야 합니다.')

class ApiClass:
    def __init__(self):
        self.__value = 5
    def get(self):
        return self.__value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'

a = Child()
print(f'{a.get()} 와 {a._value} 는 달라야 합니다.')
