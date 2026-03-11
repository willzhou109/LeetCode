from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        output = []
        q = deque()
        q.append(deque([root]))
        output.append([root.val])
        while q:
            subarray_output = []
            subarray_queue = deque() # queue within a queue
            while len(q[0]) > 0:
                if q[0][0].left:
                    subarray_queue.append(q[0][0].left)
                    subarray_output.append(q[0][0].left.val)
                if q[0][0].right:
                    subarray_queue.append(q[0][0].right)
                    subarray_output.append(q[0][0].right.val)
                q[0].popleft()
            q.popleft()
            if len(subarray_queue) > 0:
                q.append(subarray_queue)
            if len(subarray_output) > 0:
                output.append(subarray_output)
       
        return output