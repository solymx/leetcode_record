https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

貪婪演算法 (Greedy Algorithm) 的典型問題。

# 題目敘述

你被給予一個整數陣列 prices，其中 prices[i] 代表股票在第 i 天的價格。

- 你可以在一天內買入並賣出股票（但不能持有超過一股）。
- 你可以進行多次交易（可以多次買賣）。
- 你必須以當天的價格賣出後，才能再次買入。

目標：找出 最大可能的利潤。


# 解題思路

(如果 當前的最佳選擇不影響未來選擇，則適用貪婪策略)

1. 核心概念：局部最優解 → 全域最優解

這題的核心是 「可以多次買賣股票」，但 不能持有超過一股股票，所以我們的目標是在價格上升的時候賺取所有的價差。
只要今天的價格比昨天高，就賣出，這樣可以確保每一次的交易都是獲利的。
與其考慮 最低點買入、最高點賣出，我們可以把所有上升的區間加總，這樣可以達到最優解。

2. 貪婪策略

只要 今天價格 > 昨天價格，就把這個價差加入 總獲利，等同於每天都在買賣，但實際上是一種 累積獲利的方式。


# 詳細解釋
1. 初始化 profit = 0：用來累積獲利。
2. 遍歷 prices 陣列 (從第二天開始)：
- 如果今天 (prices[i]) 比昨天 (prices[i-1]) 貴：
  -賺取價差 (prices[i] - prices[i-1])，加入總獲利 profit。
3. 最後回傳 profit，即最大可獲利。

# 時間與空間複雜度

時間複雜度： 
𝑂(𝑛)
O(n)（遍歷一次 prices）

空間複雜度： 
𝑂(1)
O(1)（只使用一個變數 profit）

# 解題程式碼

```
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for(int i = 1; i < prices.length; i++){
            if(prices[i] > prices[i-1]){
                profit += prices[i] - prices[i-1] ;
            }
        }
        return profit;
    }
}
```
