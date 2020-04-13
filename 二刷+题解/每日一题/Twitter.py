#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Twitter.py
@Time    :   2020/04/13 15:22:13
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Twitter:

    user_stack = []
    tweet_db = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        user_stack.append(user_stack[-1]+1)
        self.user_id = user_stack[-1]
        tweet_db.update({self.user_id: []})
        self.follow_list = [self.user_id]




    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        tweet_db[self.user_id].append(tweetId)


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """



    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """



if __name__ == '__main__':
    # Your Twitter object will be instantiated and called as such:
    # obj = Twitter()
    # obj.postTweet(userId,tweetId)
    # param_2 = obj.getNewsFeed(userId)
    # obj.follow(followerId,followeeId)
    # obj.unfollow(followerId,followeeId)