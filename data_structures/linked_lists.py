'''
Created on 24-Sep-2017

@author: Nag
'''

from data_structures.dsExceptions import DSEmpty

class Node(object):
    '''
    Represents the node of a class
    '''


    def __init__(self, data):
        '''
        Used to initialize the data and next reference node 
        '''
        self.data = data
        self.next = None
        
    
class LinkedList(object):
    """
    used to perform the linked list operations
    """
    
    def __init__(self, *data):
        '''
        initialize the head of linked list
        '''
        self.head = None
        if len(data) > 0:
            for element in data[::-1]:
                self.insert(element)
            
    
    def insert(self, data):
        '''
        adds an new element to linked list
        
        :param data: element to be added
        :type data: object/element
        '''
        
        node = Node(data)
        node.next = self.head
        self.head = node 
    
    def search(self, data):
        """
        used to search for an existence of an element
        
        :param data: element to search for existence in linked list
        :type data: object/element
        """
        node = self.head 
        if node == None:
            return False
        while node.next != None:
            if node.data == data:
                return True
            node = node.next  
        if node.data == data:
            return True
        return False
        
    def insertEnd(self, data):
        """
        inserts the element at end
        
        :param data: element to be inserted at end
        :type data: object/element 
        """
        
        if self.head == None:
            self.insert(data)
            return 
        node = self.head
        while node.next != None:
            node = node.next
            
        node.next = Node(data)
    
    def remove(self, data):
        """
        to delete an element from linked list
        
        :param data: the element to deleted
        :type data: object/Element 
        """
        if self.head == None:
            raise DSEmpty("linked list is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        currentNode = self.head
        nextNode = self.head.next
        while nextNode.next != None:
            if nextNode.data == data:
                currentNode.next = nextNode.next
                del nextNode.data
                return
            currentNode = nextNode
            nextNode = nextNode.next
        print nextNode.data
        if nextNode.data == data:
            currentNode.next = None
            del nextNode
            return
        raise DSEmpty("Element not found")
            
    
    def transverse(self):
        """
        method to transverse the linked list
        """
        
        if self.head == None:
            raise DSEmpty("Linked list is empty")
        node = self.head
        while node.next != None:
            print node.data
            node = node.next
        print node.data
    
    def convertToList(self):
        """
        to convert the linked list to list in python
        
        :return: returns all elements of a linked list in list
        :rtype: List 
        """
        if self.head == None:
            raise DSEmpty("Linked list is empty")
        node = self.head
        output = []
        while node.next != None:
            output.append(node.data)
            node = node.next
        output.append(node.data)
        return output 
        
    def isEmpty(self):
        """
        used to check whether
        
        :return: whether linked list is empty or not
        :rtype: bool
        """
        
        return self.head == None
    
    def __len__(self):
        """
        a.__len__() => len(a)
        where  a is a linked list
        
        used to find the length of a linked list
        
        :return: length of the linked list
        :rtype: Int 
        """
        
        length = 0
        if self.head == None:
            return length
        node = self.head
        while node.next != None:
            length += 1
            node = node.next
        length += 1
        return length 
    