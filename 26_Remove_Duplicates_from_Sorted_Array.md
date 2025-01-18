#### ref: https://www.youtube.com/watch?v=86GHTcY0K4I&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=2
#### problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#### java

```
class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0; // record put unique element
        int j = 0; 
        while(j < nums.length){
            if(i == 0 || nums[i-1] != nums[j]){
                nums[i] = nums[j];
                i++;
                j++;
            }else{
                j++;
            }
        }
        return i;
    }
}
```
