# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Tuples and lists are similar in the sense that both are sequences of values of any type indexed by integers.

However, the big difference between tuples and lists is that tuples are immutable whereas lists are mutable. Therefore, only tuples are hashable which is a prerequisite for keys in dictionaries. Hence, tuples will work as keys in dictionaries, lists won't.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets are similar in the sense that they both store values of any kind.

Main differences:

(1) Sets are not ordered while lists are
(2) Sets can't have the same element twice, lists can
(3) Lists are mutable, sets are immutable

Example of using both:
(1) Lists: You would use lists whenever you care about order but not about duplicates. E.g. you could do a list containing a sequence of cities visited in a certain order.
(2) Sets: Sets are used when order does not matter, but you wouldn't want any duplicates. E.g. you could store all the different places you visited in your life in a set that only contains every place once.

Finding an element is faster in sets than in lists.That is because the set uses a hash function to map to a bucket. Since Python implementations automatically resize that hash table, the speed can be constant no matter the size of the set.

In contrast, to evaluate whether an object is a member of a list, Python has to compare every single member for equality, i.e. the test is O(n).

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.


Lambda is a tool to create functions. I.e. we can either use def or lambda to define a function in python. The difference is that lambda defines "anonymous" functions that cannot be called later on. Hence, lambda is used when using a function only once in a program. This makes particular sense when using command parameters that need function arguments (which lambda creates). One example is when sorting elemnts in a list in a certain order: e.g.:

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10)
]
 sorted(student_tuples, key=lambda student: student[2])   # this sorts the student tuples by their age.


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a concept to construct lists in an easy way similar to defining sets in mathematics.

Example 1:

Scomp = [x**2 for x in range (5)]

Equivalent with 'map':

Smap = map(lambda x: x**2 , range(5))

Example 2:

Scomp2 =  [x for x in range (5) if x%2==0]

Equivalent with 'filter'

Sfilt = filter(lambda x: x%2==0, range(5))

Comparison of capabilities:

'map' maps the (lambda) function to each element of the list sequence and returns the list with each element changed with the function. Filter on the other hand only returns those values that are True based on the (lambda) function handed to the filter function as an argument.

Set comprehension example:

s = { x for x in range(10) }

Dictionary comprehension example:

keys = ['a','b','c']
values = [1,2,3]

Dictcomp = {k:v for (k,v)in zip(keys, values)}


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  


date_start = '01-02-2013'    
date_stop = '07-28-2015'

Answer: 937 days, for code see q5_datetime.py 

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days, for code see q5_datetime.py

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

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





