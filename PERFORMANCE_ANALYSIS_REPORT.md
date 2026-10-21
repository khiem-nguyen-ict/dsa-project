# DSA Project — Performance Analysis Report

Generated: 2026-10-21T12:50:00.374624

## Methodology

- Sorting algorithms (`bubble_sort`, `insertion_sort`, `merge_sort`) were timed on input lists of various sizes and data distributions.
- Wall-clock time was measured with `time.perf_counter`; comparison and swap counts were captured via `OpStats`.
- Bubble and insertion sorts (O(n^2)) were capped at n=1000; merge sort was tested up to n=5000.
- Tree traversals (in-order, pre-order, post-order) were compared between recursive and explicit-stack iterative variants on BSTs of various sizes.
- Every sorted output was verified against Python's built-in `sorted()` for correctness.

## Sorting results (wall-clock time)

| Algorithm | Size | Distribution | Time | Comparisons | Swaps |
|---|---|---|---|---|---|
| bubble_sort | 100 | random | 2.97 ms | 4,740 | 2,298 |
| insertion_sort | 100 | random | 1.82 ms | 2,394 | 2,298 |
| merge_sort | 100 | random | 647.1 µs | 549 | 0 |
| bubble_sort | 100 | sorted | 57.6 µs | 99 | 0 |
| insertion_sort | 100 | sorted | 53.5 µs | 99 | 0 |
| merge_sort | 100 | sorted | 452.1 µs | 316 | 0 |
| bubble_sort | 100 | reverse | 109.94 ms | 4,950 | 4,950 |
| insertion_sort | 100 | reverse | 7.04 ms | 4,950 | 4,950 |
| merge_sort | 100 | reverse | 505.7 µs | 356 | 0 |
| bubble_sort | 100 | duplicates | 3.71 ms | 4,905 | 2,027 |
| insertion_sort | 100 | duplicates | 1.52 ms | 2,124 | 2,027 |
| merge_sort | 100 | duplicates | 616.7 µs | 534 | 0 |
| bubble_sort | 500 | random | 232.56 ms | 124,560 | 61,163 |
| insertion_sort | 500 | random | 99.02 ms | 61,657 | 61,163 |
| merge_sort | 500 | random | 5.85 ms | 3,853 | 0 |
| bubble_sort | 500 | sorted | 180.2 µs | 499 | 0 |
| insertion_sort | 500 | sorted | 266.1 µs | 499 | 0 |
| merge_sort | 500 | sorted | 5.42 ms | 2,216 | 0 |
| bubble_sort | 500 | reverse | 246.12 ms | 124,750 | 124,750 |
| insertion_sort | 500 | reverse | 180.04 ms | 124,750 | 124,750 |
| merge_sort | 500 | reverse | 3.64 ms | 2,272 | 0 |
| bubble_sort | 500 | duplicates | 214.90 ms | 124,344 | 62,758 |
| insertion_sort | 500 | duplicates | 76.73 ms | 63,254 | 62,758 |
| merge_sort | 500 | duplicates | 4.16 ms | 3,837 | 0 |
| bubble_sort | 1000 | random | 452.30 ms | 499,290 | 237,493 |
| insertion_sort | 1000 | random | 207.81 ms | 238,487 | 237,493 |
| merge_sort | 1000 | random | 10.01 ms | 8,704 | 0 |
| bubble_sort | 1000 | sorted | 378.2 µs | 999 | 0 |
| insertion_sort | 1000 | sorted | 456.1 µs | 999 | 0 |
| merge_sort | 1000 | sorted | 5.51 ms | 4,932 | 0 |
| bubble_sort | 1000 | reverse | 565.16 ms | 499,500 | 499,500 |
| insertion_sort | 1000 | reverse | 553.16 ms | 499,500 | 499,500 |
| merge_sort | 1000 | reverse | 10.70 ms | 5,044 | 0 |
| bubble_sort | 1000 | duplicates | 404.27 ms | 497,484 | 237,478 |
| insertion_sort | 1000 | duplicates | 240.96 ms | 238,474 | 237,478 |
| merge_sort | 1000 | duplicates | 10.70 ms | 8,710 | 0 |
| merge_sort | 2000 | random | 26.88 ms | 19,428 | 0 |
| merge_sort | 2000 | sorted | 11.72 ms | 10,864 | 0 |
| merge_sort | 2000 | reverse | 23.13 ms | 11,088 | 0 |
| merge_sort | 2000 | duplicates | 23.85 ms | 19,408 | 0 |
| merge_sort | 5000 | random | 65.00 ms | 55,192 | 0 |
| merge_sort | 5000 | sorted | 35.52 ms | 29,804 | 0 |
| merge_sort | 5000 | reverse | 43.83 ms | 32,004 | 0 |
| merge_sort | 5000 | duplicates | 73.81 ms | 55,255 | 0 |

### Sorting observations

- **Merge sort** is consistently the fastest for medium and large inputs (O(n log n)) and is unaffected by input distribution.
- **Bubble sort** and **insertion sort** are O(n^2): they are competitive only on very small or already-sorted inputs, and degrade sharply on reverse-sorted data.
- **Insertion sort** is typically faster than bubble sort in practice because it performs fewer swaps (shifts instead of exchanges).
- All three algorithms are stable: equal keys preserve their original relative order.

