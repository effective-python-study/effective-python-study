import threading
import time
from threading import Lock


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        temp = self.count
        time.sleep(0.000001)  # 아주 짧은 슬립 추가
        temp += offset
        self.count = temp


class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            temp = self.count
            time.sleep(0.000001)  # 🔥 슬립 추가로 타이밍 실험
            temp += offset
            self.count = temp


def worker(counter, how_many):
    for _ in range(how_many):
        counter.increment(1)


def test_counter(counter_class, how_many=10**5, thread_count=5):
    counter = counter_class()
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(counter, how_many))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    expected = how_many * thread_count
    print(f"[{counter_class.__name__}] Expected: {expected} | Found: {counter.count}")


# 테스트 실행
test_counter(Counter)
test_counter(LockingCounter)
