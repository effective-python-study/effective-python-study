class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f'{name}를 위한 값'
        setattr(self, name, value)
        return value

data = LazyRecord()
print('이전:', data.__dict__)
print('foo:', data.foo)
print('이후:', data.__dict__)


class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'* 호출: __getattr__({name!r}), '
              f'인스턴스 딕셔너리 채워넣음'
              )
        result = super().__getattr__(name)
        print(f'* 반환: {result!r}')
        return result

data = LoggingLazyRecord()
print('exists:', data.exists)
print('첫 번째 foo:', data.foo)
print('두 번째 foo', data.foo)
'''
exists 애트리뷰트가 인스턴스 딕셔너리에 있으므로 __getattr__이 결코 호출되지 않는다. 
반면 foo 애트리뷰트는 처음에 인스턴스 딕셔너리에 없으므로 맨 처음 foo에 접근하면 __getattr__이 호출된다. 
하지만 foo에 접근하면 __getattr__이 호출되고, 안에서 setattr을 수행해 인스턴스 딕셔너리 안에 foo라는 애트리뷰트를 추가한다. 
따라서 두 번째로 foo에 접근하면 __getattr__이 호출되지 않는다는 사실을 로그에서 확인할 수 

__getattr__은 속성이 존재하지 않을 때만 호출되므로, 한 번 속성이 조회되어 인스턴스 딕셔너리에 저장되면 이후 호출에서는 __getattr__이 호출되지 않습니다.
'''

print('====================')
class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f'* 호출: __getattr__({name!r})')
        try:
            value = super().__getattribute__(name)
            print(f'* {name!r} 찾음, {value!r} 반환')
            return value
        except AttributeError:
            value = f'{name}을 위한 값'
            print(f'* {name!r}를 {value!r}로 설정')
            setattr(self, name, value)
            return value

data = ValidatingRecord()
print('exists:', data.exists)
print('첫 번째 foo:', data.foo)
print('두 번재 foo:', data.foo)


class MissingPropertyRecord:
    def __getattr__(self, name):
        '''
        자체적으로 내장되있는 코드를 눈에 보이게 구현해줌
        '''
        if name == 'bad_name':
            raise AttributeError(f'{name}을 찾을 수 없음')
        return 1 # 무조건 1 반환

data = MissingPropertyRecord()
# print(data.bad_name)

print('===================')
data = LoggingLazyRecord()
print('이전: ', data.__dict__)
print('최초에 foo가 있나: ', hasattr(data, 'foo'))
print('이후: ', data.__dict__)
print('다음에 foo가 있나: ', hasattr(data, 'foo'))

print('===================')
data = ValidatingRecord() # __getattribute__를 구현
print('최초에 foo가 있나: ', hasattr(data, 'foo'))
print('다음에 foo가 있나: ', hasattr(data, 'foo'))

class SavingRecord:
    def __setattr__(self, name, value):
        # 데이터를 데이터베이스 레코드에 저장한다
        super().__setattr__(name, value)

class LoggingSavingRecord(SavingRecord):
    def __setattr__(self, name, value):
        print(f'* 호출: __setattr__({name!r}, {value!r})')
        super().__setattr__(name, value)

print('===================')
data = LoggingSavingRecord()
print('이전: ', data.__dict__)
data.foo = 5
print('이후: ', data.__dict__)
data.foo = 7
print('최후:', data.__dict__)

'''
__getattribute__와 __setattr__의 문제점은 여러분이 원하든 원하지 않든 
어떤 객체의 모든 애트리뷰트에 접근할 때마다 함수가 호출된다는 것이다. 
예를 들어 어떤 객체와 관련된 딕셔너리에 키가 있을 때만 이 객체의 애트리뷰트에 접근하고 싶다고 하자.
'''

class BrokenDictionaryRecord:
    def __init__(self, data):
        self._data = {}
    def __getattribute__(self, name):
        print(f'* 호출: __getattribute__({name!r})')
        return self._data[name]

data = Brokedata = BrokenDictionaryRecord({'foo': 3})
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# data.foo

''''
self._data[name]을 반환하려고 self._data에 접근함.

3. self._data 접근
self._data도 self의 속성이므로 __getattribute__('_data')가 다시 호출됨!

다시 __getattribute__가 실행되면서 또 self._data[name]을 조회하고, 다시 __getattribute__('_data') 호출됨.
'''

class DictionaryRecord:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        print(f'* 호출: __getattribute__({name!r})')
        data_dict = super().__getattribute__('_data')
        return data_dict[name]
'''
data.foo를 조회하면 __getattribute__('foo')가 호출됨.

super().__getattribute__('_data')를 사용해 _data 속성을 가져옴.

여기서 super()를 사용하면 __getattribute__를 다시 호출하지 않고 기본 객체 속성 접근 방식을 사용함.

_data[name]을 안전하게 반환 → 정상 동작
'''
data = DictionaryRecord({'foo': 3})
print('foo: ', data.foo)