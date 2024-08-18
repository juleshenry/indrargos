import threading
import queue

class Motor:
        
    def __init__(self, MAX_CONCURRENT_CALLS = 8, function = None):
        self.MAX_CONCURRENT_CALLS = MAX_CONCURRENT_CALLS
        self.function = function

    def worker(self, queue):
        while 1:
            url = queue.get()
            if url is None:
                break
            self.function(url)
            queue.task_done()

    def multithread_function(self, urls):
        qu = queue.Queue()
        threads = []
        for _ in range(self.MAX_CONCURRENT_CALLS):
            thread = threading.Thread(target=worker, args=(qu,))
            thread.start()
            threads.append(thread)
        for url in urls:
            qu.put(url)
        # Wait for all commands to finish
        qu.join()
        # Stop worker threads
        for _ in range(self.MAX_CONCURRENT_CALLS):
            qu.put(None)
        for thread in threads:
            thread.join()

