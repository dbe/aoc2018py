class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class CircularList:
    def __init__(self, values):
        if(len(values) == 0):
            raise "Can't initialze empty CircularList"

        self.tail = Node(values[0])
        self.tail.next = self.tail
        self.tail.prev = self.tail
        self.length = 1

        for value in values[1:]:
            self.append(value)


    def append(self, value):
        n = Node(value)
        n.next = self.tail.next
        n.prev = self.tail

        self.tail.next.prev = n
        self.tail.next = n
        self.tail = n

        self.length += 1

    def __getitem__(self, key):
        if(isinstance(key, slice)):
            if(key.start >= 0 or key.stop != None or key.step != None):
                raise Exception("Only have implemented negative range slices for problem 14")
            else:
                if(abs(key.start) > len(self)):
                    n = self.tail.next
                else:
                    n = self[key.start]

                a = []

                while(n != self.tail):
                    a.append(n.value)
                    n = n.next

                a.append(self.tail.value)

                return a
        else:
            if(key >= len(self) or (key < 0 and abs(key) > len(self))):
                raise KeyError(f"{key} is out of range")
            elif(key < 0):
                n = self.tail.next
                for i in range(abs(key)):
                    n = n.prev
            else:
                n = self.tail.next
                for i in range(key):
                    n = n.next

            return n


    def __len__(self):
        return self.length

    def __str__(self):
        #Head
        n = self.tail.next
        s = str(n.value)

        while(True):
            n = n.next
            s += str(n.value)
            if(n == self.tail):
                return s

def main():
    #Real pattern
    pattern = '702831'

    #Test pattern
    # pattern = '515891'


    board = CircularList([3,7])
    elf0 = board[0]
    elf1 = board[1]

    i = 0
    while(True):
        if(i % 1000000 == 0):
            print(i)
        #Appending to the board
        new = elf0.value + elf1.value
        for c in str(new):
            board.append(int(c))

        #Updating elves
        for _ in range(elf0.value + 1):
            elf0 = elf0.next

        for _ in range(elf1.value + 1):
            elf1 = elf1.next

        ending = ''.join(map(str, board[-7:]))
        if(pattern in ending):
            index = ending.index(pattern)
            return len(board) - 7 + index

        i += 1







    # c = CircularList([3,7,1,0])
    # a = [3,7,1,0]
    #
    # print(a[-7:])
    # print(c[-7:])
    #
    # print(a[-3:])
    # print(c[-3:])
    #
    # print(a[-0:])
    # print(c[-0:])
    # print(f"c: {c}")
    # print(f"a: {a}")
    # print(f"c[2]: {c[2]}")
    # print(f"a[2]: {a[2]}")
    # try:
    #     print(f"a[-5]: {a[-5]}")
    # except Exception as e:
    #     print(e)
    # try:
    #     print(f"c[-5]: {c[-5]}")
    # except Exception as e:
    #     print(e)
    # print(f"c[-1]: {c[-1]}")
    # print(f"a[-1]: {a[-1]}")
    # print(f"c.tail.next: {c.tail.next}")
    # print(f"c.tail.prev: {c.tail.prev}")
    # print(f"c.tail.prev.prev: {c.tail.prev.prev}")
    # print(f"c.tail.prev.prev.prev: {c.tail.prev.prev.prev}")
    # print(f"c.tail.prev.prev.prev.prev: {c.tail.prev.prev.prev.prev}")

if(__name__ == "__main__"):
    print(main())
