import importlib
import os
import requests
import sys

COOKIES = {
    'session':
    os.environ['AOCSESSION']
}

run = importlib.import_module(f"{sys.argv[1]}.{sys.argv[2]}").run

url = f"https://adventofcode.com/2018/day/{sys.argv[1]}/input"
r = requests.get(url, cookies=COOKIES)
print(run(r.text.strip().split('\n')))
