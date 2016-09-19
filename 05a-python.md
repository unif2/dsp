# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>Both are lists of objects
>Tuples are immutable (you can't change an existing tuple - you can't modify the elements).  Lists are mutable.
>You can access entries from both using the x[i] notation, where i in the index of the value you want to access.
>tuples will work as keys in dictionaries because tuples are hashable, as opposed to lists.
>Tuples are also faster and can act as constants.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>Both are sequences of objects.  For a list, elements can be repeated, but not so for sets.  A set is more like a collection >of dictionary keys without their accompanying values.  Therefore, since you cannot have repeated keys in a dictionary, you >cannot have repeated elements in a set.  This is just like the sets in mathematics.  One can do operations between two >sets, such as subtraction, union, intersection, just like in mathematics.  One can also check subset relationships using < >and >.
> < and > for lists are only for comparisons between the first elements of the list.  So, [1,5,6] < [0,4,3].

>Sets are faster because, according to a Stack Overflow user, "Sets are implemented using hash tables. Whenever you add an >object to a set, the position within the memory of the set object is determined using the hash of the object to be added. >When testing for membership, all that needs to be done is basically to look if the object is at the position determined by >its hash, so the speed of this operation does not depend on the size of the set. For lists, in contrast, the whole list >needs to be searched, which will become slower as the list grows.

>This is also the reason that sets do not preserve the order of the objects you add.

>Note that sets aren't faster than lists in general -- membership test is faster for sets, and so is removing an element. As >long as you don't need these operations, lists are often faster."

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>The lambda command, like the def command, is used to create a function (more precisely, funciton objects).  In that sense, >they are equivalent, but creating a function using lambda is advantageous when you need to make a short function that is to >be used only once in your code.  If you need to use a function multiple times in your application, then it's better to >section off that code and create a function out of it using def and then just call the function.  However, if you'd like to >use a function only once, calling and using it at only one spot, it may be more convenient (and faster) to create it using >the lambda function, without the need to even name it, thereby making your code look cleaner.  The body of a lambda can >contain only a single expression, making lambdas short.  What can I put into a lambda?  Anything that returns a value (i.e. >an expression), or anything that can be the right hand side of an assignment statement.  It's OK to put a function call in >a lambda.  Print statements (which is a function in Python 3), functions that return None, and even conditional expressions >can be inside a lambda.  "The most common use for lambda is to create anonymous procedures for use in GUI callbacks. In >those use cases, we don’t care about what the lambda returns, we care about what it does."

>Examples:

>square_root = lambda x: math.sqrt(x)
>or
>x=4
>(lambda x: math.sqrt(x))(x) # returns 2

>m = lambda x, y:   x + y   #  def sum(x,y): return x + y
>m(3,4) # returns 7

>frame = tk.Frame(parent)
>frame.pack()
 
>btn22 = tk.Button(frame, 
>        text="22", command=lambda: self.printNum(22))
>btn22.pack(side=tk.LEFT)
> 
>btn44 = tk.Button(frame, 
>        text="44", command=lambda: self.printNum(44))
>btn44.pack(side=tk.LEFT)

>lambda: a if some_condition() else b
>lambda x: ‘big’ if x > 100 else ‘small’

>Reference: https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/

>Example I made up myself:

>class Triangle:
>	def __init__(self,base=0,height=0):
>		self.base = base
>		self.height = height
>		self.area = 0.5*self.base*self.height
>	def __str__(self):
>		return '(%f,%f,%f)' %(self.base,self.height,self.area)
>	def __repr__(self):
>		return repr((self.base,self.height,self.area))
		
>triangles=[Triangle(6,6),Triangle(4,5),Triangle(1,1)]
>t=sorted(triangles,key=lambda triangle: triangle.area)
>print(t)

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>A list comprehension enables you to construct list based on a rule without using a for loop.  For example, the code:
>def capitalize_all(t):
>    return [s.capitalize() for s in t]
    
>takes a list of strings and capitalizes the first letter of each string in the list.  Contrast this with the following code >that uses for loops:

>def capitalize_all(t):
>    res = []
>    for s in t:
>        res.append(s.capitalize())
>    return res
    
>Using a list comprehension can usually make the function faster than using for loops.
 
> Another example:
 
> def only_upper(t):
>    return [s for s in t if s.isupper()]
    
> which takes a string and returns the letters in the string which are upper case.  Contrast with this code which doesn't >use list comprehensions:
 
>def only_upper(t):
>    res = []
>    for s in t:
>        if s.isupper():
>            res.append(s)
>    return res
    
> Now using filter:
 
> def upper(t):
>  return t.isupper()
  
> x='uNIf2'
> list(filter(upper,x)) # returns ['N','I']

>Another example:
># Using a list comprehension
>list = [0,1,2,3,4,5]
>sqr = [x**2 for x in list] # returns [0,1,4,9,16,25]

># Using map instead
>items = [0,1,2,3,4,5]
>def sqr(x):
> return x**2
 
>list(map(sqr, items)) # returns [0,1,4,9,16,25]

>or (using lambda)

>list(map((lambda x: x **2), items))

>Set comprehensions:
>{x**2 for x in range(5)} # returns set {0,1,4,9,16}

>Dictionary comprehensions:
>{x:x**2 for x in range(5)}
>---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>import datetime

>date_start=datetime.datetime.strptime("01/02/2013","%m/%d/%Y")

>date_stop=datetime.datetime.strptime("07/28/2015","%m/%d/%Y")

>delta = date_stop - date_start

>print(delta.days)

>(937)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
>import datetime

>date_start=datetime.datetime.strptime("12312013","%m%d%Y")

>date_stop=datetime.datetime.strptime("05282015","%m%d%Y")

>delta = date_stop - date_start

>print(delta.days)

>(513)


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```
>import string

>import datetime

>date_start = '15-Jan-1994'

>date_stop = '14-Jul-2015'

>s=date_start.split('-')

>t=date_stop.split('-')

>months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

>s[1]=months.index(s[1])+1

>t[1]=months.index(t[1])+1

>for i in range(3):

>  s[i]=int(s[i])

>  t[i]=int(t[i])
  
>start = datetime.datetime(s[2],s[1],s[0])

>stop = datetime.datetime(t[2],t[1],t[0])

>delta = stop - start

>print(delta.days)

>(7850)

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





