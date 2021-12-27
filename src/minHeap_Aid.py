# Python3 implementation of Min Heap

import sys


# thanks to https://www.geeksforgeeks.org/min-heap-in-python/
# data structure modified to accept dictionaries
class minHeap_Aid:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = {0: -1 * sys.maxsize}
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def left_child(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def right_child(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def is_leaf(self, pos):
        if (self.size // 2) + 1 <= pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        temp = self.Heap[fpos]
        self.Heap[fpos] = self.Heap[spos]
        self.Heap[spos] = temp

    # Function to heapify the node at pos
    def min_heapify(self, pos):
        L = self.left_child(pos)
        R = self.right_child(pos)
        lowest = pos

        if L <= self.size and list(self.Heap[pos].values())[0] > list(self.Heap[L].values())[0]:
            lowest = L
        if R <= self.size and list(self.Heap[lowest].values())[0] > list(self.Heap[R].values())[0]:
            lowest = R

        if lowest != pos:
            self.swap(pos, lowest)
            self.min_heapify(lowest)

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while list(self.Heap[current].values())[0] < list(self.Heap[self.parent(current)].values())[0]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):

        for pos in range(self.size // 2, 0, -1):
            self.min_heapify(pos)

    # Function to remove and return the minimum
    # element from the heap
    def remove(self):

        if self.size == 0:
            return None
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.min_heapify(self.FRONT)
        return popped

    def peek(self):
        return self.Heap[self.FRONT]


# # Driver Code
# if __name__ == "__main__":
#
#     minHeap = minHeap_Aid(15)
#     minHeap.insert({1: 4})
#     minHeap.insert({2: 3})
#     minHeap.insert({5: 11})
#     minHeap.insert({1: 15})
#     minHeap.insert({2: 12})
#     minHeap.insert({6: 10})
#     minHeap.insert({1: 6})
#     minHeap.insert({2: 2})
#     minHeap.insert({5: 0})
#
#     while minHeap.size > 0:
#         print("The Min val is " + str(minHeap.remove()))
#     # print(minHeap.Heap)
#     # print("The Min val is " + str(minHeap.remove()))
