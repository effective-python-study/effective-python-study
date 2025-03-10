# #01 Pythonic

## 01 파이썬 버전을 알자

아래 명령어를 사용해서 알아내다. ( 현재 내 Windows 환경에서는 python3 --version으로는 버전이 나오지 않고 있다. python --version으로는 나온다 )

```
python --version 	
python3 --version
```

```py
import sys
print(sys.version_info)
print(sys.version)
```

<br>

<br>

## 02 PEP 8 스타일 가이드를 따르라

pep은 파이썬 개선 제안서로 pep8은 파이썬 코드 스타일 가이드를 내용으로 담고 있다.

[참고] pee8은 따로 정리하는 문서가 있어 이번주 중으로 정리 완료 후 github에 업데이트 하겠습니다.

<br>

<br>

### 1. Code Lay-out

#### 들여쓰기

- 들여쓰기 레벨 당 **공백 4칸**의 간격을 사용합니다.

- (), {}, [] 안에서 연속된 줄들은 파이썬의 암시적인 줄 연결이나 '행잉 들여쓰기'를 통해 수직으로 정렬해야 한다.

  > ---
  >
  > 행잉 들여쓰기는 첫 번째 줄을 제외한 단락의 모든 줄이 들여쓰기 되는 유형 설정 스타일입니다. 파이썬의 맥락에서 이 용어는 괄호로 묶은 문장의 첫 괄호가 줄의 마지막 비백자 공간 문자이며, 이후 줄은 닫힘 괄호까지 들여쓰기 되는 스타일을 설명하는 데 사용됩니다.
  >
  > ---

  ```py
  # Wrong:
  
  # 수직 정렬을 하지않고 첫 줄에 인자들을 쓰면 가독성이 좋지 않다
  foo = long_function_name(var_one, var_two,
      var_three, var_four)
  ```

  ```py
  # Correct:
  
  # 첫 줄에 인자를 썼지만 수직정렬이 잘 됐다
  foo = long_function_name(var_one, var_two,
                           var_three, var_four)
  ```

  ---

  ```py
  # Wrong:
  
  # print문과 구분되도록 더 들여쓰기 필요
  def long_function_name(
      var_one, var_two, var_three,
      var_four):
      print(var_one)
  ```

  ```py
  # Correct:
  
  # 아래 print문과 구별되도록 추가적 들여쓰기를 했다.
  def long_function_name(
          var_one, var_two, var_three,
          var_four):
      print(var_one)
  ```

  ---

  행잉 들여쓰기를 사용할 때는 첫 번째 줄에 인자를 쓰지 않아야 하고, 추가적 들여쓰기를 통해 연속된 줄이란 것을 분명히 해야한다.

  ( 아래 연속 줄의 4공백 규칙은 선택사항이다. )

  ```py
  # 첫 줄에 인자 없이 hanging 들여쓰기
  foo = long_function_name(
      var_one, var_two,
      var_three, var_four)
  
  # '행잉 인텐트'는 4칸 공백 외에도 인텐트로 사용할 수 있습니다.
  foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
  ```

  <br>

  @@@@@

  When the conditional part of an `if`-statement is long enough to require that it be written across multiple lines, it’s worth noting that the combination of a two character keyword (i.e. `if`), plus a single space, plus an opening parenthesis creates a natural 4-space indent for the subsequent lines of the multiline conditional. This can produce a visual conflict with the indented suite of code nested inside the `if`-statement, which would also naturally be indented to 4 spaces. This PEP takes no explicit position on how (or whether) to further visually distinguish such conditional lines from the nested suite inside the `if`-statement. Acceptable options in this situation include, but are not limited to:

  ```
  # No extra indentation.
  if (this_is_one_thing and
      that_is_another_thing):
      do_something()
  
  # Add a comment, which will provide some distinction in editors
  # supporting syntax highlighting.
  if (this_is_one_thing and
      that_is_another_thing):
      # Since both conditions are true, we can frobnicate.
      do_something()
  
  # Add some extra indentation on the conditional continuation line.
  if (this_is_one_thing
          and that_is_another_thing):
      do_something()
  ```

  (Also see the discussion of whether to break before or after binary operators below.)

  The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace character of the last line of list, as in:

  ```
  my_list = [
      1, 2, 3,
      4, 5, 6,
      ]
  result = some_function_that_takes_arguments(
      'a', 'b', 'c',
      'd', 'e', 'f',
      )
  ```

  or it may be lined up under the first character of the line that starts the multiline construct, as in:

  ```
  my_list = [
      1, 2, 3,
      4, 5, 6,
  ]
  result = some_function_that_takes_arguments(
      'a', 'b', 'c',
      'd', 'e', 'f',
  )
  ```

