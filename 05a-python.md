# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

import datetime
date_start=datetime.datetime.strptime("01/02/2013","%m/%d/%Y")
date_stop=datetime.datetime.strptime("07/28/2015","%m/%d/%Y")
delta = date_stop - date_start
print(delta.days)
(937)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
import datetime
date_start=datetime.datetime.strptime("12312013","%m%d%Y")
date_stop=datetime.datetime.strptime("05282015","%m%d%Y")
delta = date_stop - date_start
print(delta.days)
(513)


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```
import string
import datetime

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

s=date_start.split('-')
t=date_stop.split('-')

months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
s[1]=months.index(s[1])+1
t[1]=months.index(t[1])+1

for i in range(3):
  s[i]=int(s[i])
  t[i]=int(t[i])
  
start = datetime.datetime(s[2],s[1],s[0])
stop = datetime.datetime(t[2],t[1],t[0])

delta = stop - start
print(delta.days)
(7850)

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





