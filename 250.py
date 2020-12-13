class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: return 0
        self.count = 0
        self.helper(root)
        return self.count

    def helper(self, root: TreeNode):
        if not root.left and not root.right:
            self.count += 1
            print(self.count)
            return True
        isTrue = True

        if root.left:
            isTrue = isTrue and self.helper(root.left) and root.left.val == root.val
        if root.right:
            isTrue = isTrue and self.helper(root.right) and root.right.val == root.val

        self.count += isTrue
        print(self.count)
        return isTrue

    def list_to_tree(self, ls):
        if not ls:
            return TreeNode(None)
        i = 0
        root = TreeNode(ls[i])
        tmp_queue = [root]
        while tmp_queue:
            i += 1
            node = tmp_queue.pop()
            if not node.val:
                continue

            if 2 * i - 1 >= len(ls):
                return root
            node.left = TreeNode(ls[2 * i - 1])
            tmp_queue.append(node.left)

            if 2 * i >= len(ls):
                return root
            node.right = TreeNode(ls[2 * i])
            tmp_queue.append(node.right)
        return root

s = Solution()
s.countUnivalSubtrees(s.list_to_tree([5,1,5,5,5,None,5]))