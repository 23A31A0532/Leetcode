class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        
        @lru_cache(None)
        def DFS(left , right):

            if left == right:
                return 0
            
            total_sum = sum(stoneValue[left : right + 1])
            left_sum = 0
            result = 0

            for index in range(left , right):

                left_sum = left_sum + stoneValue[index]
                right_sum = total_sum - left_sum

                if left_sum < right_sum:
                    result = max(result , DFS(left , index) + left_sum)
                elif left_sum > right_sum:
                    result = max(result , DFS(index + 1 , right) + right_sum)
                else:
                    result = max(result , max(DFS(left , index) , DFS(index + 1, right)) + left_sum)
                
            return result

        n = len(stoneValue)
        return DFS(0 , n - 1)