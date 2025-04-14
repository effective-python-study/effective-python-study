'''
__init_subclass__ 정의 안에서 super().__init_subclass__를 호출해 여러 계층에 걸쳐 클래스를 검증하고 다중 상속을 제대로 처리하도록 하라
'''

'''
    __new__는 객체를 생성할 때 호출되는 메서드.
    인스턴스 생성 전에 클래스가 새로운 객체를 만들기 위해 메모리를 할당하는 단계에서 호출돼.

    __init_subclass__는 Python 3.6부터 도입된 특별 메서드로, 클래스를 상속받을 때 자동으로 호출되는 훅(hook) 메서드입니다. 
    주로 메타프로그래밍 또는 프레임워크를 설계할 때 하위 클래스의 동작을 커스터마이징할 때 사용됩니다.
'''

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f'* 실행: {name}의 메타 {meta}.__new__')
        print('기반클래스들:', bases)
        print(class_dict)
        print()
        return type.__new__(meta, name, bases, class_dict)

class MyClass(metaclass=Meta):
    stuff = 123
    
        

    def foo(self):
        pass

class MySubclass(MyClass):
    other = 567

    def bar(self):
        pass

class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # Polygon 클래스의 하위 클래스만 검증한다
        if bases:
            if class_dict['sides'] < 3:
                raise ValueError('다각형 변은 3개 이상이어야 함')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides -2) * 180

class Triangle(Polygon):
    sides = 3

class Rectangle(Polygon):
    sides = 4

class Nonagon(Polygon):
    sides = 9

assert Triangle.interior_angles() == 180
assert Rectangle.interior_angles() == 360
assert Nonagon.interior_angles() == 1260

print('class 이전')

# class Line(Polygon):
#     print('sides 이전')
#     sides = 2
#     print('sides 이후')

print('class 이후')

class BetterPolygon:
    sides = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides < 3:
            raise ValueError('다각형 변은 3개 이상이어야 함')

    @classmethod
    def interior_angles(cls):
        return (cls.sides -2) * 180

class Hexagon(BetterPolygon):
    sides = 6
assert Hexagon.interior_angles() == 720

print('class 이전')
# class Point(BetterPolygon):
#     sides = 1

print('class 이후')

class ValidateFilled(type):
    def __new__(meta, name, bases, class_dict):
        if bases:
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('지원하지 않는 color 값')
        return type.__new__(meta, name, bases, class_dict)

class Filled(metaclass=ValidateFilled):
    color = None


# class RedPentagon(Filled, Polygon):
#    color = 'red'
#    sides = 5

'''
Python에서 클래스는 메타클래스(metaclass) 를 기반으로 생성되는데, 
다중 상속을 할 때 상속받은 부모 클래스들의 메타클래스가 서로 다르면 충돌이 발생합니다.
'''

class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # 루트 클래스가 아닌 경우만 검증한다
        if not class_dict.get('is_root'):
            if class_dict['sides'] < 3:
                raise ValueError('다각형 변은 3개 이상이어야 함')
        return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
    is_root = True
    sides = None  # 하위 클래스에서 이 애트리뷰트 값을 지정해야 한다

class ValidateFilledPolygon(ValidatePolygon):
    def __new__(meta, name, bases, class_dict):
        # 루트 클래스가 아닌 경우만 검증한다
        if not class_dict.get('is_root'):
            if class_dict['color'] not in ('red', 'green'):
                raise ValueError('지원하지 않는 color 값')
        return super().__new__(meta, name, bases, class_dict)

class FilledPolygon(Polygon, metaclass=ValidateFilledPolygon):
    is_root = True
    color = None  # 하위 클래스에서 이 애트리뷰트 값을 지정해야 한다

class GreenPentagon(FilledPolygon):
    color = 'green'
    sides = 5

greenie = GreenPentagon()
assert isinstance(greenie, Polygon)

# class OrangePentagon(FilledPolygon):
#    color = 'orange'
#    sides = 5

class Filled:
    color = None  # 하위 클래스에서 이 애트리뷰트 값을 지정해야 한다

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.color not in ('red', 'green', 'blue'):
            raise ValueError('지원하지 않는 color 값')

class RedTriangle(Filled, Polygon):
    color = 'red'
    sides = 3

ruddy = RedTriangle()
assert isinstance(ruddy, Filled)
assert isinstance(ruddy, Polygon)

print('class 이전')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#class BlueLine(Filled, Polygon):
#    color = 'blue'
#    sides = 2

print('class 이후')

#
print('class 이전')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#class BeigeSquare(Filled, Polygon):
#    color = 'beige'
#    sides = 4

print('class 이후')
