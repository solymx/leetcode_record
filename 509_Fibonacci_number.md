考 DP
# 介紹

費式數列

# 解題程式碼
JAVA
```
class Solution {
    public int fib(int n) {
        if(n == 0)return 0;
        if(n == 1)return 1;

        int p1 = 0;
        int p2 = 1;
        int curr = 0;
        for(int i = 2; i<= n;i++){
            curr = p1 + p2;
            p1 = p2;
            p2 = curr;
        }
        return p2;
    }
}
```
