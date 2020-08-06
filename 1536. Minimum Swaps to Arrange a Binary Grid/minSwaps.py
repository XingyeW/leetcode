# Degree of difficulty: Medium

# First count the number of consecutive 0s in each row from back to front.
# Then find the smallest number of rows that can meet the number of 0 in the current or subsequent rows of each row.
# If it cannot meet the requirement, return -1. 
# If it is satisfied, shift the elements in the array between current row and the row before found row after the element of the found row. 
# The number of steps plus the found row minus the current row.

# complexity: O(n²)
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        length = len(grid)
        zero_number = []
        for i in range(length):
            count = 0
            for j in range(length-1,-1,-1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            zero_number.append(count)
        ans = 0
        for index in range(length-1):
            if zero_number[index] >= length - 1 - index:
                continue
            e = index + 1
            while e < length:
                if zero_number[e] >= length - 1 - index:
                    ans += e - index
                    zero_number[index:e+1] = [zero_number[e]] + zero_number[index:e]
                    break
                else:
                    e += 1
            if e == length:
                return -1
        return ans
