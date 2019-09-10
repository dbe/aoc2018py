def run(input):
    foo = input.strip().split('\n')
    print(sum(map(int, foo)))
