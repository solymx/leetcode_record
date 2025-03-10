https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

考雙指標 two pointers

# 敘述題目

給定兩個字串 s 和 t，如果 s 是 t 的子序列，則回傳 true，否則回傳 false

子序列的定義： 子序列是從原字串 t 中刪除某些（可以是零個）字元後，仍保持剩下字元的相對位置順序後，所形成的新字串。例如：

- "ace" 是 "abcde" 的子序列（因為可以從 "abcde" 刪除 "b" 和 "d"，仍保持順序 "ace"）。
- "aec" 則 不是 "abcde" 的子序列，因為 "e" 出現在 "c" 之前，順序不對。

# 解法

最佳解法是 雙指標（Two Pointers），因為我們只需要檢查 s 是否能按照順序出現在 t 中，這意味著我們可以使用兩個指標：

1. 一個指標 i 用來掃描 s
2. 另一個指標 j 用來掃描 t
3. 如果 s[i] == t[j]，代表 s[i] 成功匹配到 t[j]，則 i++
4. 無論是否匹配，j++ 繼續前進
5. 最後如果 i == s.length()，代表 s 已經全部匹配完畢，是 t 的子序列

時間複雜：O(n)，其中 n 是 t 的長度，因為 j 只會掃描 t 一次

解題程式碼：
```
class Solution {
    public boolean isSubsequence(String s, String t) {
        // init two pointers
        int i = 0;
        int j = 0;

        while (i < s.length() && j < t.length()){
            if(s.charAt(i) == t.charAt(j)){
                i++;
            }
            j++;

        }// while end
        return i == s.length();
    }
}
```
