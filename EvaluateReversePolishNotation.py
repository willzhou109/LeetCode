class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
       
        for entry in tokens:
            if len(stack) > 1:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
            if entry == "+":
                stack.append(int(val2 + val1))
            elif entry == "-":
                stack.append(int(val2 - val1))
            elif entry == "*":
                stack.append(int(val2 * val1))
            elif entry == "/":
                stack.append(int(float(val2) / val1))
            else:
                stack.append(int(entry))
        return stack[-1]
