https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150

# 題目敘述

給定一個 points 陣列，其中 points[i] = [xᵢ, yᵢ] 表示 X-Y 平面上的一個點，請找出在同一直線上的最大點數。

# 解題思路

找出最多點數共線的情況，關鍵在於計算 斜率，因為 兩點確定一條直線

兩點斜率計算方式：  斜率 = (y2-y1) / (x2-x1)

由於 Java 的浮點數精度問題，我們用 分數 (dy, dx) 來表示斜率，並使用 最大公因數 (GCD) 來約分，確保斜率的唯一性。


1. 先計算斜率
2. 遍歷所有點對

- 固定一個點 作為起點。
- 使用 HashMap 記錄相同斜率的點數，鍵為 (dy/dx) 斜率，值為計數。
- 每次統計最大共線點數。
3. 處理特殊情況

- 垂直線 (x 相同，無法計算斜率)，設為 (1,0) 。
- 重複點，增加 duplicates 計數，因為它們不影響斜率計算，但應該計入最大數量。

# 解題程式碼

```
import java.util.HashMap;
class Solution {
    public int maxPoints(int[][] points) {
        if(points.length < 2) return points.length;

        int maxCount = 1; // at least one point

        for(int i = 0; i < points.length ; i ++){
            HashMap<String, Integer> slopeMap = new HashMap<>(); // use to save slope
            int dup = 0; // record duplicate point
            int localMax = 0; // record this point with other point (same line)
            for(int j = i +1 ; j < points.length; j++){
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];
                int gcd = gcd(dx, dy);

                dx /= gcd;
                dy /= gcd;

                String slope = dy + "/" + dx;
                slopeMap.put(slope, slopeMap.getOrDefault(slope, 0) + 1);

                localMax = Math.max(localMax, slopeMap.get(slope));
            }// calculate slope
            maxCount = Math.max(maxCount, localMax + 1 + dup);
        }//for end
        return maxCount;
    }
    private int gcd(int a, int b){
        return b == 0 ? a : gcd(b, a%b);
    }
}
```
