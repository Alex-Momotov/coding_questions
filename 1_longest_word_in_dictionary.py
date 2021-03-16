

"""
Leetcode: Longest Word in Dictionary

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order.

Example 1:
Input:  words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
"""


def longest_word(words):
    s = set(words)
    candidates = []
    for word in words:
        cand = True
        for sub_w in sub_words(word):
            if sub_w not in s:
                cand = False
                continue
        if cand:
            candidates.append(word)

    max_len = len(max(candidates, key=lambda w: len(w)))

    max_candidates = [cand for cand in candidates if len(cand) == max_len]

    return min(max_candidates)


def sub_words(word):
    return [word[:i] for i in range(1, len(word))]

sub_words("w")
sub_words("wo")

longest_word(["w","wo","wor","worl", "world"])
longest_word(["a", "banana", "app", "appl", "ap", "apply", "apple"])
