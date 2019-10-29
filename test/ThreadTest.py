from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request
from random import randint
from time import sleep
 
URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/']
 
# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

if __name__ == "__main__":
    pool = ThreadPoolExecutor(1)
    fs = []
    for url in URLS:
        fs.append(pool.submit(load_url, url, 60))

    r = randint(1,5)
    print ("Changing max_workers to: {}".format(r))
    pool._max_workers = r
    print ("Current queue size: {}. Number of threads in parallel: {}".format(pool._work_queue.qsize(), len(pool._threads)))

    for f in as_completed(fs):
        r = randint(1,5)
        print ("Changing max_workers to: {}".format(r))
        pool._max_workers = r
        print ("Current queue size: {}. Number of threads in parallel: {}".format(pool._work_queue.qsize(), len(pool._threads)))

        try:
            data = f.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('Page is %d bytes' % (len(data)))

    print ("done")