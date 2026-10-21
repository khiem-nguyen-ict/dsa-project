"""Tree traversals as generator functions.

Recursive variants are provided.  Every function accepts a bare
:class:`~src.dsa.trees.node.TreeNode` root, so they work on
``BinaryTree``, ``BinarySearchTree`` and ``AVLTree`` alike.
"""


from __future__ import annotations

from typing import Any, Iterator

from src.dsa.trees.node import TreeNode
from src.dsa.linear.queue import QueueLinked


def in_order(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values left-root-right (recursive).

    Time: O(n) visits every node once.
    Space: O(h) on the call stack, where h is the tree height.
    """
    if root is None:
        return
    yield from in_order(root.left)
    yield root.value
    yield from in_order(root.right)


def pre_order(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values root-left-right (recursive).

    Time: O(n).
    Space: O(h) on the call stack.
    """
    if root is None:
        return
    yield root.value
    yield from pre_order(root.left)
    yield from pre_order(root.right)


def post_order(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values left-right-root (recursive).

    Time: O(n).
    Space: O(h) on the call stack.
    """
    if root is None:
        return
    yield from post_order(root.left)
    yield from post_order(root.right)
    yield root.value


def level_order(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values breadth-first, level by level.

    Uses :class:`QueueLinked` so no ``collections.deque`` is needed.

    Time: O(n).
    Space: O(w) where w is the maximum width of a level.
    """
    if root is None:
        return
    queue: QueueLinked = QueueLinked()
    queue.enqueue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        yield node.value
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)


