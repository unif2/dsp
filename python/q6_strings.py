# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
    if not isinstance(count, int) or count < 0:
        print('Number of donuts must be a positive integer!')
        raise NotImplementedError
        
    elif 0 <= count < 10:
        return 'Number of donuts: %d' % count
    
    else:
        return 'Number of donuts: many'



def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    """
    if not isinstance(s, str):
        raise NotImplementedError
    elif len(s) < 2:
        return ''
    else:
        return s[0]+s[1]+s[-2]+s[-1]


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    if not isinstance(s, str) or len(s) < 1:
        raise NotImplementedError
    if any(l == s[0] for l in s[1:]):
        return s[0]+s[1:].replace(s[0],'*')
    return s    
    

# OR

def fix_start(s):
    from collections import Counter
    count = Counter(s)
    if not isinstance(s, str) or len(s) < 1:
        raise NotImplementedError
    if count[s[0]]>1:
        return s[0]+s[1:].replace(s[0],'*')
    return s

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    if not isinstance(a,str) or not isinstance(b,str) or len(a)<2 or len(b)<2:
        raise NotImplementedError
    return b[0]+a[1:]+' '+a[0]+b[1:]


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if not isinstance(s,str):
        raise NotImplementedError
    if len(s) < 3:
        return s
    if s[len(s)-3:]=='ing':
        return s+'ly'
    return s+'ing'



def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    if not isinstance(s,str):
		raise NotImplementedError
	t = s.split()
	if 'not' in t and 'bad' in t and t.index('bad') > t.index('not'):
		a = t.index('not')
        b = t.index('bad')
		t[a]='good'
        del(t[a+1:b+1])
		delimiter = ' '
		z = delimiter.join(t)
		return z
	else:
		return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
