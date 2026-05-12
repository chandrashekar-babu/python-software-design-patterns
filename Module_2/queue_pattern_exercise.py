from collections import deque

class Queue:
    def __init__(self, *args, **kwargs):
        self.queue = deque(*args, **kwargs)

    # TODO: Implement the '>>' operator to enqueue an element to the queue
    
    # TODO: Implement the '<<' operator to dequeue an element from the queue

    def __str__(self):
        return f"Queue({list(self.queue)})"

if __name__ == '__main__':
    q = Queue()
    2 >> q  # Enqueue element [2]
    3 >> q  # [3, 2]
    4 >> q  # [4, 3, 2]

    q << 10 # Enqueue element 10 [4, 3, 2, 10]
    q << 11 # [4, 3, 2, 10, 11]
    q << 12 # [4, 3, 2, 10, 11, 12]

    r = Queue()
    q >> r # Dequeue element from q and enqueue to r [12], q=[4, 3, 2, 10, 11]
    q >> r # [11, 12], q=[4, 3, 2, 10]
    q >> r # [10, 11, 12], q=[4, 3, 2]

    print(q)
    print(r)


