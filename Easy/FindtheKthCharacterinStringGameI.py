
class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1: return 'a'
        n = 0
        while 2**n < k:
            n+=1
        offset = 0
        pos = k-1
        while n > 0:
            half = 2**(n-1)
            if pos < half:
                pass
            else:
                pos -= half
                offset += 1
            n -= 1
        return chr(ord('a') + offset)
        
            
    
i1 = 5
i2 = 10
solver = Solution()
print(solver.kthCharacter(i1))
print(solver.kthCharacter(i2))