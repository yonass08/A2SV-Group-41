class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_comp = tuple(map(int,num1[:-1].split('+')))
        num2_comp = tuple(map(int,num2[:-1].split('+')))

        real_part = num1_comp[0] * num2_comp[0] - num1_comp[1] * num2_comp[1]
        imaginary_part = num1_comp[0] * num2_comp[1] + num1_comp[1] * num2_comp[0]

        return f"{real_part}+{imaginary_part}i"
