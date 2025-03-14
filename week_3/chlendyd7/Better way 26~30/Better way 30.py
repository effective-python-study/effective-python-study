def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = '컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어:전산기)는 진공관'
result = index_words(address)
print(result[:10])


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

# 이터레이터가 next 내장 함수를 호출할 때 마다 이터레이터는 제너레이터 함수를 다음 yield 식 까지 진행시킨다
# 제너레이터가 yield에 전달 하는 값은 이터레이터에 의해 호출하는 쪽에 반환
it = index_words_iter(address)
print(next(it))
print(next(it))
print(next(it))

result = list(index_words_iter(address))
print(result[:10])

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset