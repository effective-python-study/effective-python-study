from unittest import TestCase, main

# unittest 프레임워크는 setUpModule과 tearDownModule이라는 이름의 함수를 자동으로 찾아서 실행합니다.
"""
    작동 방식:
    setUpModule(): 테스트 모듈에서 가장 먼저, 어떤 테스트 케이스도 실행되기 전에 딱 한 번 호출됩니다.
    tearDownModule(): 테스트 모듈의 모든 테스트 케이스가 실행된 후, 마지막으로 딱 한 번 호출됩니다.
"""


def setUpModule():
    print("* 모듈 설정")


def tearDownModule():
    print("* 모듈 정리")


class IntegrationTest(TestCase):
    def setUp(self):
        print("* 테스트 설정")

    def tearDown(self):
        print("* 테스트 정리")

    def test_end_to_end1(self):
        print("* 테스트 1")

    def test_end_to_end2(self):
        print("* 테스트 2")


if __name__ == "__main__":
    main()
