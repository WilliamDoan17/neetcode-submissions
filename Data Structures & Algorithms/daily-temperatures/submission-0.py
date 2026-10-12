class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while len(st) > 0 and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            if len(st) == 0: 
                result[i] = 0 
            else:
                result[i] = st[-1] - i
            st.append(i)
        
        return result
