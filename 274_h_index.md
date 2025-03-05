https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

# 題目介紹

H-Index 是指一個研究人員發表的 h 篇論文中，每篇論文的引用次數都至少為 h，且剩餘的論文引用次數不超過 h。

給定一個整數數組 citations，其中 citations[i] 表示研究人員的第 i 篇論文被引用的次數。請返回該研究人員的 H-Index。

# 解題思路

H-Index 的计算方式是找到最大的 h 值，满足至少有 h 篇论文的引用次数不小于 h

解題步驟：
1. 將 citations 陣列由大到小排序
2. 遍歷找 h ，只到當前論文引用 >= 當前排名就讓 h 增加

# 解題程式碼

```
class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations); // 0, 1, 2, 3 ...
        int h = 0;
        int n = citations.length;

        // from big -> small to do search
        for(int i = n-1;i>=0;i--){
            if(citations[i] >= h+1){
                h++;
            }else{
                break; // if now paper's citations < h+1 then break
            }
        }
        return h;

    }
}
```
