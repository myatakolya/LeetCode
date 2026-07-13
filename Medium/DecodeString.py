'''
Problem: Decode String
Number: 13
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/decode-string
Topics: String, Stack, Recursion
'''
class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i: int):
            result = ""
            num = 0
            
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    inner, i = decode(i + 1)
                    result += inner * num
                    num = 0
                elif s[i] == ']':
                    return result, i
                else:
                    result += s[i]
                i += 1
            
            return result, i
        
        decoded, _ = decode(0)
        return decoded
            
    
i1 = "3[a]2[bc]"
i2 = "3[a2[c]]"
i3 = "2[abc]3[cd]ef"
solver = Solution()
print(solver.decodeString(i1))
print(solver.decodeString(i2))
print(solver.decodeString(i3))