from Interfaces import Deque
from DLList import DLList
import numpy as np


class DLLDeque(Deque, DLList):
    def __init__(self):
        DLList.__init__(self)

    def add_first(self, x: object):
        """
        adds to the head of the list the element x
        :param x: object type; the new element
        """
        self.add(0, x)

    def add_last(self, x: object):
        """
        adds to the tail of the list the element x
        :param x: object type; the new element
        """
        self._add_before(self.dummy, x)

    def remove_first(self) -> object:
        """
        removes the head of the list and returns it
        :return: object type; the element that was removed
        """
        return self.remove(0)

    def remove_last(self) -> object:
        """
        removes the tail of the list and returns it.
        :return: object type; the element that was removed
        """
        if self.size() == 0:
            raise IndexError()
        return self._remove(self.dummy.prev)

    def clear(self):
        """
        removes all contents in the deque
        :return: None
        """
        new_deque = DLList()
        self.dummy = new_deque.dummy
        self.n = 0

    def size(self):
        """
        returns the number of elements in the deque
        :return: int type;
        """
        return DLList.size(self)
