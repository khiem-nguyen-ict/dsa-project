# DSA Project — Performance Analysis Report

Generated: 2026-10-24T06:26:21.337992

## Methodology

- Sorting algorithms (`bubble_sort`, `insertion_sort`, `merge_sort`) were timed on input lists of various sizes and data distributions.
- Wall-clock time was measured with `time.perf_counter`; comparison and swap counts were captured via `OpStats`.
- Bubble and insertion sorts (O(n^2)) were capped at n=1000; merge sort was tested up to n=5000.
- Tree traversals (in-order, pre-order, post-order) were compared between recursive and explicit-stack iterative variants on BSTs of various sizes.
- Every sorted output was verified against Python's built-in `sorted()` for correctness.

## Sorting results (wall-clock time)

| Algorithm | Size | Distribution | Time | Comparisons | Swaps |
|---|---|---|---|---|---|
| bubble_sort | 100 | random | 960.3 µs | 4,740 | 2,298 |
| insertion_sort | 100 | random | 575.3 µs | 2,394 | 2,298 |
| merge_sort | 100 | random | 228.4 µs | 549 | 0 |
| bubble_sort | 100 | sorted | 14.4 µs | 99 | 0 |
| insertion_sort | 100 | sorted | 17.4 µs | 99 | 0 |
| merge_sort | 100 | sorted | 156.9 µs | 316 | 0 |
| bubble_sort | 100 | reverse | 1.42 ms | 4,950 | 4,950 |
| insertion_sort | 100 | reverse | 1.21 ms | 4,950 | 4,950 |
| merge_sort | 100 | reverse | 176.2 µs | 356 | 0 |
| bubble_sort | 100 | duplicates | 918.8 µs | 4,905 | 2,027 |
| insertion_sort | 100 | duplicates | 502.8 µs | 2,124 | 2,027 |
| merge_sort | 100 | duplicates | 294.6 µs | 534 | 0 |
| bubble_sort | 500 | random | 28.49 ms | 124,560 | 61,163 |
| insertion_sort | 500 | random | 16.86 ms | 61,657 | 61,163 |
| merge_sort | 500 | random | 1.65 ms | 3,853 | 0 |
| bubble_sort | 500 | sorted | 65.9 µs | 499 | 0 |
| insertion_sort | 500 | sorted | 84.7 µs | 499 | 0 |
| merge_sort | 500 | sorted | 995.4 µs | 2,216 | 0 |
| bubble_sort | 500 | reverse | 39.72 ms | 124,750 | 124,750 |
| insertion_sort | 500 | reverse | 45.54 ms | 124,750 | 124,750 |
| merge_sort | 500 | reverse | 1.71 ms | 2,272 | 0 |
| bubble_sort | 500 | duplicates | 33.39 ms | 124,344 | 62,758 |
| insertion_sort | 500 | duplicates | 101.17 ms | 63,254 | 62,758 |
| merge_sort | 500 | duplicates | 2.04 ms | 3,837 | 0 |
| bubble_sort | 1000 | random | 199.76 ms | 499,290 | 237,493 |
| insertion_sort | 1000 | random | 75.72 ms | 238,487 | 237,493 |
| merge_sort | 1000 | random | 3.47 ms | 8,704 | 0 |
| bubble_sort | 1000 | sorted | 135.0 µs | 999 | 0 |
| insertion_sort | 1000 | sorted | 177.0 µs | 999 | 0 |
| merge_sort | 1000 | sorted | 3.11 ms | 4,932 | 0 |
| bubble_sort | 1000 | reverse | 148.72 ms | 499,500 | 499,500 |
| insertion_sort | 1000 | reverse | 134.44 ms | 499,500 | 499,500 |
| merge_sort | 1000 | reverse | 2.41 ms | 5,044 | 0 |
| bubble_sort | 1000 | duplicates | 112.73 ms | 497,484 | 237,478 |
| insertion_sort | 1000 | duplicates | 71.30 ms | 238,474 | 237,478 |
| merge_sort | 1000 | duplicates | 3.48 ms | 8,710 | 0 |
| merge_sort | 2000 | random | 7.09 ms | 19,428 | 0 |
| merge_sort | 2000 | sorted | 4.54 ms | 10,864 | 0 |
| merge_sort | 2000 | reverse | 4.89 ms | 11,088 | 0 |
| merge_sort | 2000 | duplicates | 7.01 ms | 19,408 | 0 |
| merge_sort | 5000 | random | 19.64 ms | 55,192 | 0 |
| merge_sort | 5000 | sorted | 12.26 ms | 29,804 | 0 |
| merge_sort | 5000 | reverse | 13.24 ms | 32,004 | 0 |
| merge_sort | 5000 | duplicates | 18.52 ms | 55,255 | 0 |

### Sorting observations

- **Merge sort** is consistently the fastest for medium and large inputs (O(n log n)) and is unaffected by input distribution.
- **Bubble sort** and **insertion sort** are O(n^2): they are competitive only on very small or already-sorted inputs, and degrade sharply on reverse-sorted data.
- **Insertion sort** is typically faster than bubble sort in practice because it performs fewer swaps (shifts instead of exchanges).
- All three algorithms are stable: equal keys preserve their original relative order.

## Tree traversal results (wall-clock time)

| Traversal | Variant | Size | Time |
|---|---|---|---|
| in_order | recursive | 100 | 39.8 µs |
| pre_order | recursive | 100 | 32.8 µs |
| post_order | recursive | 100 | 31.9 µs |
| in_order | recursive | 500 | 160.7 µs |
| pre_order | recursive | 500 | 159.6 µs |
| post_order | recursive | 500 | 152.6 µs |
| in_order | recursive | 1000 | 358.9 µs |
| pre_order | recursive | 1000 | 375.5 µs |
| post_order | recursive | 1000 | 455.9 µs |
| in_order | recursive | 2000 | 784.9 µs |
| pre_order | recursive | 2000 | 708.1 µs |
| post_order | recursive | 2000 | 700.9 µs |
| in_order | recursive | 5000 | 1.75 ms |
| pre_order | recursive | 5000 | 1.73 ms |
| post_order | recursive | 5000 | 1.92 ms |

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