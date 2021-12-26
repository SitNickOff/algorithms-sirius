class Solution():
    def letterCombinations(self, digits):
        phone_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = ['']
        for digit in digits:
            current_combinations = list()
            for letter in phone_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations

test=Solution()
print(test.letterCombinations('52'))