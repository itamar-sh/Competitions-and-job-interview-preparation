class Solution:
    def addOne(self, lst):
        for i in range(len(lst)):
            # print(lst)
            if lst[i] == 1:
                lst[i] = 0
            elif lst[i] == 0:
                lst[i] = 1
                return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = [0] * len(nums)
        res = []
        for i in range(2 ** len(nums)):
            print(res)
            sub = []
            for j in range(len(nums)):
                if lst[j] == 1:
                    sub.append(nums[j])
            res.append(sub)
            self.addOne(lst)
        return res
