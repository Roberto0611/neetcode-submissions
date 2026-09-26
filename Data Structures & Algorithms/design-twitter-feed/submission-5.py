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
        maxHeap = []
        result = []

        # get the following
        following = self.userMap.get(userId,set()) # get following list
        users_to_check = following | {userId} # add our userId without modifyng the original

        # initialize the heap, with the last post of each person
        for user in users_to_check:
            posts = self.postsmap.get(user, []) # get the user posts

            if posts:
                idx = len(posts) - 1  # the position of the last element
                time, tweetId = posts[idx] # get the values

                # we add the post to the heap but with extra info 
                maxHeap.append([time, tweetId, user, idx])

        # once we have our list we heapify it
        heapq.heapify(maxHeap)

        # main loop to extract the 10 last posts
        while maxHeap and len(result) < 10:
            # pop the top with all the info
            time, tweetId, user, idx = heapq.heappop(maxHeap)
            result.append(tweetId) # add it to the heap

            # and then we update idx for that user
            if idx > 0:
                next_idx = idx - 1
                next_time, next_tweetId = self.postsmap[user][next_idx] # get the next post
                heapq.heappush(maxHeap, [next_time, next_tweetId, user, next_idx]) # add it to the heap
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
