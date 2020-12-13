class DLNode:
    def __init__(self):
        self.val = 0
        self.pre = None
        self.next = None
        self.key = 0


class LRUCache:
    def add(self, node: DLNode):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def delete(self, node: DLNode):
        pre = node.pre
        nex = node.next
        pre.next = nex
        nex.pre = pre

    def pop(self):
        ret = self.tail.pre.key
        self.delete(self.tail.pre)
        return ret

    def moveToHead(self, node: DLNode):
        self.delete(node)
        self.add(node)

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLNode(), DLNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        node = self.cache[key]
        if not node:
            return -1
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLNode()
            node.key = key
            node.val = value
            self.cache[key] = node
            self.add(node)
            self.size += 1
            if self.size > self.capacity:
                tail_key = self.pop()
                del self.cache[tail_key]
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)



test = LRUCache(2)
test.put(1,1)
test.put(2,2)
test.get(1)