class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        word_set.add(beginWord)
        wordList = list(word_set)

        
        def isValid(s1,s2):
            diff = 0
            for a,b in zip(s1,s2):
                if a!=b:
                    diff+=1
                    if diff>1:
                        return False
            return diff == 1

        graph = defaultdict(set)
        length = len(wordList)
        for i in range(length-1):
            for j in range(i+1,length):
                s1,s2 = wordList[i],wordList[j]
                if isValid(s1,s2):
                    graph[s1].add(s2)
                    graph[s2].add(s1)
                    
        dq = deque()
        dq.append(beginWord)
        visited = set([beginWord])
        depth = 1
        while dq:
            for _ in range(len(dq)):
                w1 = dq.popleft()
                for neighbor in graph[w1]:
                    print(neighbor,depth)
                    if neighbor == endWord:
                        return depth+1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dq.append(neighbor)
            depth+=1
        return 0