<br>

<br>

#### **최대 줄 길이**

- 모든 줄은 최대 79자로 제한한다

- 구조적 제약이 적은 긴 텍스트 블록(예: docstring 또는 주석)의 경우, 줄 길이는 72자로 제한해야 합니다.

  **[ 이유 ]**

  팀의 협업과 효율적인 코드 사용을 위해 제한하는 것이며, 일부 팀은 훨씬 긴 줄 길이를 선호합니다. 
  만약 팀이 이 문제에 대해 합의에 도달할 수 있다면, 주석과 docstring은 여전히 72자로 줄 바꿈 하되 코드의 줄 길이 제한을 99자까지 늘리는 것도 괜찮습니다.

  ( Python 표준 라이브러리는 보수적으로 79자(그리고 docstring/주석은 72자)로 줄 길이를 제한합니다. )

  ----

  **[ 긴 줄 연결 ]**

  긴 줄을 역슬레시 없이 줄 바꿈 하는 권장 방식은 Python의 괄호, 대괄호, 중괄호 내에 있는 암묵적 줄 연결을 사용하는 것입니다. 긴 줄은 괄호로 감싼 표현식을 여러 줄로 나누어 작성할 수 있습니다. 이는 줄 연결을 위한 역슬래시(\\) 사용보다 선호됩니다.

  ---

  **[ 역슬레시를 사용하는 경우 ]**

  역슬래시(\\) 사용이 여전히 적절한 경우도 있습니다. 예를 들어, Python 3.10 이전에는 암묵적 연결을 사용할 수 없었던 여러 개의 with 문이 있는 경우 역슬래시가 허용되었습니다:

  ```py
  with open('/path/to/some/file/you/want/to/read') as file_1, \
       open('/path/to/some/file/being/written', 'w') as file_2:
      file_2.write(file_1.read())
  ```

<br>

#### 탭 또는 스페이스

- 스페이스은 선호하는 들여쓰기 방법입니다.
- 탭은 이미 탭으로 들여쓰기 된 코드와 일관성을 유지하기 위해서 만 사용해야 합니다.
  ( 탭과 공백을 섞어 사용할 수 없습니다 )
- Python은 들여쓰기에 탭과 공백을 혼용하는 것을 허용하지 않습니다.

<br>

#### 이진 연산자 줄바꿈

수십 년 동안 권장된 스타일은 이진 연산자 뒤에서 줄바꿈을 하는 것이었습니다. 
그러나 이렇게 할 경우 두 가지 측면에서 가독성이 떨어질 수 있습니다.

1. 첫째, 연산자들이 화면의 서로 다른 열에 흩어져 보이게 되고, 
2. 둘째, 각 연산자가 피연산자에서 떨어져 바로 앞 줄로 이동하게 됩니다. 

* 그 결과, 어떤 항목이 더해지고 어떤 항목이 빼지는지를 눈으로 확인하는 데 추가적인 노력이 필요해집니다.

----

이런 가독성 문제를 해결하기 위해, 수학자들과 그 출판사들은 반대의 규칙을 따릅니다. 
수학의 전통을 따르는 것이 보통 더 읽기 쉬운 코드를 만들어 줍니다.
( Python 코드에서 지역적으로 일관성이 있는 한 이진 연산자 앞이나 뒤에서 줄바꿈을 해도 괜찮습니다. )
새로운 코드에서는 Knuth의 스타일을 권장합니다.

```py
# 잘못된 예:
# 연산자가 피연산자와 멀리 떨어져 있습니다.
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

```py
# 올바른 예:
# 연산자와 피연산자를 쉽게 매칭할 수 있습니다.
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

<br>

<br>

#### 빈 줄

