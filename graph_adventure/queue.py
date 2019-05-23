class Queue:
    def __init__(self):
        self.storage = []
        self.size = 0

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None

    def length(self):
        return self.size