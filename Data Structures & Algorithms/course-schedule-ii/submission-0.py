class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sub = defaultdict(set)
        pre = defaultdict(set)
        for a,b in prerequisites:
            sub[b].add(a)
            pre[a].add(b)
        dq = deque()
        res = []
        for i in range(numCourses):
            if i not in pre:
                dq.append(i)
                res.append(i)
        while dq:
            course = dq.popleft()
            for sub_course in sub[course]:
                pre[sub_course].remove(course)
                if len(pre[sub_course])==0:
                    dq.append(sub_course)
                    res.append(sub_course)
        if len(res)==numCourses:
            return res
        return[]
