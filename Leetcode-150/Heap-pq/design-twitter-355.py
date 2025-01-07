"""
    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
    and is able to see the 10 most recent tweets in the user's news feed.
    
    Implement the Twitter class:
    Twitter() Initializes your twitter object.
    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. 
    Each call to this function will be made with a unique tweetId.
    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
    Each item in the news feed must be posted by users who the user followed or by the user themself.
    Tweets must be ordered from most recent to least recent.
    void follow(int followerId, int followeeId) The user with ID followerId started following
    the user with ID followeeId.
    void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing
    the user with ID followeeId
"""
from typing import List
from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.map = defaultdict(list) # id : "List of tweets combination of tweetTime and the tweetId"[[tweetTime, tweetId]]
        self.followMap = defaultdict(set) #set : this keeps track of who he is following {userId : "set"[]}.
        # So why set if we wanted to get the tweets posted the people he if following, if it was list we had to go through
        # every sigle person he is following and get the list of tweets made by this person but with set it is faster.
        
        # Keeps track of at which time this tweet was made.
        self.tweetTime = 0
    
    # map[id : [].append([tweetTime, tweetId])]
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.map[userId].append([self.tweetTime, tweetId])
        self.tweetTime -= 1
        
    # The approach is very similar merge k sorted lists
    # The tweets made by each person are going in increasing order
    # if we wanted to get the 10 recent tweets made by him and his 
    # followers how can we do this one way would be to just merge 
    # all of these too one list and sort that and then pick the 
    # 10 most recent a better way would be to pick all the most 
    # recent ones from the list (*in this case the end of the list)
    # and offer them to the heap now this sorts them in assending 
    # order and we can pick the most recent one and then offer the 
    # next element from this poped one to heap this because the lists are 
    # sorted and we would want process the next recent tweet after this. 
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.followMap[userId].add(userId)
        for followe in self.followMap[userId]:
            if followe in self.map:
                index = len(self.map[followe]) -1
                t, tweetId = self.map[followe][index]
                heapq.heappush(min_heap,[t, tweetId, followe, index-1])

        while min_heap and len(res)< 10:
            t, tweetId, followe, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >=0 :
                newCount, newTweetId = self.map[followe][index]
                heapq.heappush(min_heap,[newCount, newTweetId, followe, index-1])

        return res

    # followMap[followerId] : set(followeeId)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
    
    # remove followeeId from followMap[followerId]: set()
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

def test_twitter():
    # Initialize Twitter
    twitter = Twitter()

    # Test 1: Post tweets and check user's own news feed
    twitter.postTweet(1, 101)
    assert twitter.getNewsFeed(1) == [101], "Test 1 Failed"

    twitter.postTweet(1, 102)
    assert twitter.getNewsFeed(1) == [102, 101], "Test 1 Failed"

    # Test 2: Follow a user and check news feed
    twitter.postTweet(2, 201)
    twitter.follow(1, 2)
    assert twitter.getNewsFeed(1) == [201, 102, 101], "Test 2 Failed"

    # Test 3: Unfollow a user and check news feed
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [102, 101], "Test 3 Failed"

    # Test 4: Multiple users and tweets
    twitter.postTweet(2, 202)
    twitter.postTweet(3, 301)
    twitter.follow(1, 3)
    assert twitter.getNewsFeed(1) == [301, 102, 101], "Test 4 Failed"

    # Test 5: Check news feed limit (10 tweets)
    for i in range(10):
        twitter.postTweet(1, 1000 + i)
    expected_feed = [1009, 1008, 1007, 1006, 1005, 1004, 1003, 1002, 1001, 1000]
    assert twitter.getNewsFeed(1) == expected_feed, "Test 5 Failed"

    # Test 6: Follow multiple users and check news feed
    twitter.postTweet(2, 203)
    twitter.postTweet(3, 302)
    twitter.follow(1, 2)
    twitter.follow(1, 3)
    assert len(twitter.getNewsFeed(1)) <= 10, "Test 6 Failed"

    # Test 7: Unfollow a user with no tweets
    twitter.unfollow(1, 3)
    assert len(twitter.getNewsFeed(1)) <= 10, "Test 7 Failed"

    print("All tests passed!")

# Run the test
test_twitter()
