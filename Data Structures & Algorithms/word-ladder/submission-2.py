from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        word_set.add(beginWord)
        L = len(beginWord)

        pattern_map = defaultdict(list)

        for word in word_set:
            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_map[pattern].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, depth = q.popleft()

            if word == endWord:
                return depth

            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1:]

                for nei in pattern_map[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, depth + 1))

                pattern_map[pattern] = []

        return 0