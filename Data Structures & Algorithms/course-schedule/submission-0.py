class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sub = defaultdict(set)
        pre = defaultdict(set)
        for a,b in prerequisites:
            sub[b].add(a)
            pre[a].add(b)
        dq = deque()
        taken = 0
        for i in range(numCourses):
            if i not in pre:
                taken+=1
                dq.append(i)
        while dq:
            course = dq.popleft()
            for sub_course in sub[course]:
                pre[sub_course].remove(course)
                if len(pre[sub_course])==0:
                    taken+=1
                    dq.append(sub_course)
        return taken ==numCourses
