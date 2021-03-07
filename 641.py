class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.arr = [None] * k
        self.num = 0
        self.head = self.tail = None

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.head:
            self.head = self.tail = 0
        else:
            new = (self.head - 1) % self.size
            if new == self.tail:
                return False
            self.head = new
        self.arr[self.head] = value
        self.num += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.tail:
            self.tail = self.head = 0
        else:
            new = (self.tail + 1) % self.size
            if new == self.head:
                return False
            self.tail = new
        self.arr[self.tail] = value
        self.num += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.head:
            return False
        self.arr[self.head] = None
        self.num -= 1
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.head = (self.head + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.tail:
            return False
        self.arr[self.tail] = None
        self.num -= 1
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.tail = (self.tail - 1) % self.size
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.head:
            return -1
        return self.arr[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.tail:
            return -1
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.head is None

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.num == self.size

s = MyCircularDeque(3)
print(s.insertLast(1))
print(s.insertLast(2))
print(s.insertFront(3))
print(s.insertFront(4))