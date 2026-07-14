'''
Problem: Merge Strings Alternately
Number: 37
Difficulty: Easy
Time Complexity: O(n + m)
Space Complexity: O(n + m)
URL: https://leetcode.com/problems/merge-strings-alternately
Topics: String, Two Pointers
'''
class Solution:
    #Time Complexity: O(n + m)
    #Space Complexity: O(n + m)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1), len(word2)
        res = []
        p1,p2 = 0,0
        while p1 < n or p2 < m:
            try:
                res.append(word1[p1])
            except IndexError:
                pass
            
            try:
                res.append(word2[p2])
            except IndexError:
                pass
            
            p1,p2 = p1+1,p2+1
            
        return ''.join(res)
    
    
    #Time Complexity: O(n + m)
    #Space Complexity: O(n + m)
    def mergeAlternately_2(self, word1: str, word2: str) -> str:
        n,m = len(word1), len(word2)
        res = []
        p1,p2 = 0,0
        while p1 < n and p2 < m:
            res.append(word1[p1])
            res.append(word2[p2])
            p1,p2 = p1+1,p2+1
        
        while p1 < n:
            res.append(word1[p1])
            p1+=1
        
        while p2 < m:
            res.append(word2[p2])
            p2 += 1
        return ''.join(res)

s1,s2 = 'ab','pqrs'
s = Solution()
print(s.mergeAlternately(s1,s2))
                
                

