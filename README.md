# ObjectList
Python list subclass that allows for attribute-wise operations with lists of objects

Requires: Python 3.4+ (needs median function from builtin statistics module)

Installation: python setup.py install

ObjectList is a custom subclass of list which allows for attribute-wise iteration through
a list of objects. The class also modifies __getitem__ so that
the list is subscriptable for tuples which allows for the sort functionality to work.

The main purpose of this class is to make it easy to deal with a list of objects
in a attribute-wise manner. This module uses only builtin Python 3 modules and
ObjectList operations are not particularly fast compared to NumPy ndarrrays but
do provide additional flexibility compared to ndarrays with object dypes

Functionalities of ObjectLists are (in addition to list functionalities):
1. ObjectLists are subscriptable by tuples
2. Pull values for an atttribute form all objects in ObjectList
3. Sort ObjectList by values of specified attribute
4. Get argsort list of indices for ObjectList by values of specified attribute
5. Get mean, standard deviation, median, max, and min for ObjectList by values of specified attribute
6. Get argmin adn argmax for ObjectList by values of specified attribute

These functionalities are demonstrated in the example code below:

#Loading the ObjectList class
from ObjectList import ObjectList

#Creating a generic class
class foo():
    def __init__(self,bar,inv_bar):
        self.bar=bar
        self.inv_bar=inv_bar

#Populating a list with objects of the class defined above
foo_list=[None]*10
for i in range(10):
    foo_list[i]=foo(i+1,1/(i+1))

#Creating an ObjectList from list of objects
foo_ObjectList=ObjectList(foo_list)

#ObjectList prints like list
print(foo_ObjectList)

#Get a single index from the ObjectList - returns that object
print(foo_ObjectList[1])

#Get a tuple of indices from the ObjectList - returns an ObjectList
print(foo_ObjectList[1,3,4])

#Get a slice from the ObjectList - returns an ObjectList
print(foo_ObjectList[1:4])

#Pull values for a specified attribute from all objects in the ObjectList - returns a list
print(foo_ObjectList.pull('bar'))
print(foo_ObjectList.pull('inv_bar'))

#Sort the ObjectList by a specified attribute - returns an ObjectList
sorted_foo_ObjectList=foo_ObjectList.sort('inv_bar')
print(sorted_foo_ObjectList.sort('inv_bar').pull('bar'))
print(sorted_foo_ObjectList.sort('inv_bar').pull('inv_bar'))

#argsort for the ObjectList by a specified attribute - returns a list
print(foo_ObjectList.argsort('inv_bar'))

#Get the mean, standard deviation, median, max, and min for a specified attribute - return values
print(foo_ObjectList.mean('bar'))
print(foo_ObjectList.std('bar'))
print(foo_ObjectList.med('bar'))
print(foo_ObjectList.max('bar'))
print(foo_ObjectList.min('bar'))

#Get argmax and argmin for a specified attribute - return int indices
print(foo_ObjectList.argmax('bar'))
print(foo_ObjectList.argmin('bar'))
