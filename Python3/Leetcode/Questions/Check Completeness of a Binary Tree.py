from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS solution using Queue - Time Complexity: O(n), Space Complexity: O(n)
class BFS:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q:
            curr = q.popleft()

            if curr:
                q.append(curr.left)
                q.append(curr.right)
            else:
                while q:
                    if q.popleft():
                        return False
        return True
