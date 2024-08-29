import threading
import queue


class MotorMonoFunction:

    def __init__(self, MAX_CONCURRENT_CALLS=8, function=None):
        self.MAX_CONCURRENT_CALLS = MAX_CONCURRENT_CALLS
        self.function = function
        self.results = []

    def worker(self, queue):
        while 1:
            args = queue.get()
            if not args:
                break
            self.results.extend(self.function(*args))
            queue.task_done()

    def multithread_function(self, args_list):
        qu = queue.Queue()
        threads = []
        for _ in range(self.MAX_CONCURRENT_CALLS):
            thread = threading.Thread(target=self.worker, args=(qu,))
            thread.start()
            threads.append(thread)
        for args in args_list:
            qu.put(args)
        qu.join()
        for _ in range(self.MAX_CONCURRENT_CALLS):
            qu.put(None)
        for thread in threads:
            thread.join()
        return self.results


if __name__ == "__main__":
    MotorMonoFunction(function=lambda x, y: print(x * y)).multithread_function(
        [
            (
                o,
                o,
            )
            for o in range(10)
        ]
    )
