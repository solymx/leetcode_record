https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150

# 介紹

這題要你實作一個函數 pow(x, n)，這個函數的目的是計算一個數字 x 的 n 次方，即計算 

# 解法

選擇使用迭代 (非遞迴) 的方式，避免了遞迴的額外成本

這題牽涉到指數運算，如果直接用循環逐次相乘來計算，會導致運算效率極低（時間複雜度為 O(n)），因此需要用到快速冪法 (Fast Power)。

快速冪法利用了指數運算的特性：
1. x^4 = x^2 * x^2
2. x^5 = x * x^2 * x^2

我們可以透過遞迴或者迭代的方式，快速地將指數減半，從而達到 O(logn) 的複雜度。
選擇使用迭代 (非遞迴) 的方式，避免了遞迴的額外成本

# 解題程式碼
```
class Solution {
    public double myPow(double x, int n) {
        double result = 1.0;
        long N = n; // avoid int overflow , use long type to deal negative

        // deal to positive
        if(N < 0){
            x = 1/x;
            N = -N;
        }

        // do fast power
        while(N > 0){
            if((N & 1) == 1) {// if N is odd
                result *= x;
            }
            x *= x;
            N >>= 1; // N / 2 (represent N >> 1)
        }
        return result;
    }
}
```
