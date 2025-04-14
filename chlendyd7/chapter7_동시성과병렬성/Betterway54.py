import threading


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        temp = self.count
        temp += offset
        self.count = temp


def worker(counter, how_many):
    for _ in range(how_many):
        counter.increment(1)


how_many = 10**6
counter = Counter()

threads = []
for _ in range(5):
    t = threading.Thread(target=worker, args=(counter, how_many))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Expected:", how_many * 5)
print("Found   :", counter.count)


from threading import Thread
import select
import socket

from threading import Lock


class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # 센서를 읽는다
        counter.increment(1)


from threading import Thread

how_many = 10**5
counter = LockingCounter()

threads = []
for i in range(5):
    thread = Thread(target=worker, args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f"카운터 값은 {expected}여야 하는데, 실제로는 {found} 입니다")
