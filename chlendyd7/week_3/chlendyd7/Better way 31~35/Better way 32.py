value = [len(x) for x in open('my_file.txt')]
print(value)

'''
리스트 컴프리헨션으로 하려면 파일 각 줄의 길이를 메모리에 저장해야한다.
아주 크거나 네트워크 소켓이라면 사용하는 것이 문제 될 수 있다.
문제를 해결하기 위해 제너레이터 식을 제공(generator expression)

출력 시퀀스 전체가 실체화 되지는 않음. 대신 식에 들어있는 식으로부터 원소를 하나씩 만들어내는 이터레이터 생성?

'''

it = (len(x) for x in open('my_file.txt'))
print(it)
# <generator object <genexpr> at 0x0000023FC0F935E0> genrator obj

print(next(it))
print(next(it))

roots = ((x, x**0.5) for x in it)

print(next(roots))


'''
중간에 파일이 삭제되면 어떻게 될까?

파일이 중간에 삭제되면, 제너레이터가 파일을 순차적으로 읽고 있을 때 문제가 발생할 수 있습니다. 이유는 파일을 읽고 있는 동안, 그 파일이 시스템에서 삭제되면 더 이상 읽을 수 없기 때문입니다.

파일이 삭제되었을 때의 동작
파일을 읽는 도중에 파일이 삭제되면, open 함수로 파일을 읽을 수 없습니다. 구체적인 상황을 살펴보겠습니다.

제너레이터가 파일을 읽고 있을 때:

제너레이터는 open('my_file.txt')로 파일을 열고, 한 줄씩 읽어옵니다.
만약 파일이 삭제되면, **다음 줄을 읽으려고 할 때 FileNotFoundError**가 발생합니다.
open으로 파일을 열고 이터레이션 중:

open은 파일을 파일 객체로 반환하고, 그 객체에서 데이터를 읽는 과정이 파일 시스템과 연결됩니다.
만약 파일이 삭제되거나 접근할 수 없게 되면, 이터레이션을 계속할 수 없고, **FileNotFoundError**가 발생합니다.


쿼리셋의 경우 generator을 붙히면 i/o는 많아지지만 메모리적으로 관리 가능
'''