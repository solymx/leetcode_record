#### ref: https://www.youtube.com/watch?v=86GHTcY0K4I&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=2
#### problem: https://leetcode.com/problems/reverse-string/description/
#### use 2 pointer to swap first and last
#### java

```
class Solution {
    public void reverseString(char[] s) {
        int i = 0 ; // head
        int j = s.length - 1; // tail
        while (i<j){
            //swap
            char tmp = s[j];
            s[j] = s[i];
            s[i] = tmp;
            i++;
            j--;
        }
    }
}
```
