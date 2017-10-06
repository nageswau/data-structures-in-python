from data_structures.linked_lists import LinkedList

a = LinkedList()
"""print a.isEmpty()
print len(a)
#print a.transverse()
#print a.convertToList()"""
a.insert("nag")
a.insert(15)
a.insertEnd("25")

a.transverse()
print a.convertToList()
print a.search(15)
print a.search("python")
print len(a)

print a.remove('nag')
print a.convertToList()
