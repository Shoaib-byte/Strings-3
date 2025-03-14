#time complexity o(n)
#space complexity o(n)
class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        st = []
        lastSign = '+'
        num = 0
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            elif s[i] == '(':
                if lastSign == '+':
                    st.append(1)
                else:
                    st.append(-1)
                st.append(float('inf'))
                num = 0
                lastSign = '+'
            elif s[i] == ')':
                if lastSign == '+':
                    st.append(num)
                else:
                    st.append(-num)
                inter = 0
                while st[-1] != float('inf'):
                    inter += st.pop()
                st.pop()
                popped = st.pop()
                inter = inter * popped
                st.append(inter)

                num = 0
                lastSign = '+'
            elif not s[i].isdigit() and s[i] != ' ':
                if lastSign == '+':
                    st.append(num)
                else:
                    st.append(-num)
                num = 0
                lastSign = s[i]

        calc = 0
        if s[n-1] != ')':
            if lastSign == '+':
                st.append(num)
            else:
                st.append(-num)

        while st:
            calc += st.pop()
        
        return calc





        