    #!/usr/bin/env python3.8
from unittest import TestCase, main
from utils import to_str

'''
    이거까지 필요한가?
'''
class UtilsErrorTestCase(TestCase):
    def test_to_str_bad(self):
        with self.assertRaises(TypeError):
            to_str(object())

    def test_to_str_bad_encoding(self):
        with self.assertRaises(UnicodeDecodeError):
            to_str(b'\xfa\xfa')

if __name__ == '__main__':
    main()

'''
    with 문을 사용하는 이유 try catch보다 더 짧음
    이는 테스트가 예상치 못한 상황에서 멈추거나, 리소스 누수를 일으키는 것을 방지합니다
    def test_to_str_bad(self):
    try:
        to_str(object())
        self.fail("TypeError was not raised") # 예외가 발생하지 않으면 테스트 실패
    except TypeError:
        pass # TypeError가 발생하면 통과
    except Exception as e:
        self.fail(f"Unexpected exception {type(e).__name__} was raised") # 다른 예외가 발생하면 실패
'''