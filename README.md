# DSA Project

A runnable Python "Data Structures and Algorithms" project. Every structure
is implemented from scratch using only the Python standard library -- no
`collections.deque`, `heapq`, `bisect`, `dict`, or `set` inside the hash
tables, and no `list.sort()`/`sorted()` inside the algorithms.

## Layout

- `src/dsa/` -- the library: linear structures, trees, hashing, sorting, searching.
- `scenarios/` -- runnable demo programs, one per structure area.
- `main.py` -- argparse entry point that runs the scenarios.

## Run

From the project root:

```bash
python main.py                # run every scenario
python main.py --scenario dynamic_array_grades   # run a single scenario
python scenarios/bst_student_records.py          # run a scenario directly
```

Each scenario also has a `main()` and can be run on its own.