* **최상위(top-level) 함수**와 **클래스 정의**는 **2줄씩 띄어** 씁니다.

* 클래스 내의 **메소드 정의는 1줄씩 띄어** 씁니다.
* 관련 **함수 그룹을 구분하기 위해**(드물게) 추가 **1줄**을 띄어 사용할 수 있습니다.
  * 관련된 한 줄짜리 코드 묶음 사이에는 빈 줄을 생략할 수 있습니다(예: 여러 개의 임시 구현).
* **함수 내에서는 논리적 구분**을 나타내기 위해 **1줄**을 드물게 띄어 사용합니다.
* Python은 contrl-L(즉, ^L) 폼 피드 문자를 공백으로 인정합니다.
  * 많은 도구들이 이 문자를 페이지 구분자로 취급하므로, 파일 내 관련 섹션의 페이지를 구분하는 데 사용할 수 있습니다.
  * 단, 일부 편집기나 웹 기반 코드 뷰어는 제어-L을 폼 피드로 인식하지 못하고 다른 기호로 표시할 수 있습니다.

<br>

<br>

#### 소스 파일 인코딩

<u>코어 Python 배포판의 코드는 항상 UTF-8을 사용해야 하며, 인코딩 선언이 없어야 합니다.</u>

---

표준 라이브러리에서는 테스트 목적으로만 비-UTF-8 인코딩을 사용해야 합니다.
비-ASCII 문자는 드물게 사용하며, 가능하면 지명이나 인명 등을 나타내는 데에만 사용해야 합니다.
데이터로서 비-ASCII 문자를 사용할 경우, z̯̯͡a̧͎̺l̡͓̫g̹̲o̡̼̘와 같은 시끄러운 유니코드 문자나 바이트 순서 표시(Byte Order Marks)를 피해야 합니다.

Python 표준 라이브러리의 모든 식별자는 반드시 ASCII 문자만 사용해야 하며, 
가능한 경우 영어 단어를 사용해야 합니다(많은 경우 약어나 기술 용어가 영어가 아닐 수 있음).

전 세계를 대상으로 하는 오픈 소스 프로젝트들도 유사한 정책을 채택할 것을 권장합니다.

----

<br>

<br>

<br>

#### 임포트

보통 임포트는 별도의 줄에 작성해야 합니다:

```python
# 올바른 예:
import os
import sys

# 잘못된 예:
import sys, os
```

다음과 같이 작성하는 것은 괜찮습니다:

```python
# 올바른 예:
from subprocess import Popen, PIPE
```

임포트는 항상 파일 상단에 위치하며, 모듈 주석과 docstring 바로 뒤, 그리고 모듈 전역 변수와 상수보다 앞에 있어야 합니다.

**[ 임포트 순서 ]** 

임포트는 다음 순서로 그룹화해야 합니다:

1. 표준 라이브러리 임포트
2. 관련 서드파티 임포트
3. 로컬 애플리케이션/라이브러리 전용 임포트

* 각 임포트 그룹 사이에는 빈 줄을 한 줄씩 넣어야 합니다.

절대 임포트를 권장합니다. 절대 임포트는 보통 더 읽기 쉽고, 임포트 시스템이 잘못 구성된 경우(예를 들어, 패키지 내 디렉터리가 sys.path에 들어갔을 때) 더 나은 오류 메시지를 제공하거나 더 안정적으로 동작하는 경향이 있기 때문입니다:

```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

하지만 복잡한 패키지 구조에서 절대 임포트를 사용하면 불필요하게 길어질 수 있으므로, 명시적 상대 임포트도 허용되는 대안입니다:

```python
from . import sibling
from .sibling import example
```

표준 라이브러리 코드에서는 복잡한 패키지 구조를 피하고 항상 절대 임포트를 사용해야 합니다.

클래스를 포함하는 모듈에서 클래스를 임포트할 때는 다음과 같이 작성하는 것이 보통 괜찮습니다:

```python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

만약 이와 같이 작성해서 지역 이름 충돌이 발생한다면, 명시적으로 작성해야 합니다:

```python
import myclass
import foo.bar.yourclass
```

그리고 `myclass.MyClass`와 `foo.bar.yourclass.YourClass`처럼 사용합니다.

