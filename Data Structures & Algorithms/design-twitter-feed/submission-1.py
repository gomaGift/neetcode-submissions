import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.user_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        out += self.tweet_map[userId][-10:]
        for followee_id in self.user_map[userId]:
            out += self.tweet_map[followee_id][-10:]

        out.sort(reverse=True)
        return [t[1] for t in out[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
          self.user_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_map[followerId].discard(followeeId)
