"""Queue implementations: linked-list and circular-array backed."""

from __future__ import annotations

from typing import Any, Iterator

from src.dsa.linear.linked_list import _Node


class QueueLinked:
    """A FIFO queue backed by a singly linked list with head/tail pointers.

    Enqueue appends at the tail and dequeue removes from the head, so both
    operations are O(1).
    """

    def __init__(self) -> None:
        self._head: _Node | None = None
        self._tail: _Node | None = None
        self._size: int = 0

    def enqueue(self, value: Any) -> None:
        """Add ``value`` to the tail of the queue.

        Time: O(1).
        Space: O(1).
        """
        node = _Node(value)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self) -> Any:
        """Remove and return the head value; raise ``IndexError`` if empty.

        Time: O(1).
        Space: O(1).
        """
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self) -> Any:
        """Return the head value without removing it.

        Time: O(1).
        Space: O(1).
        """
        if self._head is None:
            raise IndexError("peek from empty queue")
        return self._head.value

    def is_empty(self) -> bool:
        """Return ``True`` when the queue holds no elements."""
        return self._head is None

    def size(self) -> int:
        """Return the number of elements currently in the queue."""
        return self._size

    def __iter__(self) -> Iterator[Any]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size


class QueueCircularArray:
    """A FIFO queue backed by a circular plain-list buffer.

    The buffer is a plain ``[None] * capacity`` list with head/tail indices
    that wrap around modulo the capacity.  When the buffer is full it is
    grown (doubled) and the elements are re-laid-out in order; this is
    grow-only, matching the project's no-shrink policy.
    """

    DEFAULT_CAPACITY: int = 8
    GROW_FACTOR: int = 2

    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        # Plain list used purely as raw fixed-capacity storage.
        self._storage: list[Any] = [None] * capacity
        self._head: int = 0
        self._size: int = 0

    @property
    def _capacity(self) -> int:
        return len(self._storage)

    @property
    def _tail(self) -> int:
        # Index of the slot where the *next* enqueue will land.
        return (self._head + self._size) % self._capacity

    def enqueue(self, value: Any) -> None:
        """Add ``value`` to the tail of the queue, growing if full.

        Time: amortized O(1), worst case O(n) on a grow.
        Space: O(1) amortized.
        """
        if self._size == self._capacity:
            self._grow()
        self._storage[self._tail] = value
        self._size += 1

    def dequeue(self) -> Any:
        """Remove and return the head value; raise ``IndexError`` if empty.

        Time: O(1).
        Space: O(1).
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._storage[self._head]
        self._storage[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return value

    def peek(self) -> Any:
        """Return the head value without removing it.

        Time: O(1).
        Space: O(1).
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._storage[self._head]

    def is_empty(self) -> bool:
        """Return ``True`` when the queue holds no elements."""
        return self._size == 0

    def size(self) -> int:
        """Return the number of elements currently in the queue."""
        return self._size

    def _grow(self) -> None:
        """Allocate a larger buffer and re-lay-out elements in order."""
        new_capacity = self.GROW_FACTOR * self._capacity
        new_storage: list[Any] = [None] * new_capacity
        # Copy live elements starting at index 0 of the new buffer.
        for i in range(self._size):
            new_storage[i] = self._storage[(self._head + i) % self._capacity]
        self._storage = new_storage
        self._head = 0

    def __iter__(self) -> Iterator[Any]:
        for i in range(self._size):
            yield self._storage[(self._head + i) % self._capacity]

    def __len__(self) -> int:
        return self._size