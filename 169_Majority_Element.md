https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
# Description

這題目要求找出在陣列 nums 中出現超過 n/2 次的元素，且保證一定會有這個元素。

這題重點在，他保證一定存在 n > n/2 的元素，才可以用投票法

使用：Boyer-Moore 投票法（最佳解法，時間 O(n)，空間 O(1)）
演算法概念：

1. 候選人選擇： 使用變數 candidate 來儲存目前的多數元素候選人。
2. 計數更新： 若 count == 0，則更新 candidate 為當前數字。
3. 計數變化： 若 num == candidate，則 count +1，否則 count -1。
4. 最終結果： 由於多數元素一定存在，最終 candidate 即為答案。

algorithm.java
```
public class MajorityElement {
    public static int majorityElement(int[] nums) {
        int candidate = 0, count = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }

    public static void main(String[] args) {
        int[] nums = {2, 2, 1, 1, 1, 2, 2};
        System.out.println(majorityElement(nums)); // Output: 2
    }
}
```


# 演算法核心概念
Boyer-Moore 投票法的核心思想是 「計票與抵消」，目標是在一次遍歷中找出可能的多數元素。

1. 候選人（candidate）選擇：使用變數 candidate 來代表多數元素的候選人。
2. 計數（count）更新：
- 如果 count == 0，則更新 candidate 為當前數字，並將 count 設為 1。
- 如果當前數字與 candidate 相同，則 count +1。
- 如果當前數字與 candidate 不同，則 count -1。
3. 最終結果：
- 由於題目保證陣列中一定有多數元素（出現次數 > n/2），所以最後 candidate 一定是正確的答案。



solution.java
```
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        for (int num: nums){
            if(count == 0){
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }
        return candidate;
    }
}
```
