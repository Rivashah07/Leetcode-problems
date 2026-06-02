from bisect import bisect_right
from typing import List
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        land_finish = sorted(
            s + d for s, d in zip(landStartTime, landDuration)
        )
        water_finish = sorted(
            s + d for s, d in zip(waterStartTime, waterDuration)
        )

        ans = float('inf')

        for ws, wd in zip(waterStartTime, waterDuration):
            if land_finish[0] <= ws:
                ans = min(ans, ws + wd)
            else:
                idx = bisect_right(land_finish, ws)
                if idx < len(land_finish):
                    ans = min(ans, land_finish[idx] + wd)
        for ls, ld in zip(landStartTime, landDuration):
            if water_finish[0] <= ls:
                ans = min(ans, ls + ld)
            else:
                idx = bisect_right(water_finish, ls)
                if idx < len(water_finish):
                    ans = min(ans, water_finish[idx] + ld)

        return ans