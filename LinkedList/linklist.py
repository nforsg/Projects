# A list element that stores a value of type T.
from ctypes import GetLastError
from msilib.schema import RemoveFile
from re import A
import string

class _ListElement:
    def __init__(self, _data=None):
        self._data = _data
        self._next = None

# A singly linked list of elements of type T.
class LinkedList:
    def __init__(self):
        self._first=  None      # first element in list
        self._last= None        # last element in list
        self._size = 0          # number of elements in list
    
    # Insert the given element at the end of this list.
    def addLast(self, _newdata):
        '''Worst-case time complexity: T(n) = O(1).
        new_LE is what we choose when this method is called upon in main'''
        self.healthy()
        new_LE = _ListElement(_newdata)
        if self._first == None:
            '''Then we want both the first and last element to be the same'''
            
            self._last = new_LE
            self._first = self._last
        else:
            '''new_LE is pointing at None, hence becoming the new last element in the linked list'''
            self._last._next = new_LE
            self._last = new_LE
        self._size += 1
        self.healthy()

    # Insert the given element at the beginning of this list.
    #Time complexity i O(1)
    def addFirst(self, _newdata):
        '''Worst-case time complexity: T(n) ∊ O(1). 
        new_LE is what we choose when this method is called upon in main.'''
        new_LE = _ListElement(_newdata)
        '''This element is now to point at what currently is the first element in the linked list.'''
        new_LE._next = self._first
        self.healthy()
        if self._first == None:
            '''If we add an element to the empty list, we want both the first and last element to be the same'''
            self._last = new_LE
            self._first = self._last
            #self._first = None
        else:
            '''When the pointer of the new element is directed, we simply redefine what the first element is.'''
            self._first = new_LE
        self._size+=1
        self.healthy()

    # Return the first element of this list.
    # Return null if the list is empty.
    def getFirst(self):
        '''Worst-case time complexity: T(n) ∊ O(1).
        Returns the first element in the current linked list.'''
        if self._first == None:
            '''Without this, the program would only know what to do in a "none-None" situation (haha)'''
            return None
        self.healthy()
        return self._first._data

    # Return the last element of this list.
    # Return null if the list is empty.
    def getLast(self):
        '''Worst-case time complexity: T(n) ∊ O(1). 
        Returns the last element in the current  linked list.'''
        self.healthy()
        if self._last == None:
            '''Without this, the program would only know what to do in a "none-None" situation (haha)'''
            return None
        else:
            return self._last._data

    # Return the element at the specified position in this list.
    # Return null if index is out of bounds.
    def get(self, index_int):
        '''Worst-case time complexity: T(n) ∊ O(n)
        Traverses through the list until finding the wanted element'''

        n = self._first
        i = 0
        while n:
            if i==index_int:
                return n._data
            i += 1
            n = n._next
    
    # Remove and returns the first element from this list.
    # Return null if the list is empty.
    def removeFirst(self):
        '''Worst-case time complexity: T(n) ∊ O(1).
        Removing and returning the first element in the current list, 
        knowing that None is to be returned in a None-situation'''
        self.healthy()
        while self._first != None:
            b = self._first._data
            self._first = self._first._next
            self._size -= 1
            self.healthy()
            return b
        else:
            return None
        

    # Remove all elements from this list.
    def clear(self):
        '''Worst-case time complexity: T(n) ∊ O(n)
        As we traverse through the linked list, every element passed is obliterated.'''

        while self._first != None:
            '''n = self._first
            self._first = self._first._next
            n = None'''
            self._first = None
            self._last = None
            self._size = 0
        self.healthy()
        
        
    # Return the number of elements in this list.
    def size(self):
        '''Enabling the size to be increased/decreased after each insertion/deletion.'''
        return self._size
  
    # Return a string representation of this list.
    # The elements are enclosed in square brackets ("[]").
    # Adjacent elements are separated by ", ".
    def string(self):
        '''Worst-case time complexity: T(n) ∊ O(n^2). 
        While traversing through the linked list, every element adds to the string. '''
        
        strlist = '['
        a = self._first
        b = self._last
        while a != None and a != b:
            strlist += str(a._data) + ','
            a = a._next
        if a == b and a != None:
            strlist += str(a._data)
        strlist += ']'
        print(strlist)
        return strlist
    
        '''list = []
        m = self._first
        while m != None:
            list.append(m._data)    
            m = m._next
        strlist = str(list)
        self.healthy()
        #print(strlist)
        return strlist'''
        
    def healthy(self):
        '''A method that is called upon, to make sure the size, empty list and pointer of the 
        last element is works correctly.'''
        n = self._first
        a = self._last
        m = 0
        while n != None:
            m += 1
            n = n._next
        if a != None and a._next != None:
            raise AssertionError ('The pointer of the last element must point to None')
        if m != self._size:
            raise AssertionError ('The size is not correct')
        if m == 0 and a != n:
            raise AssertionError ('For the empty list, both first and last must be None')

