"""The Longest Palindromic - https://checkio.org/mission/the-longest-palindromic/"""


def longest_palindromic(text):
    if is_palindrom(text):
        return text
    sub = ''
    length_of_input = len(text)
    lin = length_of_input - 1

    while lin > 0:
        for c in range(lin):
            if c + lin <= length_of_input:
                sub = text[c:c + lin]

            if is_palindrom(sub):
                lin = 0
                break
        lin -= 1
    return sub


def is_palindrom(text):
    return text == text[::-1]


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"

    # TODO find recursive solution! to learn the freaking recursion
