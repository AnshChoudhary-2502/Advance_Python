import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    print(f"Thread func({seconds}) starting")
    time.sleep(seconds)
    print(f"Thread func({seconds}) finished after {seconds} seconds")
# time1 = time.perf_counter()
#normal code
# func(4)
# func(6)
# func(2)
# time2 = time.perf_counter()
# print(f"Normal code finished in {time2 - time1} seconds")

#using threading
# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[6])
# t3 = threading.Thread(target=func, args=[2])
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# time2 = time.perf_counter()
# print(f"Threading code finished in {time2 - time1} seconds")

#using ThreadPoolExecutor
def poolingDemo():
    with ThreadPoolExecutor(max_workers=3) as executor:                    # max_workers define the no. of threads run at one time
        # sleep1 = executor.submit(func, 4)
        # sleep2 = executor.submit(func, 6)
        # sleep3 = executor.submit(func, 2)
        # print(sleep1.result)
        # print(sleep2.result)
        # print(sleep3.result)
        l = [4,6,2]
        results = executor.map(func, l)                                    # .map is used when there is list of tasks
        for result in results:
            print(result)
poolingDemo()