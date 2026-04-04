class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 先把数组转成哈希集合，方便用 O(1) 时间判断某个数字是否存在
        # Convert the array into a hash set so we can check existence in O(1) time
        num_set = set(nums)

        # 记录最长连续序列的长度，初始为 0
        # Store the length of the longest consecutive sequence, initialized to 0
        longest = 0

        # 只有当前一个数字不存在时，才把当前数字当作连续序列的起点
            # Only treat the current number as the start of a sequence if the previous number does not exist
        for num in num_set:
            # 当前数字是连续序列的起点，因此当前序列长度先设为 1
            # Current number is the start of a sequence, so initialize current sequence length to 1
            current_length = 1
            # 从当前数字开始向后查找连续的下一个数字
            # Starting from the current number, keep checking the next consecutive numbers
            current_num = num
            # 只要下一个数字存在，说明连续序列还可以继续延伸
            # As long as the next number exists, the consecutive sequence can continue
            while current_num + 1 in num_set:
                # 移动到下一个连续数字
                # Move to the next consecutive number
                current_num += 1
                # 当前连续序列长度加 1
                # Increase the current sequence length by 1
                current_length += 1
            # 更新全局最长连续序列长度
            # Update the global longest consecutive sequence length
            longest = max(longest, current_length)
            
        return longest