'''
    contextlib과 with
    파이썬의 with 문은 코드가 특별한 컨텍스트(context) 안에서 실행되는 경우를 표현한다
    정리: with 문 안에서만 해당 환경이 적용됨 나가면 자동 적용 해제
'''
import logging

def my_function():
    logging.debug('디버깅 데이터')
    logging.error('이 부분은 오류 로그')
    logging.debug('추가 디버깅 데이터')

# my_function() # default는 warring, error가 출력됨
from contextlib import contextmanager

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG):
    '''
        with은 debug 모드인가?
    '''
    print('* 내부:')
    my_function()

print('* 외부:')
my_function()


#아래있는게 더 좋은 표현이다 뭐 그런 내용 인 것 같음
with open('my_output.txt', 'w') as handle:
    handle.write('데이터입니다!')

@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

logging.basicConfig()

with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug(f'대상: {logger.name}!')
    logging.debug('이 메시지는 출력되지 않습니다')

logger = logging.getLogger('my-log')
logger.debug('디버그 메시지는 출력되지 않습니다')
logger.error('오류 메시지는 출력됩니다')

with log_level(logging.DEBUG, 'other-log') as logger:
    logger.debug(f'대상: {logger.name}!')
    logging.debug('이 메시지는 출력되지 않습니다')