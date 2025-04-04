import itertools
import time

def pretend_workload():
    for _ in itertools.count():
        sum(i**2 for i in range(10_000))
        if _ % 1_000 == 0:
            time.sleep(0.01)
if __name__ == "__main__":
    print("[*] Processing data stream...")
    pretend_workload()
