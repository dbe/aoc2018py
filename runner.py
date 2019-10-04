import importlib
import os
import requests
import sys

COOKIES = {
    'session':
    os.environ['AOCSESSION']
}

def main():
    run = importlib.import_module(f"{sys.argv[1]}.{sys.argv[2]}").run
    input = get_input().strip().split('\n')
    print(run(input))

def get_input():
    if(len(sys.argv) > 3):
        with open(sys.argv[3]) as f:
            return f.read()
    else:
        url = f"https://adventofcode.com/2018/day/{sys.argv[1]}/input"
        r = requests.get(url, cookies=COOKIES)
        return r.text

if(__name__ == '__main__'):
    main()
