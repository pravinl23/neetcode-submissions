class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        c = [(-c[task]) for task in c]
        heapq.heapify(c)
        q = deque()
        time = 0

        while c or q:
            time += 1
            
            if c:
                count = heapq.heappop(c) + 1
                if count != 0:
                    q.append([count, time + n])

            if q and time >= q[0][1]:
                heapq.heappush(c, q[0][0])
                q.popleft()
            

        return time

