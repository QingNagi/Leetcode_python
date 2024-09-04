# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.distance, self.res = deque(), deque()
        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            temp = abs(target - root.val)
            if len(self.res) < k:
                if not self.distance:
                    self.distance.append(temp)
                    self.res.append(root.val)
                elif self.distance[-1] >= temp:
                    self.distance.append(temp)
                    self.res.append(root.val)
                elif self.distance[0] <= temp:
                    self.distance.appendleft(temp)
                    self.res.appendleft(root.val)
                else: 
                    for i in range(len(self.res)-1):
                        if self.distance[i] <= temp:
                            break
                    self.distance.insert(i, temp)
                    self.res.insert(i, root.val)
            else:
                if self.distance[-1] >= temp:
                    self.distance.popleft()
                    self.res.popleft()                    
                    self.distance.append(temp)
                    self.res.append(root.val)
                elif self.distance[0] >= temp: 
                    for i in range(len(self.res)-1):
                        if self.distance[i] <= temp:
                            break
                    self.distance.popleft()
                    self.res.popleft()  
                    self.distance.insert(i-1, temp)
                    self.res.insert(i-1, root.val)
        dfs(root)
        return list(self.res)