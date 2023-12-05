# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur_node = root
        answer = None
        cnt = 0
        while cur_node:
            #if cnt += 1:
                #break
            print(cur_node.val)
            if cur_node.val == val:
                answer = cur_node
                break
            elif cur_node.val > val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
            # 1. cur_node.val과 val이 같다면 answer에 cur_node를 지정하고 break
            # 2. cur_node.val이 val보다 작다면, answer에 cur_node.left를 지정
            # 3. cur_node.val이 val보다 크다면, answer에 cur_node.right를 지정
        return answer
        