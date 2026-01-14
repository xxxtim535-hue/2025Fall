#回溯法
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = defaultdict(int)

        # nums[i] 选或不选
        def dfs(i: int) -> None:
            if i == len(nums):
                nonlocal ans
                ans += 1
                return
            dfs(i + 1)  # 不选
            x = nums[i]
            if cnt[x - k] == 0 and cnt[x + k] == 0:  # 可以选
                cnt[x] += 1  # 选
                dfs(i + 1)  # 讨论 nums[i+1] 选或不选
                cnt[x] -= 1

        dfs(0)
        return ans

#另解
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = defaultdict(int)

        # 在 [i, n-1] 中选一个数
        def dfs(i: int) -> None:
            nonlocal ans
            ans += 1
            if i == len(nums):
                return
            for j in range(i, len(nums)):  # 枚举选哪个
                x = nums[j]
                if cnt[x - k] == 0 and cnt[x + k] == 0:  # 可以选
                    cnt[x] += 1  # 选
                    dfs(j + 1)  # 下一个数在 [j+1, n-1] 中选
                    cnt[x] -= 1  # 撤销，恢复现场

        dfs(0)
        return ans