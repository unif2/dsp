# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
	if any(type(x)==int for x in words):
		raise NotImplementedError
	sum = 0
	for word in t:
		if len(word) >= 2 and word[0]==word[-1]:
			sum += 1
	return sum


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
	if any(type(x)==int for x in words):
		raise NotImplementedError
	
	xlist = [word for word in words if word[0]=='x']
	notxlist = [word for word in words if word[0]!='x']
	xlist.sort()
	notxlist.sort()
	merge = xlist + notxlist
	return merge


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
	if any(type(x)==tuple for x in tuples):
		raise NotImplementedError	
	y=sorted(tuples,key=lambda x: x[1])
	return y
    


def remove_adjacent(nums):
# This, surprisingly, took me many hours of convoluted and long (but failed) methods until I arrived at this one!
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
	if any(type(x)!=int for x in nums):
		raise NotImplementedError
	i=0
	while i != len(nums)-1:
		if nums[i]==nums[i+1]:
			del(nums[i])
		else:
			i = i+1
	return nums



def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
	if any(type(x)!=str for x in list1) or any(type(x)!=str for x in list2):
		raise NotImplementedError
	merged = []
	while list1 and list2: # while both lists are nonempty
		if list1[-1] > list2[-1]:
			merged.append(list1.pop())
		else:
			merged.append(list2.pop())
	# At this point, one of the lists is empty, and the other
	# has been diminished, but still sorted in ascending order
	# So now we add that set (but reversed) to our merged list
	merged += sorted(list1 + list2, reverse = True)
	merged.reverse()
	return merged
	
	# Alternate solution suggested by Gina Soileau:
	
	lst = list1 + list2
	lst.sort()
	return lst
	
	
