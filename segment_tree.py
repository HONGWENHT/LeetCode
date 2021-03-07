class SegmentTree:
    def __init__(self, arr):
        self.tree = [0] * (4 * len(arr))
        self.arr = arr

    def buildSegTree(self, arr, treeIndex, lo, hi):
        if lo == hi:
            self.tree[treeIndex] = arr[lo]
            return

        mid = (lo + hi) // 2
        self.buildSegTree(arr, 2 * treeIndex + 1, lo, mid)
        self.buildSegTree(arr, 2 * treeIndex + 2, mid + 1, hi)

        self.tree[treeIndex] = self.tree[2 * treeIndex + 1] + self.tree[2 * treeIndex + 2]

    def query(self, treeIndex, lo, hi, i, j):
        if j < lo or i > hi :
            return 0

        if i >= lo and j <= hi:
            return self.tree[treeIndex]

        mid = (lo + hi) // 2

        if i > mid :
            return self.query(2 * treeIndex + 2, mid + 1, hi, i, j)
        elif j <= mid:
            return self.query(2 * treeIndex + 1, lo, mid, i , j)

        return self.query(2 * treeIndex + 1, lo, mid, i, mid) + self.query(2 * treeIndex + 2, mid + 1, hi, mid + 1, j)

    def updateTree(self, treeIndex, lo, hi, arrIndex, val):
        if lo == hi:
            self.tree[treeIndex] = val
            return

        mid = (lo + hi) // 2

        if arrIndex > mid:
            self.updateTree(2 * treeIndex + 2, mid + 1, hi, arrIndex, val)
        elif arrIndex <= mid :
            self.updateTree(2 * treeIndex + 1, lo, mid, arrIndex, val)
        self.tree[treeIndex] = self.tree[2 * treeIndex + 1] + self.tree[2 * treeIndex + 2]
