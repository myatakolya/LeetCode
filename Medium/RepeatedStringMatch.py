'''
Problem: Repeated String Match
Number: 79
Difficulty: Easy
Time Complexity: O(len(a)*len(b))
Space Complexity: O(len(a)+len(b))
URL: https://leetcode.com/problems/repeated-string-match
Topics: String, String Matching
'''
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 1
        sub_string = a
        while len(sub_string) < len(b):
            sub_string += a
            count += 1
        if b in sub_string:
            return count
        if b in sub_string + a:
            return count + 1
        return -1
                