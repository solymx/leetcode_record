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

得到：
```
70 -> 50 -> 10 -> 60 -> 90 -> 20 -> 100
```

```
  private preOrderTraverseNode(node: Node<T> | null) {
    if (node) {
      console.log(node.value);
      this.preOrderTraverseNode(node.left)
      this.preOrderTraverseNode(node.right)
    }
  }

  preOrderTraverse() {
    this.preOrderTraverseNode(this.root)
  }
```

## inorder Traverse（中序遍歷）

特色：中序遍歷（in-order traversal）會得到一個遞增的數列

流程：先訪問left children node -> root node -> right children node
example
```
        70
    /        \
  50           90
 /   \        /     \
10    60      20    100
```

得到：

```
10 -> 50 -> 60 -> 70 -> 20 -> 90 -> 100
```

```
  private inOrderTraverseNode(node: Node<T> | null) {
    if (node) {
      this.inOrderTraverseNode(node.left)
      console.log(node.value)
      this.inOrderTraverseNode(node.right)
    }
  }

  inOrderTraverse() {
    this.inOrderTraverseNode(this.root)
  }
```

## postorder Traverse（後序遍歷）

遍歷流程：先訪問left children node -> right children node -> root node

example
```
        70
    /        \
  50           90
 /   \        /     \
10    60      20    100
```

得到：
```
10 -> 60 -> 50 -> 20 -> 100 -> 90 -> 70
```

```
  private postOrderTraverseNode(node: Node<T> | null) {
    if (node) {
      this.postOrderTraverseNode(node.left)
      this.postOrderTraverseNode(node.right)
      console.log(node.value)
    }
  }

  postOrderTraverse() {
    this.postOrderTraverseNode(this.root)
  }
```
