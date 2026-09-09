class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        # result[0,0,0,0...]
        for i in range(len(temperatures)):
            result.append(0)

        for i in range(len(temperatures)):
            # current day is > prior day, record days difference in result
            while stack and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop() 

            # add index to stack
            stack.append(i)

        return result
            

        