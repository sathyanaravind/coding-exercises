# coding-exercises
list of solutions to common coding problems


# Table of Contents
- [Notes](#Notes)
- [Data Structures](#data-structures)
  - [Array](#array)
  - [Linked list](#linked-list)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Trees](#trees)
  - [Tries](#tries)
  - [Graphs](#graphs)
  - [Hashing](#hashing)
- [Algorithms](#algorithms)
  - [Sorting](#sorting)
    1. [Selection Sort](#selection-sort)
    2. [Insertion Sort](#insertion-sort)
    3. [Bubble](#bubble)
    4. [Merge](#merge)
    5. [Quick](#quick)
    6. [Heap](#heap)
  - [Recursion](#recursion)
- [Problems and Solutions](#problems-and-solutions)
  - [Array and Hashing](#array-and-hashing)
  - [Two pointers](#two-pointers)
  - [Sliding window](#sliding-window)
  - [Stack](#stack-1)
  - [Binary search](#binary-search)
  - [Linked list](#linked-list-1)
  - [Trees](#trees-1)
    1.erwwer
    2. sdfsdf
    3. sdfsdf
    
    - [preorder](#preorder)
    - [height](#height)
    - [diameter](#diameter)
  - [Tries](#tries-1)
  - [Backtracking](#backtracking)

## Data Structures
### Array 
- collection of items of same data type stored a contiguous memory locations
- Problems

### Linked list
- linear data structure with connected nodes
- each node contains data and pointer to next node    
- head->|data|next|->|data|next|->|data|next|->NULL  
- used in web browsers

- class
```
#include<bits/stdc++.h>
using namespace std;
class Node {
    public:
    int data;
    Node *next;

    public:
    Node(int data1, Node *next1){
        data = data1;
        next = next1;
    }
};

int main(){
    vector<int> arr = {1,2,3,4};
    Node *y = new Node(arr[0], nullptr);
    cout << y << endl;
    cout << y->data << endl;
    cout << y->next<< endl;
    return 0;
}
```
- struct
```
#include<bits/stdc++.h>
using namespace std;
struct Node {
    public:
    int data;
    Node *next;

    public:
    Node(int data1, Node *next1){
        data = data1;
        next = next1;
    }
};

```

- memory spaces used:  
- difference between Node and Node* :
- convert arrary -> linked list   
- traversal in linked list  
- lenght of a linked list  
- search an element in linked list

### Stack
- Last In First Out(LIFO)
- plates on top of each other
- 
### Queue
- First In First Out(FIFO)
### Trees
Binary tree
- root, children,ancestor, leaf nodes
- 5 types of trees  
1. full bt: every node has either has 2 or 0 children
2. complete bt: all levels completely filled except last level. 
                the last level has all nodes as left as possible
3. prefect: all leaf nodes are at same level
4. balanced: height of tree at max log(N)
5. degenerate: all nodes have one child  
- binary tree traversal
- depth first 
  - inorder : left-root-right
  - preorder: root-left-right
  - postorder:left-right-root
- level order traversal: queue and an array of array

- binary tree in C++  
```
struct Node{
  int data;
  struct Node *left;
  struct Node *right;

  Node (int val){
    data = val;
    left = right = null;
  }
}

main(){
  struct Node *root
  new_Node(1)
  root->left = Node(2)
  root->right = Node(3)
  root->left->left = Node(4)
  root->left->right = Node(5)
}
```
### Tries
### Graphs
### Hashing

## Algorithms

### Sorting
1. ### Selection Sort
2. ### Insertion sort
3. ### Bubble
4. ### Merge
5. ### Quick
6. ### Heap

### Recursion
- fuction calling itself until a specific condition
- basic problems  
  1. print anything n times

  2. print 1 to N 
    ```
    ```

  3. print from 1 to N
  4. print N to 1
  5. print 1 to N using *Backtracking*
  6. print N to 1 using *Backtracking*
- parameterised vs functional recursion
  8. reverese an array
  9. factorial
- mutiple recursion calls
  10. fibonacci
  ```
  f(n)
  {
    if (n<=1)
      return n
    last = f(n-1)
    slast = f(n-2)
    return last + slast 
  }

  ```

## Problems and Solutions
- Strategy: Brute -> Better -> Optimal
### Array and Hashing
1. Largest element
  - brute: sort and give n-1. TC = nlogn
  - optimal: largest varible, replace largest by linear search
  ```
  max = 0
  for i=0,i<n,i++
    if a[i]>largest:
      max = a[i]
    print(max)
  ```
2. Second largest
  - 3 solutions
  - brute: TC = nlogn + n
  ```
  sort array
    for i=n-2,i<=0,i--:
      if a[i] != a[n-1]
      secondl = arr[i]
      break
    return secondl
  ```
  - better : TC(2N)
  ```
  largest = 0
  for i=0,i<n,i++
    if a[i]>largest:
      largest = a[i]
  secondl = -1
  for i=0,i<n,i++:
    if secondl < a[i] and secondl != largest
      secondl = arr[i]
      break
  return secondl
  ```
  - Optimum: two variables largest and second largest
  ```
  largest = a[0]
  slargest = -1
  for i=0,i<n,i++
    if a[i]>largest:
      slargest = largest
      largest = a[i]
    else if a[i] < largest and a[i]> secondl:
      slargest = a[i]
  return slargest
  ```

### Two pointers
### Sliding window
### Stack
### Binary search
### Linked list
### Trees
1. inorder
2. #### preorder
3. postorder
4. level order
5. iterative preorder

```
while stack:
  stack.pop

```
6. iterative inorder
7. iterative postorder
8. #### height
9. balanced binary tree
10. #### diameter
11. identical trees
12. 
recursive   
height(root)   
lh = height(root.left)   
rh = height(root.righ)  
return 1+ max(lh+rh)  
### Tries
### Backtracking



## Problems and Solutions
### Array and Hashing
### Two pointers
### Sliding window
### Stack
### Binary search
### Linked list
### Trees
### Tries
### Backtracking
###
