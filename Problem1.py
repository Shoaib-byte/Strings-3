#time complexity o(m)
#space complexity o(1)
class Solution:
    def calculate(self, s: str) -> int:
        currNum = 0
        calc = 0
        tail = 0
        lastSign = '+'
        result = 0
        m = len(s)
        for i in range(m):
            if s[i].isdigit():
                currNum = currNum * 10 + (ord(s[i]) - ord('0'))
            if (not s[i].isdigit() and s[i] != ' ') or i == m - 1:
                if lastSign == '+':
                   calc += currNum
                   tail = +currNum

                elif lastSign == '-':
                    calc -= currNum
                    tail = -currNum

                elif lastSign == '*':
                    calc = calc - tail + tail * currNum
                    tail = tail * currNum
                elif lastSign == '/':
                    calc = calc - tail + int(tail / currNum)
                    tail = int(tail / currNum)
                
                currNum = 0
                lastSign = s[i]
                
        
        return calc

        