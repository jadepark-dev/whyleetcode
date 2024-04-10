#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
# https://leetcode.com/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (49.69%)
# Likes:    4693
# Dislikes: 539
# Total Accepted:    424.1K
# Total Submissions: 857.3K
# Testcase Example:  '["TimeMap","set","get","get","set","get","get"]\n' +
#  '[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a
# certain timestamp.
#
# Implement the TimeMap class:
#
#
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the
# value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was
# called previously, with timestamp_prev <= timestamp. If there are multiple
# such values, it returns the value associated with the largest timestamp_prev.
# If there are no values, it returns "".
#
#
#
# Example 1:
#
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo",
# 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along
# with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value
# corresponding to foo at timestamp 3 and timestamp 2, then the only value is
# at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along
# with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
#
#
#
# Constraints:
#
#
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 10^7
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.
#
#
#


# @lc code=start
class TimeMap:

    def __init__(self):
        self.map = {}  # key=string, value=[[val, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])
        # if you don't find exact match, return the most recent one.
        l, r = 0, len(values) - 1

        while l <= r:  # while the left pointer hans't cross the right pointer

            m = l + (r - l) // 2

            if values[m][1] <= timestamp:
                # so far this is the closest value(valid)
                res = values[m][0]

                # move the left pointer
                l = m + 1

            else:
                r = m - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
