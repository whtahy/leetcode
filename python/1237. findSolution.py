"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

# brute force
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ls = []
        for x in range(1, 1000+1):
            for y in range(1, 1000+1):
                if customfunction.f(x, y) == z:
                    ls += [[x, y]]
                elif customfunction.f(x, y) > z:
                    break
        return ls
