"""info."""

import time

import tqdm

a = [x**2 for x in range(10)]


for item in tqdm.tqdm(a):
    time.sleep(0.1)


s = "too long lineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"

print(s)
