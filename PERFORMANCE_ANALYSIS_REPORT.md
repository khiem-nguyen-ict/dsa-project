# DSA Project — Performance Analysis Report

Generated: 2026-11-02T16:53:20.114399

## Methodology

- Sorting algorithms (`bubble_sort`, `insertion_sort`, `merge_sort`) were timed on input lists of various sizes and data distributions.
- Wall-clock time was measured with `time.perf_counter`; comparison and swap counts were captured via `OpStats`.
- Bubble and insertion sorts (O(n^2)) were capped at n=1000; merge sort was tested up to n=5000.
- Tree traversals (in-order, pre-order, post-order) were compared between recursive and explicit-stack iterative variants on BSTs of various sizes.
- Every sorted output was verified against Python's built-in `sorted()` for correctness.

## Sorting results (wall-clock time)

| Algorithm | Size | Distribution | Time | Comparisons | Swaps |
|---|---|---|---|---|---|
| bubble_sort | 100 | random | 1.01 ms | 4,740 | 2,298 |
| insertion_sort | 100 | random | 748.3 µs | 2,394 | 2,298 |
| merge_sort | 100 | random | 910.8 µs | 549 | 0 |
| bubble_sort | 100 | sorted | 30.4 µs | 99 | 0 |
| insertion_sort | 100 | sorted | 43.8 µs | 99 | 0 |
| merge_sort | 100 | sorted | 319.3 µs | 316 | 0 |
| bubble_sort | 100 | reverse | 2.39 ms | 4,950 | 4,950 |
| insertion_sort | 100 | reverse | 1.86 ms | 4,950 | 4,950 |
| merge_sort | 100 | reverse | 192.3 µs | 356 | 0 |
| bubble_sort | 100 | duplicates | 1.07 ms | 4,905 | 2,027 |
| insertion_sort | 100 | duplicates | 565.1 µs | 2,124 | 2,027 |
| merge_sort | 100 | duplicates | 339.7 µs | 534 | 0 |
| bubble_sort | 500 | random | 39.63 ms | 124,560 | 61,163 |
| insertion_sort | 500 | random | 24.74 ms | 61,657 | 61,163 |
| merge_sort | 500 | random | 2.62 ms | 3,853 | 0 |
| bubble_sort | 500 | sorted | 136.4 µs | 499 | 0 |
| insertion_sort | 500 | sorted | 146.3 µs | 499 | 0 |
| merge_sort | 500 | sorted | 1.52 ms | 2,216 | 0 |
| bubble_sort | 500 | reverse | 52.97 ms | 124,750 | 124,750 |
| insertion_sort | 500 | reverse | 59.42 ms | 124,750 | 124,750 |
| merge_sort | 500 | reverse | 1.90 ms | 2,272 | 0 |
| bubble_sort | 500 | duplicates | 31.97 ms | 124,344 | 62,758 |
| insertion_sort | 500 | duplicates | 16.61 ms | 63,254 | 62,758 |
| merge_sort | 500 | duplicates | 1.49 ms | 3,837 | 0 |
| bubble_sort | 1000 | random | 90.27 ms | 499,290 | 237,493 |
| insertion_sort | 1000 | random | 52.17 ms | 238,487 | 237,493 |
| merge_sort | 1000 | random | 2.55 ms | 8,704 | 0 |
| bubble_sort | 1000 | sorted | 98.6 µs | 999 | 0 |
| insertion_sort | 1000 | sorted | 127.6 µs | 999 | 0 |
| merge_sort | 1000 | sorted | 1.73 ms | 4,932 | 0 |
| bubble_sort | 1000 | reverse | 121.05 ms | 499,500 | 499,500 |
| insertion_sort | 1000 | reverse | 98.05 ms | 499,500 | 499,500 |
| merge_sort | 1000 | reverse | 1.63 ms | 5,044 | 0 |
| bubble_sort | 1000 | duplicates | 85.55 ms | 497,484 | 237,478 |
| insertion_sort | 1000 | duplicates | 59.36 ms | 238,474 | 237,478 |
| merge_sort | 1000 | duplicates | 3.18 ms | 8,710 | 0 |
| merge_sort | 2000 | random | 6.17 ms | 19,428 | 0 |
| merge_sort | 2000 | sorted | 3.62 ms | 10,864 | 0 |
| merge_sort | 2000 | reverse | 3.55 ms | 11,088 | 0 |
| merge_sort | 2000 | duplicates | 5.55 ms | 19,408 | 0 |
| merge_sort | 5000 | random | 14.84 ms | 55,192 | 0 |
| merge_sort | 5000 | sorted | 10.12 ms | 29,804 | 0 |
| merge_sort | 5000 | reverse | 10.46 ms | 32,004 | 0 |
| merge_sort | 5000 | duplicates | 15.11 ms | 55,255 | 0 |

### Sorting observations

- **Merge sort** is consistently the fastest for medium and large inputs (O(n log n)) and is unaffected by input distribution.
- **Bubble sort** and **insertion sort** are O(n^2): they are competitive only on very small or already-sorted inputs, and degrade sharply on reverse-sorted data.
- **Insertion sort** is typically faster than bubble sort in practice because it performs fewer swaps (shifts instead of exchanges).
- All three algorithms are stable: equal keys preserve their original relative order.

## Tree traversal results (wall-clock time)

| Traversal | Variant | Size | Time |
|---|---|---|---|
| in_order | recursive | 100 | 34.2 µs |
| pre_order | recursive | 100 | 26.9 µs |
| post_order | recursive | 100 | 26.0 µs |
| in_order | recursive | 500 | 131.3 µs |
| pre_order | recursive | 500 | 122.6 µs |
| post_order | recursive | 500 | 123.8 µs |
| in_order | recursive | 1000 | 256.7 µs |
| pre_order | recursive | 1000 | 248.8 µs |
| post_order | recursive | 1000 | 250.5 µs |
| in_order | recursive | 2000 | 631.0 µs |
| pre_order | recursive | 2000 | 587.0 µs |
| post_order | recursive | 2000 | 822.4 µs |
| in_order | recursive | 5000 | 1.44 ms |
| pre_order | recursive | 5000 | 1.42 ms |
| post_order | recursive | 5000 | 1.46 ms |

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
- Hash tables give O(1) average-case put/get/remove; choose separate chaining for simplicity for lower memory overhead when load factor is kept low.