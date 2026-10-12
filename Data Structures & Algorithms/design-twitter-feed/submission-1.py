class Twitter:

    def __init__(self):
        self.followList = {} # {id: set(followingIds)}
        self.feed = [] # [[userId, TweetId]]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i = len(self.feed) - 1
        c = 0

        if userId not in self.followList:
            self.followList[userId] = set()

        while i >= 0 and c != 10:
            if self.feed[i][0] == userId or self.feed[i][0] in self.followList[userId]:
                res.append(self.feed[i][1])
                c += 1
            i -= 1
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followList:
            self.followList[followerId] = set()
        
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followList:
            if followeeId in self.followList[followerId]:
                self.followList[followerId].remove(followeeId)
