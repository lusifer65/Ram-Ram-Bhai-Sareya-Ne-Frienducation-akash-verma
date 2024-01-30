class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return None
        q=[(root,0)]
        h={}
        while(len(q)>0):
            if(q[0][1] in h):
                h[q[0][1]].append(q[0][0].val)
            else:
                h[q[0][1]]=([q[0][0].val])
            if(q[0][0].left!=None):
                q.append((q[0][0].left,q[0][1]+1))
            if(q[0][0].right!=None):
                q.append((q[0][0].right,q[0][1]+1))
            q.pop(0)

        return list(h.values())