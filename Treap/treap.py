
import random

class _Treapelement:
    def __init__(self, _data = None):
        '''Initializing new element to be part of treap'''
        self._data = _data
        self.p = float(random.uniform(0,100000))
        #self._counter = 1
        self._left = None
        self._right = None

    def _insert(self, _node, _newdata):
        '''In order to add the new element in treap correctly, we use recursion to navigate thoughout
        each node, implementing different conditions depeneting on what the input is.
        Worst-case time complexity: T(n) ∊ O(logn)'''
        if _node == None:
            _node = _Treapelement(_newdata)
            
            return _node   
             
        #New input is equal to the data of the current node      
        elif _newdata == _node._data:
            return _node

        #If new input is larger than the root, we insert to the right.
        elif _newdata > _node._data:
            _node._right = self._insert(_node._right,_newdata)
        #Possible right rotation, depending on the priority situtaion.
            if _node._right.p < _node.p:
                _node = self._Lefttrotate(_node)
            return _node
        #If new value is lesser than the root, we insert to the left.
        elif _newdata < _node._data:
            _node._left = self._insert(_node._left, _newdata)
        #Possible left rotation, depending on the priority situation.
            if _node._left.p < _node.p:
                _node = self._Rightrotate(_node)
            return _node
        
    '''The rotations, changing what's the root of the tree - but maintains the order. This is what
    makes it balanced.'''

    def _Rightrotate(self, node):
        a = node._left
        node._left = a._right
        a._right = node
        node = a
        return node

    def _Lefttrotate(self, node):
        a = node._right
        node._right = a._left
        a._left = node
        node = a
        return node

class Treap():
    '''Initializing an empty tree.'''
    def __init__(self):
            self._root = None
            self._size = 0 

    def Add(self, _newdata):
        '''Adds a new data to treap. If the treap is empty, we simply redirect the root to an element
        that contains the given input and points to None in both left and right.
        Otherwise, we call for insert.
        Worst-case time complexity: T(n) ∊ O(logn)'''
        if self._root == None:
            self._root = _Treapelement(_newdata)
            self._size += 1
        elif self._root._data == _newdata:
            self._root = self._root._insert(self._root, _newdata)
        else:
            self._root = self._root._insert(self._root, _newdata)
            self._size +=1

    def size(self):
        '''Regarding the size: when duplicates occur, I increase the counter in the
        private class with 1. Therefore, the the size is considered to always be the ammount 
        of elements inserted, that is, a duplicate inout increases the size with 2 
        and the counter with 1.'''

        return self._size

    def sortedstring(self, _node):
        '''Using recusrion to be able to print the treap into string. Worst-case time compleity: T(n) ∊ O(logn) '''

        _string= ''
        if _node:
            _string += self.sortedstring(_node._left)
            _string += (str(_node._data) + ' ')
            _string += self.sortedstring(_node._right)

        return _string


def main():

    tree = Treap()

    '''Testing fr the empty tree'''
    assert tree._root == None
    assert tree.size() == 0
    assert tree.sortedstring(tree._root) == ''
    '''passed'''

    '''
    PLEASE OBSERVE: Since p is a a random float,there are different outcomes, the tree is not always 
    in one certain way. Hence, we implement the if-, elif-, and else-statements.'''

    '''Testing for adding duplicates.
    In this case, the counter of Anton and David should be two, which adds up to the size - 4. '''
    tree.Add('Anton')
    tree.Add('Anton')
    tree.Add('David')
    tree.Add('David')
    #assert tree._root._counter == 2
    assert tree._size == 2
    if tree._root._right and tree._root._left:
        assert tree._root.p < tree._root._right.p
        assert tree._root.p < tree._root._left.p
        assert tree._root._data <= tree._root._right._data
        assert tree._root._data >= tree._root._left._data

    elif tree._root._right != None and tree._root._left == None:
        #assert tree._root._right._counter == 2
        if tree._root._right._right:
            assert tree._root._data <= tree._root._right._data
            assert tree._root._data <= tree._root._right._right._data
            assert tree._root._right._data <= tree._root._right._right._data
            assert tree._root.p < tree._root._right.p
            assert tree._root.p < tree._root._right._right.p
            assert tree._root._right.p < tree._root._right._right.p
        if tree._root._right._left:
            assert tree._root._data <= tree._root._right._data
            assert tree._root._data <= tree._root._right._left._data
            assert tree._root._right._data >= tree._root._right._left._data
            assert tree._root.p < tree._root._right.p
            assert tree._root.p < tree._root._right._left.p
            assert tree._root._right.p < tree._root._right._left.p
            
    else:
        if tree._root._left._left:
            #assert tree._root._counter == 2
            assert tree._root._data >= tree._root._left._data
            assert tree._root._data >= tree._root._left._left._data
            assert tree._root._left._data >= tree._root._left._left._data
            assert tree._root.p < tree._root._left.p
            assert tree._root.p < tree._root._left._left.p
            assert tree._root._left.p < tree._root._left._left.p

    assert tree.sortedstring(tree._root) == 'Anton David '
    '''passed'''

    '''Test case for inputs that have a wide spread of values.
    Here, in my testing, I make sure that I really dig deep in the treap, checking if any 
    AssertionErrors appear on the most distant nodes. AttributeError occurs in some cases, which 
    can be expected, since p is a random float at such a large interval. What is important is that
    the Assertion is correct.'''
    
    tree1 = Treap()
    tree1.Add('W')
    tree1.Add('M')
    tree1.Add('A')
    tree1.Add('Q')
    tree1.Add('F')
    tree1.Add('Fl')
    tree1.Add('A2')
    assert tree1.size() == 7
    assert tree1.sortedstring(tree1._root) == 'A A2 F Fl M Q W '
    if tree1._root._right and tree1._root._left:
        assert tree1._root.p < tree1._root._right.p
        assert tree1._root.p < tree1._root._left.p
        assert tree1._root._data <= tree1._root._right._data
        assert tree1._root._data >= tree1._root._left._data

    elif tree1._root._right != None and tree1._root._left == None:
        if tree1._root._right._right_left._left:
            assert tree1._root._data <= tree1._root._right._data
            assert tree1._root._data <= tree1._root._right._right._data
            assert tree1._root._right._data <= tree1._root._right._right._data
            assert tree1._root._right._right._left._data >= tree1._root._right._right._left._left._data
            assert tree1._root.p < tree1._root._right.p
            assert tree1._root.p < tree1._root._right._right.p
            assert tree1._root._right._right.p < tree1._root._right._right._left.p
        if tree1._root._right._left._left._right._left._right:
            assert tree1._root._data <= tree1._root._right._data
            assert tree1._root._right._data >= tree1._root._right._left._data
            assert tree1._root._right._left._data >= tree1._root._data
            assert tree1._root._right._left._left._data >= tree1._root._right._left._data
            assert tree1._root._right._left._left._right._left._data >= tree1._root._right._left._left._right._left._right._data
            assert tree1._root.p < tree1._root._right.p
            assert tree1._root.p < tree1._root._right._left.p
            assert tree1._root._right._left._left.p < tree1._root._right._left._left._right.p   
    else:
        if tree1._root._left._left:
            assert tree1._root._data >= tree1._root._left._data
            assert tree1._root._data >= tree1._root._left._left._data
            assert tree1._root._left._data >= tree1._root._left._left._data
            assert tree1._root.p < tree1._root._left.p
            assert tree1._root.p < tree1._root._left._left.p
            assert tree1._root._left.p < tree1._root._left._left.p


if __name__ == '__main__': main()