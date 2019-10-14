class Node:
    def __init__(self, value, priority):
        self.v = value
        self.p = priority

    def __repr__(self):
        return f"({self.v} - Priority: {self.p})"

class PriorityQueue:
    def __init__(self):
        self.data = []

    def add(self, value, priority):
        self.data.append(Node(value, priority))
        self._bubble_up(len(self.data) - 1)

    def peek(self):
        return self.data[0].v if len(self.data) > 0 else None

    def pop(self):
        pass

    def _bubble_up(self, i):
        while(i > 0):
            p = self._parent(i)

            if(self.data[i].p < self.data[p].p):
                self._swap(i, p)
                i = p
            else:
                return


    def _parent(self, i):
        return int((i - 1) / 2)

    def _swap(self, a, b):
        temp = self.data[a]
        self.data[a] = self.data[b]
        self.data[b] = temp

    def __repr__(self):
        return str(self.data)

if(__name__ == "__main__"):
    def add_and_print(p, word):
        p.add(word, len(word))
        print(f"p: {p}")

    p = PriorityQueue()
    print(f"p.peek(): {p.peek()}")
    add_and_print(p, "oreo")
    print(f"p.peek(): {p.peek()}")
    add_and_print(p, "foo")
    print(f"p.peek(): {p.peek()}")
    add_and_print(p, "omglotsofstuff")
    print(f"p.peek(): {p.peek()}")
    add_and_print(p, "ok")
    print(f"p.peek(): {p.peek()}")
    add_and_print(p, "nopers")
    print(f"p.peek(): {p.peek()}")
    add_and_print(p, "a")
    print(f"p.peek(): {p.peek()}")
