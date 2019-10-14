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
        ret = self.data[0].v
        self.data[0] = self.data[len(self.data) - 1]
        self.data.pop()
        self._bubble_down(0)
        return ret

    def __len__(self):
        return len(self.data)

    def _bubble_down(self, i):
        #If not child
        if(i * 2 + 1 < len(self.data)):
            smaller = self._smaller_child(i)
            self._swap(i, smaller)
            self._bubble_down(smaller)

    def _smaller_child(self, i):
        if(i * 2 + 2 >= len(self.data)):
            return i * 2 + 1
        else:
            if(self.data[i * 2 + 1].p < self.data[i * 2 + 2].p):
                return i * 2 + 1
            else:
                return i * 2 + 2


    def _bubble_up(self, i):
        if(i > 0):
            p = self._parent(i)
            if(self.data[i].p < self.data[p].p):
                self._swap(i, p)
                self._bubble_up(p)

    def _is_child_node(self, i):
        pass

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

    while(len(p) > 0):
        print(f"p: {p}")
        print(f"p.pop(): {p.pop()}")
