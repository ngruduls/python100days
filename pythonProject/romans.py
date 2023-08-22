class Solution:
    def romanToInt(s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IX": 9,
            "IV": 4,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        sum = 0
        i = len(s) - 1
        while i >= 0:
            current = s[i]
            if i > 0:
                prev = s[i - 1]
            else:
                prev = ""
            # two-sum
            if dict.get(prev + current) is not None:
                sum += dict.get(prev + current)
                i -= 2
            else:
                sum += dict.get(current)
                i -= 1
        return sum


print(Solution.romanToInt("MCDXC"))
