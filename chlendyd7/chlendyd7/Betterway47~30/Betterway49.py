import json

class Serializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})

class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'

point = Point2D(5, 3)
print('객체:', point)
print('직렬화한 값:', point.serialize())

class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f'BetterPoint2D({self.x}, {self.y})'


before = BetterPoint2D(5, 3)
print()
print('이전:', before)
data = before.serialize()
print('직렬화한 값:', data)
after = BetterPoint2D.deserialize(data)
print('이후:', after)

class BetterSerializable:
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })

    def __repr__(self):
        name = self.__class__.__name__
        args_str = ', '.join(str(x) for x in self.args)
        return f'{name}({args_str})'

registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])

class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

register_class(EvenBetterPoint2D)
print()
before = EvenBetterPoint2D(5, 3)
print('이전: ', before)
data = before.serialize()
print('직렬화한 값:', data)
after = deserialize(data)
print('이후: ', after)


class Point3D(BetterSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

# register을 까먹음
# register_class(Point3D)
# point = Point3D(5, 9, -4)
# data = point.serialize()
# deserialize(data)


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

class RegisteredSerializable(
    BetterSerializable,
    metaclass=Meta
):
    pass

class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z

before = Vector3D(10, -7, 3)
print('이전: ', before)
data = before.serialize()
print('직렬화한 값:', data)
print('이후: ', deserialize(data))

class BetterRegisteredSerializable(BetterSerializable):
    def __init_subclass__(cls):
        super().__init_subclass__()
        register_class(cls)


class Vector1D(BetterRegisteredSerializable):
    def __init__(self, magnitude):
        super().__init__(magnitude)
        self.magnitude = magnitude

before = Vector1D(6)
print('이전: ', before)
data = before.serialize()
print('직렬화한 값:', data)
print('이후: ', deserialize(data))

'''
__init_subclass__는 Python에서 서브클래스를 정의할 때 자동으로 호출되는 메서드입니다. 즉, 어떤 클래스를 상속받아 새로운 클래스를 만들면, 그 순간 부모 클래스의 __init_subclass__가 호출됩니다.

이 메서드는 Python 3.6부터 도입된 기능이며, 클래스를 메타프로그래밍 방식으로 제어하고 싶을 때 유용하게 사용됩니다.

클래스 자체를 만들 때 실행
'''