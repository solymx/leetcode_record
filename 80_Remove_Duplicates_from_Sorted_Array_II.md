# Description

這題考雙指針用法

目標是 移除排序陣列中多於兩次的重複元素，並且 原地修改陣列 (in-place)，不能使用額外空間

由於陣列已經是 非遞減排序 (non-decreasing order)，我們可以利用 雙指針 (Two Pointers) 來高效解決問題：

1. 指針 index：用來存放符合條件的數字，從索引 2 開始，因為前兩個數字可以直接保留。
2. 指針 i：用來遍歷整個陣列，從索引 2 開始。
3. 條件判斷：
- 若 nums[i] 與 nums[index - 2] 不同，則 nums[i] 需要被保留。
- 我們將 nums[i] 存入 nums[index]，並讓 index++，表示有效元素數量增加。
- 若 nums[i] 與 nums[index - 2] 相同，表示這個數字已經出現兩次以上，因此跳過它。

時間與空間複雜度
- 時間複雜度：O(n)，只需遍歷一次陣列。
- 空間複雜度：O(1)，僅使用了常數額外變數。

這種 雙指針 (Two Pointers) 方法 不會改變原始元素順序，而且只需要 O(n) 時間複雜度 和 O(1) 額外空間

solution.java
```
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2){
            return nums.length;
        }

        int index = 2;
        for(int i = 2; i < nums.length; i++){
            // if now number differ index - 2 , then save
            if(nums[i] != nums[index - 2]){
                nums[index] = nums[i];
                index++;
            }
        }//for end
        return index;
    }
}
```
