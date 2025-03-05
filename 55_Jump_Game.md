https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

# 介紹

貪心演算法（Greedy Algorithm） 的典型問題，主要考慮如何透過跳躍來到達最後一個位置。

題目要求判斷是否能夠從 索引 0 開始，透過每個位置的跳躍範圍來到達最後一個索引。

📌 如果有一個位置是 0，且無法透過前面的跳躍繞過它，就無法到達終點！

關鍵點：

1. 每個位置的值 nums[i] 表示在該位置最多能往前跳幾步。
2. 如果某個位置是 0，且無法跨越，則無法到達最後索引。
3. 只要能到達最後一個索引，就回傳 true，否則回傳 false。

# 解法：貪心演算法
解題思路
核心思想：維護一個變數 maxReach，表示當前可以到達的最遠位置：

1. 初始化 maxReach = 0，表示最遠可到達索引的初始值為 0。
2. 遍歷 nums，如果當前索引 i 超過 maxReach，代表無法到達該位置，直接回傳 false。
3. 不斷更新 maxReach = max(maxReach, i + nums[i])，代表從當前位置 i，最遠可以跳到的位置。
4. 如果 maxReach >= nums.length - 1，則可以到達最後位置，回傳 true。

# 時間與空間複雜度分析
時間複雜度：O(n)，因為我們只遍歷一次 nums 陣列。
空間複雜度：O(1)，因為只使用了一個變數 maxReach。

這個方法比 回溯（Backtracking, O(2^n)） 或 動態規劃（DP, O(n^2)） 更高效，非常適合處理 n = 10^4 的大數據範圍。

# 解題程式碼

```
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0; // location that can reach the most

        for(int i = 0; i < nums.length;i++){
            if(i > maxReach){
                return false; // now index over the maxReach
            }
            maxReach = Math.max(maxReach, i + nums[i]); // update the most location that can reach
            if(maxReach >= nums.length - 1){
                return true;
            }

        }//for end
        return false;
    }
}
```
