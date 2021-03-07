import collections
from functools import reduce
from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            reduce(dict.__getitem__, word, self.trie)['#'] = word

    def search(self, searchWord: str) -> bool:

        def helper2(cur, word):
            for i, c in enumerate(word):
                if c not in cur:
                    return False
                else:
                    cur = cur[c]
            return '#' in cur

        def helper(cur, word):
            for i, c in enumerate(word):
                if c not in cur:
                    for nextLeval in cur:
                        if helper2(nextLeval, word[i + 1:]):
                            return True
                else:
                    cur = cur[c]
            return False

        return helper(self.trie, searchWord)

s = MagicDictionary()
s.buildDict(["hello","leetcode"])
s.search('hhllo')