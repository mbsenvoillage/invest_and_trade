import time


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        print('%r  %2.2f ms' % (method.__name__, (end - start) * 1000))
        return result
    return timed