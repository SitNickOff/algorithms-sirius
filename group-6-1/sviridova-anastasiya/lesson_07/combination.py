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
            for combination in all_combinations:
                for letter in phone_digit[digit]:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations

def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')



iphone = Solution()
test(iphone.letterCombinations('23'), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
test(iphone.letterCombinations('92'), ['wa', 'wb', 'wc', 'xa', 'xb', 'xc', 'ya', 'yb', 'yc', 'za', 'zb', 'zc'])
