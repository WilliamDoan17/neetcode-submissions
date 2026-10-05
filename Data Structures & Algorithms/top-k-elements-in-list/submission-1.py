class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict[int, int] = dict()

        for num in nums:
            freq.update({num: freq.get(num, 0) + 1})

        freqList = []
        
        for item, count in freq.items():
            freqList.append((count, item))

        def getFreq(num: int) -> int:
            return freq[num]
            
        nums = list(set(nums))
        nums.sort(reverse = True, key = getFreq)
        
        return nums[:k]