#time complexity o(1)
#space complexity o(1)
class Solution:
    def numberToWords(self, num: int) -> str:
        thousands = ["", "Thousand", "Million", "Billion"]

        below_20 = [
            "Zero", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
            "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        
        if num == 0:
            return "Zero"
        result = []
        i = 0  # suffix index

        while num > 0:
            triplet = num % 1000
            if triplet != 0:
                result.insert(0, (self.magic(triplet).strip() + " " + thousands[i]).strip())
            num = num // 1000
            i += 1
        
        
        return " ".join(result).strip()

    def magic(self, curr: int) -> str:
        below_20 = [
            "Zero", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
            "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        if curr < 20:
            return below_20[curr]
        elif curr < 100:
            if curr % 10 == 0:
                return tens[curr // 10]
            else:
                return tens[curr // 10] + " " + self.magic(curr % 10)
        else:
            if curr % 100 == 0:
                return below_20[curr // 100] + " Hundred"
            else:
                return below_20[curr // 100] + " Hundred " + self.magic(curr % 100)
