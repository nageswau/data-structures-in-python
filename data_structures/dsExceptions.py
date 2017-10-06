'''
Created on 24-Sep-2017

@author: Nag
'''

class DSException(Exception):
    """
    custom base Exception for all data structures Exceptions
    """
    pass

class DSEmpty(DSException):
        """
        customnException for DS empty 
        """
        
        def __init__(self, msg):
            super(DSEmpty, self).__init__(msg)
            self.msg = msg 
            