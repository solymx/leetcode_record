# 題目敘述

給定一棵二元搜尋樹，請找出任意兩個節點之間的最小絕對差值。

這道題的特點是利用 BST 的性質：中序遍歷 的結果會是一個遞增的序列，最小差值一定出現在相鄰節點之間。

# 解題

```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

        private int minDiff = Integer.MAX_VALUE;
        private Integer prev = null; // use to record now value




    public int getMinimumDifference(TreeNode root) {
        
        inOrderTravelsal(root);
        return minDiff;

        
    }

    private void inOrderTravelsal(TreeNode node){
        if(node == null) return ;
        
        inOrderTravelsal(node.left);

        if(prev != null){ // calculate near node's diff value
            minDiff = Math.min(minDiff, node.val - prev);
        }
        prev = node.val;

        inOrderTravelsal(node.right);


    }
}
```
