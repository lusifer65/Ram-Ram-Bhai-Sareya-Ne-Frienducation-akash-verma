class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        ans=[]
		stack=[]
		
		for i in range(len(A)):
			if(len(stack)==0):
				stack.append(A[i])
				ans.append(-1)
			else:
				while(len(stack)>0 and stack[-1]>=A[i]):
					stack.pop()
				if(len(stack)==0):
					ans.append(-1)
					
				else:
					ans.append(stack[-1])
					
				stack.append(A[i])
		return ans
					
					