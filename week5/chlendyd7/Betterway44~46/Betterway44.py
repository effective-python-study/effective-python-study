class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms

r0 = OldResistor(50e3)
print('이전:', r0.get_ohms())
r0.set_ohms(10e3)
print('이후:', r0.get_ohms())
'''
이전: 50000.0
이후: 10000.0
'''

r0.set_ohms(r0.get_ohms() - 4e3)
assert r0.get_ohms() == 6e3

class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3

r1.ohms += 5e3


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

r2 = VoltageResistance(1e3)
print(f'이전: {r2.current:.2f} 암페어')
r2.voltage = 10
print(f'이후: {r2.current:.2f} 암페어')

'''
이전: 0.00 암페어
이후: 0.01 암페어
'''


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'저항 > 0이어야 합니다. 실제 값: {ohms}')
        self._ohms = ohms

r3 = BoundedResistance(1e3)
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# r3.ohms = 0

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# BoundedResistance(-5)
# 생성자에 잘못된 값을 넘기는 경우에도 예외가 발생한다.

class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Ohms는 불변객체입니다")
        self._ohms = ohms

r4 = FixedResistance(1e3)
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# r4.ohms = 2e3

class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r7 = MysteriousResistor(10)
r7.current = 0.01
print(f'이전: {r7.voltage:.2f}')
r7.ohms
print(f'이후: {r7.voltage:.2f}')

'''
디스크립터(Descriptor)는 파이썬에서 속성(attribute)을 제어하는 특별한 방식으로, 객체의 속성 접근 시 특정 동작을 정의할 수 있도록 해주는 클래스입니다. 
디스크립터는 주로 __get__, __set__, __delete__ 메서드를 사용하여 속성의 접근 방식을 제어할 수 있습니다. 이들은 클래스의 속성이나 객체에 접근할 때 호출됩니다.
'''

class MyDescriptor:
    def __init__(self):
        self.value = 42

    def __get__(self, instance, owner):
        print(f"Getting value: {self.value}")
        return self.value

    def __set__(self, instance, value):
        print(f"Setting value to: {value}")
        self.value = value

    def __delete__(self, instance):
        print("Deleting value")
        del self.value

class MyClass:
    # MyClass의 속성 'attr'에 MyDescriptor를 사용
    attr = MyDescriptor()

# MyClass 인스턴스를 생성
obj = MyClass()

# 디스크립터의 __get__ 호출
print(obj.attr)  # Getting value: 42

# 디스크립터의 __set__ 호출
obj.attr = 100  # Setting value to: 100

# 디스크립터의 __get__ 호출
print(obj.attr)  # Getting value: 100

# 디스크립터의 __delete__ 호출
del obj.attr  # Deleting value
