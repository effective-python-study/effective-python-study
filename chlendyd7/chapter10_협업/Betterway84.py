def palindrom(word):
    '''주어진 단어가 회문인 경우 True를 반환한다'''
    return word == word[::-1]

assert palindrom('tacocat')
assert not palindrom('banana')

print(repr(palindrom.__doc__))
