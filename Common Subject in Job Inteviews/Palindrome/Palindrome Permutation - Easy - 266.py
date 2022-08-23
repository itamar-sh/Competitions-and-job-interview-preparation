def palindrome_permutation(word: str):
    chars_dict = {}
    for c in word:
        if c in chars_dict:
            chars_dict[c] += 1
        else:
            chars_dict[c] = 1
    even_chars = 0
    for val in chars_dict.values():
        if val % 2 != 0:
            even_chars += 1
    if len(word) %  2 == 0 and even_chars == 0:
        return True
    if len(word) %  2 != 0 and even_chars <= 1:
        return True
    return False

if __name__ == '__main__':
    assert(palindrome_permutation("abab"))
    assert(palindrome_permutation("aabab"))
    assert(palindrome_permutation("aaaaa"))
    assert(not palindrome_permutation("abcde"))
    assert(not palindrome_permutation("abcabb"))
    assert(palindrome_permutation("abcacb"))
