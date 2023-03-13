class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        res = []

        if num >= 1000000000:
            res += self.convert_three(num // 1000000000)+ ['Billion']
            num %= 1000000000

        if num >= 1000000:
            res += self.convert_three(num // 1000000) + ['Million']
            num %= 1000000
        
        if num >= 1000:
            res += self.convert_three(num // 1000) + ['Thousand']
            num %= 1000

        res += self.convert_three(num)
        return (' '.join(res)).strip()

    def convert_three(self, num):
        word_map = [
                    ('', ), 
                    ('One', 'Eleven'),
                    ('Two', 'Twelve', 'Twenty'),
                    ('Three', 'Thirteen', 'Thirty'),
                    ('Four', 'Fourteen', 'Forty'),
                    ('Five', 'Fifteen', 'Fifty'),
                    ('Six', 'Sixteen', 'Sixty'),
                    ('Seven', 'Seventeen', 'Seventy'), 
                    ('Eight', 'Eighteen', 'Eighty'),
                    ('Nine', 'Nineteen', 'Ninety'),
                    ('Ten', )
                    ]

        res = []
        if num > 99:
            res += [word_map[num // 100][0], 'Hundred']
        
        num %= 100
        if num > 19:
            res += [word_map[num // 10][2]]
            res += [word_map[num % 10][0]]
        elif num > 10:
            res += [word_map[num % 10][1]]
        else:
            res += [word_map[num][0]]

        return (' '.join(res)).strip().split()
        
