class RomanConverter:
    def __init__(self):
        self.num = int(input("Enter an integer: "))

    def to_roman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman = ""
        n = self.num
        for i in range(len(val)):
            while n >= val[i]:
                roman += syms[i]
                n -= val[i]
        return roman

r = RomanConverter()
print(r.to_roman())