와일드카드 임포트(즉, `from <module> import *`)는 네임스페이스에 어떤 이름들이 존재하는지 불분명하게 만들어 독자와 많은 자동화 도구들을 혼란스럽게 하므로 피해야 합니다.
 와일드카드 임포트가 정당화될 수 있는 한 가지 경우는 내부 인터페이스를 공개 API의 일부로 재공개할 때입니다. (예를 들어, 선택적 가속기 모듈의 정의로 순수 Python으로 작성된 인터페이스 구현을 덮어쓸 때, 어떤 정의가 미리 정해지지 않은 경우 등)
 이와 같이 이름을 재공개할 때는, 공개 및 내부 인터페이스에 관한 아래의 지침이 여전히 적용됩니다.

<br>

<br>

<br>

## 03 bytes와 str 차이를 알아두라

* **bytes** : bytes 타임의 인스턴스에는 부호 없는 8바이트 데이터가 그대로 들어간다.
  ( <u>종종 아스키 인코딩을 사용해 내부 문자를 표시</u>한다 )
  * 직접 대응하는 텍스트 인코딩이 없다 - 유니코드 데이터로 변환하려면 bytes.decode 메서드를 호출해야 한다.
  
* **str** : str인스턴스에는 사람이 사용하는 언어의 문자를 표현하는 <u>유니코드 코드</u> 포인트가 들어있다.
  * 직접 대응하는 이진 이코딩이 없다 - 이진데이터로 변환하려면 str.encode 메서드를 호출해야 한다.


---

<br>

**[ 유니코드 샌드위치 ]**

유니코드 데이터를 인코딩하거나 디코딩하는 부분을 인터페이스의 가장 먼 경계지접에 위치시켜라.|
즉,  **가장 바깥(입력/출력 단계)에서만** 문자 인코딩/디코딩을 처리하라는 원칙을 비유적으로 “샌드위치”에 빗댄 것입니다.

1. **중간 로직은 ‘순수한 유니코드 문자열’만 다루도록** 만들어서 혼란을 줄일 수 있습니다.
2. **에러가 발생할 지점을 최소화**합니다.
3. **유지보수가 쉬워집니다.**

> ---
>
> **바깥쪽(인터페이스) 예시**
>
> - 파일 입출력(IO)
> - 네트워크 통신(HTTP, Socket 등)
> - 사용자 입력(키보드 입력, 콘솔 입력)
> - 데이터베이스 입출력(DB에서 가져오기/넣기)
>
> ---

```py
with open("data.txt", mode="r", encoding="utf-8") as f:
    text_data = f.read()  # 유니코드 문자열로 읽힘
```

```py
# 예시로 requests 라이브러리를 쓴다고 가정
import requests

# 네트워크에 보낼 때는 UTF-8로 인코딩해서 전송하는 경우가 많다.
response = requests.post("http://example.com/api",
                         data=processed_text.encode("utf-8"))
```

<br>

<br>

**[ 문자열 도우미 함수 사용 ]**

문자열에서 입력 값 일치여부를 확인할 수 있는 2가지 도우미 함수다.

```py
# 01 str반환 (bytes,str 매개변수 사용)

def to_str(bytes_or_str):
	if isinstance(bytes_or_str, bytes):
		value = bytes_or_str.decode('utf-8')
	else:
		value = bytes_or_str
	return value
```

```py
# 02 bytes반환 (bytes,str 매개변수 사용)

def to_bytes(bytes_or_str):
	if isinstance(bytes_or_str, str):
		value = bytes_or_str.encode('utf-8')
	else:
		value = bytes_or_str
	return value
```

<br>

<br>

#### **파이썬 문자열 사용 (주의점!)**

**1) 첫 번째, bytes와 str 호환 불가**

bytes와 str은 각각 인스턴스가 호환되지 않는다. 
이 때문에 전달 중인 문자 시퀀스가 어떤 타입인지를 항상 잘 알고 있어야 한다.

```py
print(b'one' + b'one')			# 연산 - 가능
print('one' + 'one')			# 연산 - 가능
print(b'one' + 'one')			# 연산 - 불가능(str과 bytes는 연산 불가)
```