## Tree traversal results (wall-clock time)

| Traversal | Variant | Size | Time |
|---|---|---|---|
| in_order | recursive | 100 | 218.5 µs |
| in_order | iterative | 100 | 181.1 µs |
| pre_order | recursive | 100 | 135.6 µs |
| pre_order | iterative | 100 | 150.1 µs |
| post_order | recursive | 100 | 645.6 µs |
| post_order | iterative | 100 | 257.1 µs |
| in_order | recursive | 500 | 687.6 µs |
| in_order | iterative | 500 | 657.5 µs |
| pre_order | recursive | 500 | 705.2 µs |
| pre_order | iterative | 500 | 653.0 µs |
| post_order | recursive | 500 | 7.22 ms |
| post_order | iterative | 500 | 2.12 ms |
| in_order | recursive | 1000 | 1.49 ms |
| in_order | iterative | 1000 | 1.50 ms |
| pre_order | recursive | 1000 | 2.86 ms |
| pre_order | iterative | 1000 | 1.35 ms |
| post_order | recursive | 1000 | 2.14 ms |
| post_order | iterative | 1000 | 2.82 ms |
| in_order | recursive | 2000 | 3.29 ms |
| in_order | iterative | 2000 | 3.74 ms |
| pre_order | recursive | 2000 | 3.05 ms |
| pre_order | iterative | 2000 | 7.63 ms |
| post_order | recursive | 2000 | 7.07 ms |
| post_order | iterative | 2000 | 7.08 ms |
| in_order | recursive | 5000 | 9.20 ms |
| in_order | iterative | 5000 | 13.96 ms |
| pre_order | recursive | 5000 | 8.57 ms |
| pre_order | iterative | 5000 | 9.58 ms |
| post_order | recursive | 5000 | 10.53 ms |
| post_order | iterative | 5000 | 19.82 ms |

### Traversal observations

- Recursive and iterative traversals both run in O(n) time and produce identical sequences.
- Recursive traversals use O(h) call-stack space; iterative traversals use O(h) explicit-stack space.
- For balanced trees h = O(log n); for skewed BSTs h = O(n), so recursive depth can become a practical limit.

## Space complexity summary

| Structure / Algorithm | Auxiliary space | Notes |
|---|---|---|
| DynamicArray | O(1) amortized append | O(n) occasional resize |
| SinglyLinkedList | O(1) per node | O(n) total for n nodes |
| StackArray / StackLinked | O(1) per push | StackLinked allocates a node per push |
| QueueLinked | O(1) per enqueue | |
| BinarySearchTree | O(1) per node | O(h) recursion for insert/delete |
| AVLTree | O(1) per node | O(log n) recursion depth when balanced |
| ChainingHashTable | O(1) amortized | Buckets plus occasional O(n) resize |
| OpenAddressingHashTable | O(1) amortized | Slot array plus occasional O(n) resize |
| bubble_sort / insertion_sort / merge_sort | O(n) | Each returns a new sorted list |
| linear_search | O(1) | In-place scan |
| binary_search_iterative | O(1) | In-place halving |
| binary_search_recursive | O(log n) | Call-stack depth |

## Time complexity summary

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| DynamicArray append | O(1) | O(1) amortized | O(n) on resize |
| DynamicArray insert/delete/get | O(n) / O(n) / O(1) | — | — |
| SinglyLinkedList insert_head/append | O(1) / O(1) | — | — |
| SinglyLinkedList insert_at/delete/search | O(n) | — | — |
| Stack push/pop/peek | O(1) | — | — |
| Queue enqueue/dequeue/peek | O(1) | — | — |
| BST insert/search/delete | O(h) | O(log n) balanced | O(n) skewed |
| AVL insert/search/delete | O(log n) | O(log n) | O(log n) |
| Tree traversal (any order) | O(n) | O(n) | O(n) |
| ChainingHashTable put/get/remove | O(1) avg | O(1) avg | O(n) worst (all collide) |
| OpenAddressingHashTable put/get/remove | O(1) avg | O(1) avg | O(n) worst (full probe) |
| bubble_sort | O(n) | O(n^2) | O(n^2) |
| insertion_sort | O(n) | O(n^2) | O(n^2) |
| merge_sort | O(n log n) | O(n log n) | O(n log n) |
| linear_search | O(1) | O(n) | O(n) |
| binary_search | O(1) | O(log n) | O(log n) |

## Conclusion

- Use **merge sort** for general-purpose sorting of medium/large inputs.
- Use **insertion sort** only for tiny or nearly-sorted inputs.
- Prefer a **balanced tree (AVL)** when sorted-order operations must remain O(log n) on adversarial/sorted input; a plain BST degenerates to O(n).
- Recursive and iterative traversals are equivalent in result and asymptotic time; choose recursive for clarity, iterative when stack depth is a concern.
- Hash tables give O(1) average-case put/get/remove; choose separate chaining for simplicity or open addressing for lower memory overhead when load factor is kept low.