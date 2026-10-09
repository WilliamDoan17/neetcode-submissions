class Solution:
    def isValid(self, s: str) -> bool:
        def isOpen(s: str) -> bool:
            return s == '(' or s == '[' or s == '{'
            
        def check(s1: str, s2: str) -> bool:
            if (s1 == '(' and s2 == ')'):
                return True
            elif (s1 == '[' and s2 == ']'):
                return True
            elif (s1 == '{' and s2 == '}'):
                return True
            return False 
        st = []

        for i in range(len(s)):
            if not isOpen(s[i]):
                if len(st) == 0:
                    return False
                else:
                    top = st[-1]
                    if check(top, s[i]):
                        st.pop()
                    else:
                        return False
            else: 
                st.append(s[i])
        
        return (len(st) == 0)
        
