class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carInf = [(position[i], speed[i]) for i in range(len(speed))]
        carInf.sort()
        def isCatchingUp(i: int, j: int) -> bool:
            """whether i-th car is catching up with j-th car""" 
            return  ((target - carInf[i][0]) / carInf[i][1]) <= (target - carInf[j][0]) / carInf[j][1]
        
        st = []

        for i in range(len(position) - 1, -1, -1):
            if len(st) != 0 and isCatchingUp(i, st[-1]):
                continue
            st.append(i)
        
        return len(st)
