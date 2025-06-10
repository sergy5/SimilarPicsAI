"""info."""

import time

import tqdm

a = [x**2 for x in range(10)]


for _ in tqdm.tqdm(a):
    time.sleep(0.1)


s = "too long lineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"

print(s)
