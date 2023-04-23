class Solution:
    r2iMap = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}

    groups = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        if len(s) == 1:
            return self.r2iMap[s]

        s2int = 0
        c1 = None
        for i, c in enumerate(s[::-1]):
            if c1:
                if c + c1 in self.groups:
                    s2int += self.groups[c + c1]
                    c1 = None
                else:
                    s2int += self.r2iMap[c1]
                    c1 = c if c in ['V', 'X', 'L', 'C', 'D', 'M'] else None
            elif c in ['V', 'X', 'L', 'C', 'D', 'M']:
                c1 = c
                continue
            else:
                s2int += self.r2iMap[c]

        if c1:
            s2int += self.r2iMap[c1]

        return s2int


if __name__ == '__main__':
    roman = 'LVIII'
    sol = Solution()
    convInt = sol.romanToInt(roman)
    print(convInt)