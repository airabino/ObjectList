from math import sqrt
from statistics import median

"""
ObjectList is a custom subclass of list which allows for attribute-wise iteration through
a list of objects. The class also modifies __getitem__ and __getslice__ so that
the list is subscriptable for tuples and slices.

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

"""

class ObjectList(list):
	#Class which allows for iteration through a list of custom objects
	def __init__(self,Vals=list()):
		self.Vals=Vals

	#Replaces list __getitem__ returns ObjectLists for tuples and slices and returns objects
	#for single indices
	def __getitem__(self,items):
		if type(items)==slice:
			return ObjectList(self.Vals[items])
		if hasattr(items, '__iter__'):
			return ObjectList(list(self.Vals[item] for item in items))
		else:
			return self.Vals[items]

	#Replaces list __repr__ to show that the variable is of the ObjectList type
	def __repr__(self):
		return str('ObjectList {}'.format(self.Vals))

	#Replaces list __iter__ to iterate using ObjectListIterator
	def __iter__(self):
		return ObjectListIterator(self.Vals)

	#Pulls values from all objects in ObjectList for a specified attribute
	def pull(self,attr):
		vals_list=[None]*len(self.Vals)
		ObjectListIterator=iter(self)
		i=0
		while True:
			try:
				vals_list[i]=getattr(next(ObjectListIterator),attr)
				i+=1
			except StopIteration:
				break
		return vals_list

	def sum(self,attr):
		return sum(self.pull(attr))

	def mean(self,attr):
		return self.sum(attr)/len(self.Vals)

	def std(self,attr):
		mu=self.mean(attr)
		return sqrt(sum([(x-mu)**2 for x in self.pull(attr)])/len(self.pull(attr)))

	def med(self,attr):
		return median(self.pull(attr))

	def sort(self,attr):
		sorted_order=self.argsort(attr)
		return ObjectList(self.Vals).__getitem__(sorted_order)

	def argsort(self,attr):
		sort_by=self.pull(attr)
		return sorted(range(len(sort_by)), key=sort_by.__getitem__)

	def max(self,attr):
		return max(self.pull(attr))

	def min(self,attr):
		return min(self.pull(attr))

	def argmax(self,attr):
		return self.argsort(attr)[-1]

	def argmin(self,attr):
		return self.argsort(attr)[0]

class ObjectListIterator():
	def __init__(self,Expr):
		self.obj=Expr
		self.ind=-1
	def __next__(self):
		if self.ind<len(self.obj)-1:
			self.ind+=1
			return self.obj[self.ind]
		raise StopIteration