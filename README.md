# DSA Playground

A personal learning journal documenting my journey through Data Structures and Algorithms. This repository contains implementations, practice problems, and LeetCode solutions primarily written in Python.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Data Structures](#data-structures)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Linked Lists](#linked-lists)
  - [Trees](#trees)
- [Sorting Algorithms](#sorting-algorithms)
- [Search Algorithms](#search-algorithms)
- [LeetCode Problems](#leetcode-problems)
- [Classic Problems](#classic-problems)
- [Usage](#usage)
- [Progress Tracker](#progress-tracker)
- [Resources](#resources)

## Project Overview

| | |
|---|---|
| **Purpose** | Personal DSA learning and interview preparation |
| **Primary Language** | Python 3 |
| **Secondary** | JavaScript |
| **Status** | Ongoing |

## Directory Structure

```
data-structure/
├── binary-search/          # Binary search implementations
├── exercises/              # Python programming exercises
├── file/                   # File I/O practice
├── fizz-buzz/              # FizzBuzz variations
├── linkedlist/
│   ├── single/             # Singly linked list
│   ├── double/             # Doubly linked list
│   └── findLowestValue/    # Finding min value in list
├── queues/                 # Queue implementations
├── session/
│   └── week1/              # Weekly LeetCode practice
├── sort/
│   ├── bubble-sort/
│   ├── selection-sort/
│   ├── insertion-sort/
│   ├── merge-sort/
│   ├── quick-sort/
│   ├── counting-sort/
│   └── radix-sort/
├── stack/                  # Stack implementation
├── tree/
│   ├── binary-tree/        # Basic binary tree
│   ├── binary-search-tree/ # BST with all operations
│   └── avl/                # Self-balancing AVL tree
├── anagram.py              # Anagram checker
├── fibonacci.py            # Fibonacci sequence
├── palindrome.py           # Palindrome checker
└── ...
```

## Data Structures

### Stack

**Location:** `stack/day1.py`

LIFO (Last In, First Out) data structure implementation.

| Operation | Description | Time Complexity | Space Complexity |
|-----------|-------------|-----------------|------------------|
| `push(value)` | Add element to top | O(1) | O(1) |
| `pop()` | Remove and return top element | O(1) | O(1) |
| `peek()` | View top element without removal | O(1) | O(1) |
| `is_empty()` | Check if stack is empty | O(1) | O(1) |
| `size()` | Return number of elements | O(1) | O(1) |

**Use Cases:** String reversal, expression evaluation, undo operations, backtracking algorithms.

---

### Queue

**Location:** `queues/day1.py`

FIFO (First In, First Out) data structure implementation.

| Operation | Description | Time Complexity | Space Complexity |
|-----------|-------------|-----------------|------------------|
| `enqueue(value)` | Add element to back | O(n)* | O(1) |
| `dequeue()` | Remove and return front element | O(1) | O(1) |
| `is_empty()` | Check if queue is empty | O(1) | O(1) |
| `size()` | Return number of elements | O(1) | O(1) |

*\*O(n) due to `insert(0, value)` - can be optimized using `collections.deque`*

**Additional:** `queues/buyticket.py` - Queue application example.

---

### Linked Lists

#### Singly Linked List

**Location:** `linkedlist/single/day1.py`

Each node contains data and a pointer to the next node.

| Operation | Time Complexity |
|-----------|-----------------|
| Access by index | O(n) |
| Search | O(n) |
| Insert at head | O(1) |
| Insert at tail | O(n) |
| Delete | O(n) |

#### Doubly Linked List

**Location:** `linkedlist/double/day1.py`

Each node contains data and pointers to both next and previous nodes.

| Operation | Time Complexity |
|-----------|-----------------|
| Traverse forward | O(n) |
| Traverse backward | O(n) |
| Insert at head/tail | O(1) |
| Delete (given node) | O(1) |

---

### Trees

#### Binary Tree

**Location:** `tree/binary-tree/day1.py`

Basic binary tree structure where each node has at most two children.

#### Binary Search Tree (BST)

**Location:** `tree/binary-search-tree/day1.py`

BST property: Left subtree values < Node value < Right subtree values.

| Operation | Average | Worst (unbalanced) |
|-----------|---------|-------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Find Min/Max | O(log n) | O(n) |

**Implemented Traversals:**
- **Pre-order:** Root → Left → Right (used for tree copying)
- **In-order:** Left → Root → Right (returns sorted order for BST)
- **Post-order:** Left → Right → Root (used for tree deletion)

#### AVL Tree

**Location:** `tree/avl/day1.py`

Self-balancing BST invented by Adelson-Velsky and Landis (1962).

| Operation | Time Complexity |
|-----------|-----------------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

**Key Concepts:**
- Balance Factor = Height(Left Subtree) - Height(Right Subtree)
- Tree is balanced when |Balance Factor| <= 1
- **Rotations:** Left Rotate, Right Rotate, Left-Right, Right-Left

---

## Sorting Algorithms

| Algorithm | Location | Best | Average | Worst | Space | Stable |
|-----------|----------|------|---------|-------|-------|--------|
| **Bubble Sort** | `sort/bubble-sort/` | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | `sort/selection-sort/` | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | `sort/insertion-sort/` | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | `sort/merge-sort/` | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | `sort/quick-sort/` | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Counting Sort** | `sort/counting-sort/` | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| **Radix Sort** | `sort/radix-sort/` | O(nk) | O(nk) | O(nk) | O(n + k) | Yes |

**Legend:** n = number of elements, k = range of input (for counting/radix sort)

### Quick Reference

**When to use which?**

| Scenario | Recommended |
|----------|-------------|
| Small dataset (< 50 elements) | Insertion Sort |
| Nearly sorted data | Insertion Sort |
| Need guaranteed O(n log n) | Merge Sort |
| In-place sorting needed | Quick Sort |
| Integer sorting with known range | Counting/Radix Sort |
| Stability required | Merge Sort |

---

## Search Algorithms

### Binary Search

**Location:** `binary-search/day1.py`

Efficient search on **sorted** arrays by repeatedly dividing the search interval in half.

| Metric | Complexity |
|--------|------------|
| Time (Best) | O(1) |
| Time (Average) | O(log n) |
| Time (Worst) | O(log n) |
| Space (Iterative) | O(1) |
| Space (Recursive) | O(log n) |

**Implementation:** Iterative approach with left/right pointers.

---

## LeetCode Problems

### Week 1: Linked List Focus

| # | Problem | Difficulty | Location | Key Technique |
|---|---------|------------|----------|---------------|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | `session/week1/01-reverse-linkedlist.py` | Two pointers, iterative reversal |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | `session/week1/02-merge-list.py` | Dummy head, comparison |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | `session/week1/03-linked-list-cycle.py` | Floyd's Cycle Detection (fast/slow pointers) |
| 876 | [Middle of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | `session/week1/04-middle-of-the-linked-list.py` | Fast/slow pointers |
| 19 | [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | `session/week1/05-remove-nth-node-from-end-of-list.py` | Two pointers with gap |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | `exercises/add-two-numbers.py` | Linked list traversal, carry handling |

---

## Classic Problems

### Palindrome Checker

**Location:** `palindrome.py`

```python
def palindrome(word):
    word = word.lower()
    return word[::-1] == word
```
**Complexity:** O(n) time, O(n) space

---

### Anagram Checker

**Location:** `anagram.py`

```python
def anagram(source, target):
    return sorted(source.lower()) == sorted(target.lower())
```
**Complexity:** O(n log n) time (due to sorting), O(n) space

---

### FizzBuzz

**Location:** `fizz-buzz/day1.py`, `fizz-buzz/day2.py`

Classic programming problem: Print numbers 1-n, but print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.

---

### Fibonacci Sequence

**Location:** `fibonacci.py`

Recursive implementation of the Fibonacci sequence.

**Complexity:** O(2^n) time (can be optimized with memoization to O(n))

---

## Usage

### Prerequisites

- Python 3.x installed
- (Optional) Node.js for JavaScript files

### Running Examples

```bash
# Clone the repository
git clone https://github.com/yourusername/data-structure.git
cd data-structure

# Run a sorting algorithm
python sort/quick-sort/day1.py

# Test linked list implementation
python linkedlist/single/day1.py

# Run binary search
python binary-search/day1.py

# Test stack operations
python stack/day1.py

# Run tree traversals
python tree/binary-search-tree/day1.py

# Test AVL tree with rotations
python tree/avl/day1.py
```

### Running JavaScript Files

```bash
node algorithm.js
node split.js
```

---

## Progress Tracker

### Data Structures
- [x] Stack
- [x] Queue
- [x] Singly Linked List
- [x] Doubly Linked List
- [x] Binary Tree
- [x] Binary Search Tree
- [x] AVL Tree
- [ ] Red-Black Tree
- [ ] Heap / Priority Queue
- [ ] Hash Table
- [ ] Graph

### Sorting Algorithms
- [x] Bubble Sort
- [x] Selection Sort
- [x] Insertion Sort
- [x] Merge Sort
- [x] Quick Sort
- [x] Counting Sort
- [x] Radix Sort
- [ ] Heap Sort
- [ ] Tim Sort

### Search Algorithms
- [x] Binary Search
- [ ] Depth-First Search (DFS)
- [ ] Breadth-First Search (BFS)

### Advanced Topics
- [ ] Dynamic Programming
- [ ] Greedy Algorithms
- [ ] Backtracking
- [ ] Graph Algorithms (Dijkstra, BFS, DFS)

---

## Resources

### Books
- *Introduction to Algorithms* (CLRS)
- *Cracking the Coding Interview* by Gayle Laakmann McDowell

### Online Platforms
- [LeetCode](https://leetcode.com/)
- [NeetCode](https://neetcode.io/)
- [Visualgo](https://visualgo.net/) - Algorithm Visualizations

### Video Resources
- [Abdul Bari - Algorithms](https://www.youtube.com/channel/UCZCFT11CWBi3MHNlGf019nw)
- [NeetCode YouTube](https://www.youtube.com/c/NeetCode)

---

## Notes

*Space for personal learning notes and insights:*

- **Key Insight:** For linked list problems, always consider the two-pointer technique (fast/slow pointers)
- **Remember:** BST in-order traversal gives sorted output
- **AVL Tip:** Balance factor determines which rotation to apply

---

## License

This project is for personal educational purposes.

---

*Last updated: March 2026*
