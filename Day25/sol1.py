class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,ans):
            if(root==None):
                return 
            ans.append(root.val)
            helper(root.left,ans)
            helper(root.right,ans)
        ans=[]
        helper(root,ans)
        return ans