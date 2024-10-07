class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass
   
        valid_brack = [('{', '}'), ('(', ')'), ('[', ']')]
        stack = []
        for c in s:
            if len(stack)>0 and (stack[-1], c) in valid_brack:
                stack.pop()
            else:
                stack.append(c)
        return len(stack)==0






    



  

