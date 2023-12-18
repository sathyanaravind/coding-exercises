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
  - [Tries](#tries-1)
  - [Backtracking](#backtracking)

# coding-exercises
list of solutions to common coding problems

## Data Structures
### Array 
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

memory spaces used:  
difference between Node and Node* :
arrary -> linked list  
traversal in linked list  
lenght of a linked list  
search an element in linked list

### Stack
### Queue
### Trees
Binary tree
- root
- children
- ancestor
- leaf nodes

5 types of trees  
1. full bt: every node has either has 2 or 0 children
2. complete bt: all levels completely filled except last level. 
                the last level has all nodes as left as possible
3. prefect: all leaf nodes are at same level
4. balanced: height of tree at max log(N)
5. degenerate: all nodes have one child  
  
binary tree in C++  
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
