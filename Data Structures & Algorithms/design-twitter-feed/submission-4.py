class Twitter:

    def __init__(self):
        # define structures
        self.userMap = {} # will contain sets
        self.postsmap = {} # will contain lists
        self.time = 0; # this value is going to be decrementing bc we are simulating a max heap         

    def postTweet(self, userId: int, tweetId: int) -> None:
        userPosts = self.postsmap.get(userId,[]) # get the list of posts
        post = [self.time,tweetId] # make post
        userPosts.append(post) # add post
        self.postsmap[userId] = userPosts # update map

        self.time -= 1 # update time

    def getNewsFeed(self, userId: int) -> List[int]:
        # retrive all the following and self posts
        candidates = []
        candidates.append(self.postsmap.get(userId,[]).copy()) # append the user posts

        following = self.userMap.get(userId,set()) # get following list

        for follow in following: # for each person the user follows
            candidates.append(self.postsmap.get(follow,[]).copy()) # append the posts
        
        # now we apply a max heap with the last values of each array
        # and we repeat 10 times (bc we want to retrieve just 10)
        result = []
        maxHeap = []
        
        for i in range(10):

            for posts in candidates:
                # make sure its not empty
                if not posts:
                    continue
                
                post = posts.pop() # remove last element
                heapq.heappush(maxHeap,post) # add it to the heap

            if maxHeap:
                result.append(heapq.heappop(maxHeap)[1])
            else:
                break;

        return result
    

    def follow(self, followerId: int, followeeId: int) -> None:
        following = self.userMap.get(followerId,set()) # get following list
        following.add(followeeId) # add the new follower
        self.userMap[followerId] = following # update the map

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.userMap.get(followerId,set()) # get following list

        # check if following
        if followeeId in following:
            following.remove(followeeId) # remove follower

        # update the map
        self.userMap[followerId] = following 
