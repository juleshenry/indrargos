import threading
import queue
from indrargos import Indrargos

MAX_CONCURRENT_CALLS = 8

def worker(queue):
    while 1:
        url = queue.get()
        if url is None:
            break
        Indrargos.see(url)
        queue.task_done()

def multi_scrape(urls):
    qu = queue.Queue()
    threads = []
    for _ in range(MAX_CONCURRENT_CALLS):
        thread = threading.Thread(target=worker, args=(qu,))
        thread.start()
        threads.append(thread)
    for url in urls:
        qu.put(url)
    # Wait for all commands to finish
    qu.join()
    # Stop worker threads
    for _ in range(MAX_CONCURRENT_CALLS):
        qu.put(None)
    for thread in threads:
        thread.join()

