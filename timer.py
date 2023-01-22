"""A cool little timer"""
from time import perf_counter

class Timer:
    def __enter__(self):
        self.start = perf_counter(); self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = perf_counter()

with Timer() as timer:
    input('Tell me when...')
print(timer())