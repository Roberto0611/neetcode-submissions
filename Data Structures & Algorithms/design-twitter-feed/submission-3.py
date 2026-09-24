class Twitter:

    def __init__(self):
        self.posts = []
        self.follows = {} 

    def postTweet(self, userId: int, tweetId: int) -> None:
        post = [-tweetId, userId] # negative for max heap
        self.posts.append(post) # we use a regular list not a heap

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        copia_posts = self.posts.copy()
        # set to avoid duplicate values
        following = self.follows.get(userId, set())
        following.add(userId)

        # here make sure to count the pop posts not the total posts
        count = 0
        while count < 10:
            if len(copia_posts) == 0:
                break

            p = copia_posts.pop()
            if p[1] in following:
                feed.append(-p[0])
                count += 1
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        following = self.follows.get(followerId, set())
        following.add(followeeId)
        self.follows[followerId] = following

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # here I feel we can optimize using linked list or binary search
        following = self.follows.get(followerId, set())

        # search the value
        if followeeId in following:
            following.remove(followeeId)
        
        self.follows[followerId] = following    
