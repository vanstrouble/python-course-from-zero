from typing_extensions import Self


class Solution(object):
    def romanToInt(self, s) -> int:
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        for index, number in enumerate(s):
            if (index < len(s) - 1 and numerals[number] < numerals[s[index + 1]]):
                total -= numerals[number]
            else:
                total += numerals[number]

        return total


if __name__ == '__main__':
    number = input('Input: ')
    answer = Self.romanToInt(s=number)
    print(answer)
