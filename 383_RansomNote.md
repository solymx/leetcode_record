https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

考：hash table

# 簡介

給定兩個字串 ransomNote（勒索信）與 magazine（雜誌），若能夠從雜誌裡取出足夠的字母（每個字母只能使用一次），拼湊出勒索信的內容，則回傳true，否則回傳false。

# 解題

使用Hash Table（或陣列）來記錄magazine字串中每個字母出現的次數，然後遍歷ransomNote中的每個字母，檢查是否有足夠的字母來使用。

由於題目限制字母只包含小寫英文字母，因此可以用大小為26的陣列來統計次數。

解題程式碼
```
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] count = new int[26];

        // calculate magazine's each alpha's count
        for(char c: magazine.toCharArray()){
            count[c - 'a']++;
        }
        // check ransomNote can use ?
        for(char c: ransomNote.toCharArray()){
            count[c - 'a']--;
            if(count[c - 'a'] < 0){
                return false;
            }
        }

        return true;
    }
}
```
