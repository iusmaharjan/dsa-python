class DualStack:

    def __init__(self, size = 10):
        if size <= 0:
            raise ValueError("size must be positive")
        self.items = list()
        for i in range(size):
            self.items.append(0)
        self.stack1_top = -1 
        self.stack2_top = size

    def size(self):
        return len(self.items)

    def stack1_is_empty(self):
        return self.stack1_top == -1 

    def stack2_is_empty(self):
        return self.stack2_top == len(self.items)

    def stack1_push(self, x):
        if (self.stack1_top + 1 == self.stack2_top):
            raise RuntimeError("stack overflow")
        self.stack1_top = self.stack1_top + 1
        self.items[self.stack1_top] = x
        return self.stack1_top

    def stack2_push(self, x):
        if (self.stack2_top - 1 == self.stack1_top):
            raise RuntimeError("stack overflow")
        self.stack2_top = self.stack2_top - 1
        self.items[self.stack2_top] = x 
        return self.stack2_top

    def stack1_pop(self):
        if (self.stack1_is_empty()):
            raise RuntimeError("stack underflow")
        self.stack1_top = self.stack1_top - 1
        return self.items[self.stack1_top + 1]

    def stack2_pop(self):
        if (self.stack2_is_empty()):
            raise RuntimeError("stack underflow")
        self.stack2_top = self.stack2_top + 1
        return self.items[self.stack2_top - 1]
