# 介紹

二元搜尋樹（Binary Search Tree）, BST

- 左一定小於中間
- 右一定大於中間

# 找最大最小值

- 只要持續的往left node找就會找到最小值，反之最大值則是持續往right node查找

# 遍歷

## preorder Traverse（前序遍歷）

先訪問root node-> left children node -> right children node

example
```
        70
    /        \
  50           90
 /   \        /     \
10    60      20    100
```