```py
print(b'one' > b'two')			# 연산 - 가능
print('one' > 'two')			# 연산 - 가능
print(b'one' > 'two')			# 연산 - 불가능(str과 bytes는 연산 불가)
```

```py
print(b'red %s' % b'blue')		# 형식화 문자열 - 가능
print('red %s' % 'blue')		# 형식화 문자열 - 가능
------------------------
print(b'red %s' % 'blue')		# 형식화 문자열 - 불가능(Type Error 발생)
print('red %s' % b'blue')		# 형식화 문자열 - 이상 작동(red b'blue')
```

<br>

**2) 두 번째, 파일 핸들 기본 문자열** 

파일 핸들과 관련된 연사자들은 유니코드 문자열을 요구하지만 이진 바이트 문자열을 요구하지 않는다.
시스템의 디폴트 인코딩은 UTF-8이다. 

----

**[ bytes의 경우 ]**

```py
# wrong - TypeError

with open('data.bin', 'w') as f:
	f.write(b'\xf1\xf2\xf3\xf4\xf5)
```

```py
# correct - 'wb'모드 사용

with open('data.bin', 'wb') as f
	f.write(b'\xf1\xf2\xf3\xf4\xf5)
```

---

**[ str의 경우 ]**

```py
# wrong - UnicodeDecodeError

with open('data.bin', 'r') as f
	data = f.read()
```

```py
# correct - 'rb'모드 사용

with open('data.bin', 'rb') as f
	data = f.read()
```

---

**[ 그 외 ]**

```
with open('data.bin', 'r', encoding='cp1252') as f
	data = f.read()
```

<br>

<br>

<br>

<br>

## 04 C스타일 형식 대신 f-string 포맷형식을 사용하라

이 장에서는 C스타일 문자형식이 어떤식으로 변화했고, 어떤 제약과 문제가 발생했는지를 이야기 한다.
주로 안정성과 가독성 부분의 문제점들이다. 

레거시 코드들은 이런 방식을 사용하였고, 파이썬 3.6부터 추가된 interpolation(통칭 f-string)이 도입되면서 문제점을 대부분 해소하게 된다.
표현력, 간결성, 명확성 부분이 더 향상된 것이다.

<br>

<br>

<br>

<br>

## 05 복잡한 식을 대신 도우미 함수를 작성하라

식이 복잡해지면 더 작은 조각으로 나눠서 로직을 도우미 함수로 옮길지 고려해야 한다.

```py
from urllib.parse import parse_qs

my_values = parse_qs('빨강=5&파랑=0&초록=',
                     keep_blank_values=True)
print(repr(my_values))
```

```
{'빨강': ['5'], '파랑': ['0'], '초록': ['']}
```

> ---
>
> **[ `parse_qs` 함수의 동작 원리 ]**
>
> - ```
>   parse_qs(query_string, keep_blank_values=False, ...)
>   ```
>
>   - `query_string`: 예) `'빨강=5&파랑=0&초록='`
>   - `keep_blank_values`: `True`로 설정 시, **값이 비어 있는 파라미터**도 딕셔너리에 포함시켜서 **빈 문자열**을 값으로 둠
>   - 반환값: **딕셔너리**(`dict`), 키는 “파라미터 이름”, 값은 “파라미터 값들의 리스트”
>
> 즉, `parse_qs`는 `'&'`와 `'='`로 구분된 키-값 쌍을 찾고, 같은 키가 여러 번 등장할 수 있기 때문에 **값을 항상 리스트 형태**로 담아 돌려줍니다.
>
> ---

---

```py
# wrong - 가독성이 낮은 복잡한 수식(사용)

green = my_values.get('파랑', [''])[0] or 0
```

```py
# correct - 가독성이 높은 간단한 수식(사용)

green_str = my_values.get('초록', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
```

----

```py
# correct - 재사용을 위한 도우미 함수(사용)

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default
    
    green = get_first_int(my_values, '초록')
```

* 복잡한 식은 간단한 수식으로 만들어서 도우미 함수로 만들자
  * 반복해 사용할 가능성이 높거나 사용 예정인 함수들은 더욱 더 필요하다.
  * [참고] 불 연산자 or나 and를 식에 사용하는 것보다 if/else 식을 쓰는 편이 더 가독성이 좋다.









