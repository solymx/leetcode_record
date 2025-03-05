https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

# Description

給定一個數組 nums，將其向右旋轉 k 次，k 是非負數

## 解法

反轉數組 (最佳解法，O(1) 空間)，這種方法利用數組反轉來達成旋轉效果。

反轉法的核心概念是 透過三次反轉來達成旋轉效果，這樣就能夠 原地 (in-place) 進行數組旋轉，並且 時間複雜度 O(n)、空間複雜度 O(1)。

反轉全部：
```
[1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
```


為什麼這樣能正確旋轉？
1. 反轉整個數組 讓右側的 k 個元素變到前面。
2. 反轉前 k 個元素，讓它們回到正確的順序。
3. 反轉後 n-k 個元素，讓剩下的部分回到正確順序。

優勢 
✅ O(n) 時間複雜度
✅ O(1) 空間複雜度
✅ 容易實作，無需額外數組

solution.java
```
class Solution {
    public void reverse(int[] nums, int left, int right){
        while(left < right){
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
    
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n; // avoid k over length

        reverse(nums, 0, n-1); // reverse all
        reverse(nums, 0, k-1); // reverse k
        reverse(nums, k, n-1); // reverse last n-k

    }


}
```
