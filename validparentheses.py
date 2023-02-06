class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack= []
        closeToOpen = {")": "(", "]" : "[", "}" : "{"}

        for i in s:
            #check if the first input is a closing parenthese
            if i in closeToOpen:
                #check if the stack is empty and checking if the last item in the stack matches the same type of open parenthese
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                #dont match or stack empty return false
                else:
                    return False
            else:
                stack.append(i)
        #returning true if the stack is empty
        return True if not stack else False