class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def toNum(s: str) -> int | None:
            try:
                return int(s)
            except:
                return None
        
        st = []

        def calculate(st: List[int], token: str) -> None:
            top = st[-1]
            st.pop()
            if token == '+':
                st[-1] = top + st[-1]
            elif token == '-':
                st[-1] = st[-1] - top
            elif token == '*':
                st[-1] = st[-1] * top
            elif token == '/':
                st[-1] = int(st[-1] / top)

        for i in range(len(tokens)):
            n = toNum(tokens[i])
            if not (n is None):
                st.append(n)
            else:
                calculate(st, tokens[i])

        return st[-1] 
                
