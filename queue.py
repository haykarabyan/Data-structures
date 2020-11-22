class Queue:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def enqueue(self, e):
        self.data.insert(0,e)

    def dequeue(self):
        return self.data.pop()

    def size(self):
        return len(self.data)
