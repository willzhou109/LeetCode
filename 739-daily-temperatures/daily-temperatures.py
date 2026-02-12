class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        daysUntilWarmer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if i == 0 or temperatures[i] <= temperatures[i - 1]:
                stack.append(i)
            else:
                j = len(stack) - 1
                while stack and temperatures[i] > temperatures[stack[j]]: # stack[j] represents an index
                    daysUntilWarmer[stack[j]] = i - stack[j]
                    stack.pop()
                    j -= 1
                stack.append(i)
        return daysUntilWarmer