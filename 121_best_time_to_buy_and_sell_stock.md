https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

# Description

題目要求找出一個數組 prices 中的最大獲利，條件是：

- 只能買賣一次（先買後賣）。
- 買入的日子必須在賣出之前。
- 若無法獲利，則回傳 0。

# 解法思路
使用變數 minPrice 來追蹤目前最低的股價：

1. 一開始將 minPrice 設為無限大 (Integer.MAX_VALUE)。
- 遍歷 prices，若發現更低的價格，就更新 minPrice。

2. 使用變數 maxProfit 來追蹤目前最高的獲利：
- 計算當天價格與 minPrice 之間的利潤。
- 若此利潤大於 maxProfit，則更新 maxProfit。

時間複雜度分析：
- 由於只需遍歷一次 prices（O(n)），這是一個 線性時間 解法，非常高效。

solution.java
```
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for(int price: prices){
            if(price < minPrice){
                minPrice = price;
            }
            // calculate if sell can get how much ?
            int profit = price - minPrice;
            if(profit > maxProfit){
                maxProfit = profit;
            }
        }
        return maxProfit;

    }
}
```
