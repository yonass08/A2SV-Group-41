class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        if s == '0':
            return 0
        num, last, res, op, = 0, 0, 0, '+' 
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ' ) or i == n-1:
                if op == '+' or op == '-':
                    res += last
                    last = num if op == '+' else -num
                elif op == '*':
                    last *= num
                elif op == '/':
                    quo = last // num
                    if quo < 0 and quo * num != last:
                        quo += 1
                    last = quo

                op = ch
                num = 0
        res += last
        return res