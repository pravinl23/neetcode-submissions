class Twitter:

    def __init__(self):
        self.users = {} # user_id : [set(following), heap(posts)]
        self.time = 0
    
    def ensureUserExist(self, userId):
        if userId not in self.users:
            self.users[userId] = [set(), []]
            self.users[userId][0].add(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ensureUserExist(userId)
        heapq.heappush(self.users[userId][1], (-self.time, tweetId))
        self.time += 1
        return


    def getNewsFeed(self, userId: int) -> List[int]:
        self.ensureUserExist(userId)
        
        followingList = self.users[userId][0]
        revert = [] # (userId, tweetId)
        for _ in range(10):
            i = None
            m = math.inf
            t = None
            for f in followingList:
                if self.users[f][1] and self.users[f][1][0][0] < m:
                    i = f
                    m = self.users[f][1][0][0]
            if i is None:
                break    
            tweetId = heapq.heappop(self.users[i][1])[1]
            revert.append((i, tweetId, m))

        res = []
        for u, tweet, t in revert:
            res.append(tweet)
            heapq.heappush(self.users[u][1], (t, tweet))

        return res

            
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.ensureUserExist(followerId)
        self.ensureUserExist(followeeId)
        self.users[followerId][0].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.ensureUserExist(followerId)
        if followeeId != followerId and followeeId in self.users[followerId][0]:
            self.users[followerId][0].remove(followeeId)
        return
