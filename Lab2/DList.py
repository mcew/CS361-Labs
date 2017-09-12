# ----------------------------------------------------------------------
# DList.py
# Tom Green
# ----------------------------------------------------------------------

import sys

from DListNode import *


# ----------------------------------------------------------------------

class DList:
    '''implementation of subset of Python built-in list API using
    a doubly linked list'''

    # List implemented as doubly linked nodes
    # invariant:
    # self.size indicates the number of items in the list
    # if self.size == 0, self.head is None otherwise
    # self.head is a reference to the first DListNode in list
    # self.tail is a reference to the last DListNode in the list to
    #   make the append operation efficient
    # preconditions for each method are indicated by the assert test

    # ------------------------------------------------------------------

    def __init__(self, seq=None):

        '''creates an empty list'''

        self.head = None
        self.tail = None
        self.size = 0

        if seq is not None:
            for i in seq:
                self.append(i)

    # ------------------------------------------------------------------

    def __len__(self):

        '''returns number of items in the list'''

        return self.size

    # ------------------------------------------------------------------

    def __iter__(self):

        '''forward iterator'''

        node = self.head
        while node is not None:
            yield node.item
            node = node.next

    # ------------------------------------------------------------------

    def _find(self, position):

        '''private method that returns node that is at location position
        in the list;
        for non negative positions, 0 is first item, size-1 is last item
        for negative positions, -1 is the last item -size is the first
        item'''

        if self.head:
            if position >= 0 and position < self.size:
                node = self.head
                for i in range(position):
                    node = node.next
                return node
            elif position < 0 and position >= -self.size:
                node = self.tail
                for i in range(-position):
                    node = node.prev
                return node
            else:
                raise ValueError
        else:
            raise ValueError

    # ------------------------------------------------------------------

    def __getitem__(self, position):

        '''return data item at location position'''

        node = self._find(position)
        return node.item

    # ------------------------------------------------------------------

    def __setitem__(self, position, value):

        '''set data item at location position to value'''

        node = self._find(position)
        node.item = value

    # ------------------------------------------------------------------

    def __delitem__(self, position):

        '''delete item at location position from the list'''

        self._delete(position)

    # ------------------------------------------------------------------

    def _delete(self, position):

        '''private method to delete item at location position from the list'''

        if self.head:
            node = self._find(position)
            if self.size == 1:
                self.head = None
                self.tail = None
            elif node is self.head:
                node.next.prev = None
                self.head = node.next
            elif node is self.tail:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.size -= 1
            return node.item
        else:
            raise ValueError

    # ------------------------------------------------------------------

    def append(self, x):

        '''appends x onto end of the list'''

        newNode = DListNode(x, self.tail)
        if self.size == 0:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    # ------------------------------------------------------------------

    def insert(self, i, x):

        '''inserts x before position i in the list'''

        newNode = DListNode(x)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        elif i == self.size:
            self.append(x)
        elif i == 0:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            node = self._find(i)
            newNode.next = node
            newNode.prev = node.prev
            node.prev.next = newNode
            node.prev = newNode
        self.size += 1

    # ------------------------------------------------------------------

    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item'''

        if i is None:
            i = self.size - 1
        return self._delete(i)

    # ------------------------------------------------------------------

    def remove(self, x):

        '''removes the first instance of x from the list'''

        self._delete(self.index(x))

    # ------------------------------------------------------------------

    def __min__(self):

        '''return minimum element in the list'''

        if self.head:
            node = self.head
            min = node.item
            while node:
                if node.item < min:
                    min = node.item
                node = node.next
            return min
        else:
            raise ValueError

    # ------------------------------------------------------------------

    def __max__(self):

        '''return maximum element in the list'''

        if self.head:
            node = self.head
            max = node.item
            while node:
                if node.item > max:
                    max = node.item
                node = node.next
            return max
        else:
            raise ValueError

    # ------------------------------------------------------------------

    def extend(self, l):

        '''add each element of list l onto the list'''

        for i in l:
            self.append(i)

    # ------------------------------------------------------------------

    def count(self, x):

        '''return number of occurrences of x in the list'''
        node = self.head
        count = 0
        while node:
            if node.item == x:
                count += 1
            node = node.next
        return count

    # ------------------------------------------------------------------

    def index(self, x, start=0):

        '''return position of first occurence of x in the list starting
        at position start'''

        node = self._find(start)
        pos = start
        while node and node.item != x:
            node = node.next
            pos += 1
        if node == None:
            raise ValueError
        else:
            return pos

    # ------------------------------------------------------------------

    def reverse_iter(self):

        '''iterate over items in reverse'''

        node = self.tail
        while node is not None:
            yield node.item
            node = node.prev

# ----------------------------------------------------------------------
