"""
    given an integer numRows return the first numRows of Pascal's Triangle
    in pascal's triangle each number is the sum of the two numbers directly above it as shown
"""

class Solution:
    def pascal_triangle(self,numRows: int) -> List[list[int]]:
        res = [[1]]
        
        