def main():

    '''All of the methods are being called upon with different parameters, and thereafter tested. 
    I made the tests for three data-types - ints, strings and floats, 
    the ones most commonly stored in lists'''

    '''Testing for the empty list'''
    s = LinkedList()
    f = LinkedList()
    s.removeFirst()
    s.string()
    s.clear()
    assert s.size() == 0
    assert s.removeFirst() == None
    assert s.get(0) == None
    assert s.getFirst() == None
    assert s.getLast() == None
    res1 = '[]'
    assert res1 == s.string()
    '''passed'''

    '''Testing for two addFirst- and two addLast-insertions of type string'''
    f.addFirst('A')
    f.addFirst('B')
    f.addLast('C')
    f.addLast('D') 
    
    assert f.size() == 4
    assert f.get(0) == 'B'
    assert f.get(1) == 'A'
    assert f.get(2) == 'C'
    assert f.getLast() == 'D'
    assert f.getFirst() == 'B'
    res2 = '[B,A,C,D]'
    assert res2 == f.string()
    f.clear()
    assert f.size() == 0
    assert f.getFirst() == None
    assert f.getLast() == None
    '''passed'''
    
    '''Testing for two addFirst - insertions of type int'''
    f.addFirst(1)
    f.addFirst(2)
    #f.string()
    res3 = '[2,1]'
    assert res3 == f.string()
    assert f.get(0) == 2
    assert f.get(1) == 1
    assert f.getFirst() == 2
    assert f.getLast() == 1
    assert f.size() == 2
    assert f.removeFirst() == 2
    f.clear()
    assert f.size() == 0
    '''passed'''
    
    '''Testing for two addLast-insertions of type float'''
    f.addLast(3.14)
    f.addLast(2.5)
    res4 = '[3.14,2.5]'
    assert res4 == f.string()
    assert f.get(0) == 3.14
    assert f.get(1) == 2.5
    assert f.getFirst() == 3.14
    assert f.getLast() == 2.5
    assert f.size() == 2
    f.clear() 
    assert f.size() == 0
    '''passed'''

    '''Testing for different insertion of different types'''
    f.addFirst('A')
    f.addLast(2)
    f.addFirst(3.14)
    res5 = '[3.14,A,2]'
    assert res5 == f.string()
    assert f.getFirst() == 3.14
    assert f.getLast() == 2
    assert f.get(0) == 3.14
    assert f.get(1) == 'A'
    assert f.get(2) == 2
    assert f.size() == 3
    f.clear()
    assert f.size() == 0
    '''passed'''

    '''Testing for input 0'''
    f.addFirst(0)
    f.addFirst(0)
    f.addLast(0)
    f.addLast(0)
    res6 = '[0,0,0,0]'
    assert res6 == f.string()
    assert f.getFirst() == 0
    assert f.getLast() == 0
    assert f.get(0) == 0
    assert f.get(1) == 0
    assert f.get(2) == 0
    assert f.get(3) == 0
    assert f.size() == 4
    
    f.clear()
    f.string()
    assert f.size() == 0
    assert f.get(0) == None
    assert f.getFirst() == None
    assert f.getLast() == None
    '''passed'''

  
if __name__ == '__main__': main()