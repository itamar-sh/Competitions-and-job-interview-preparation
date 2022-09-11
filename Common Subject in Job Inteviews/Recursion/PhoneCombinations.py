import itertools


class Solution:
    digits_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                         "9": "wxyz"}

    def _letterCombinationHelper(self, digits: str, index: int = 0, result=[], cur_path=[]) -> List[str]:
        if index == len(digits):
            result.append(''.join(cur_path))
        else:
            for letter in Solution.digits_to_letters[digits[index]]:
                new_path = cur_path[:]
                new_path.append(letter)
                self._letterCombinationHelper(digits, index + 1, result, new_path)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        result = []
        self._letterCombinationHelper(digits, result=result)
        return result


    def letterCombinationsProduct(self, digits):
        """
        change digits to all letters combinations.
        Pruduct solution
        :param digits:
        :return:
        """
        b = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return [] if digits == "" else ["".join(x) for x in itertools.product(*(b[d] for d in digits if d in b))]

