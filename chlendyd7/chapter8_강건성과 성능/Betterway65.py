def try_finally_example(filename):
    print("* 파일 열기")
    handle = open(filename, encoding="utf-8")  # oserror 발생 가능성
    try:
        print("* 데이터 읽기")
        return handle.read()
    finally:
        print("* close() 호출")
        handle.close()  # try 블록이 실행된 다음 항상 이 블록이 실행


filename = "random_data.txt"

with open(filename, "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")

# data = try_finally_example(filename)
# try_finally_example('does_not_exist.txt')

import json


def load_json_key(data, key):
    try:
        print("* json 데이터 읽기")
        result_dict = json.loads(data)  # Value Error ㅂ라생 가능성
    except ValueError as e:
        print(" * ValueError 처리")
        raise KeyError(key) from e
    else:
        print(" * 키 검색")
        return result_dict[key]


assert load_json_key('{"foo": "bar"}', "foo") == "bar"


# load_json_key('{"foo": bad payload', 'foo')

# load_json_key('{"foo": "bar"}', '존재하지 않음')

#
UNDEFINED = object()


def divide_json(path):
    """
    복합적인 문장 안에 모든 요소를 다 넣고 싶다면 
    try/except/else/finally를 사용하라. 예를 들어 수행할 작업에
    대한 설명을 파일에서 읽어 처리한 다음, 원본 파일 자체를 변경하고 싶다
    이 경우 try 블록을 사용해 파일을 읽고 처리하며,
    try 블록 안에서 발생할 것으로 예상되는 예외를 처리하고자 except 블록을 사용한다.
    
    정상적이면 try else finally
    계산이 잘못되면 try, except, finally
    json 데이터가 잘못되면 try 블록 실행, finally 블록 실행
    """
    print("* 파일 열기")
    handle = open(path, "r+")  # OSError가 발생할 수 있음
    try:
        print("* 데이터 읽기")
        data = handle.read()  # UnicodeDecodeError가 발생할 수 있음
        print("* JSON 데이터 읽기")
        op = json.loads(data)  # ValueError가 발생할 수 있음
        print("* 계산 수행")
        value = (
            op["numerator"] / op["denominator"]
        )  # ZeroDivisionError가 발생할 수 있음
    except ZeroDivisionError as e:
        print("* ZeroDivisionError 처리")
        return UNDEFINED
    else:
        print("* 계산 결과 쓰기")
        op["result"] = value
        result = json.dumps(op)
        handle.seek(0)  # OSError가 발생할 수 있음
        handle.write(result)  # OSError가 발생할 수 있음
        return value
    finally:
        print("* close() 호출")
        handle.close()  # 어떤 경우든 실행됨


temp_path = "random_data.json"

with open(temp_path, "w") as f:
    f.write('{"numerator": 1, "denominator": 10}')

assert divide_json(temp_path) == 0.1

#
# with open(temp_path, "w") as f:
#     f.write('{"numerator": 1, "denominator": 0}')

# assert divide_json(temp_path) is UNDEFINED

# #
# with open(temp_path, "w") as f:
#     f.write('{"numerator": 1 bad data')

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
# divide_json(temp_path)
