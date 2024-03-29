# Python Cheat Sheet

[Click here for similar Java Resource (not made by me)](https://drive.google.com/file/d/1ao4ZA28zzBttDkuS6MLQI52gDs_CJZEm/view) <br>


## Basics

- Data Types

    ![Untitled](https://user-images.githubusercontent.com/59110866/173563442-1a6fa3d2-b569-4eb0-99cc-9b91cc8be1eb.png)

- Operators and it’s precedence

| Operators                   | Description                                 |
|-----------------------------|---------------------------------------------|
| ()                          | Parentheses                                 |
| **                          | Exponentiation                              |
| +x  -x  ~x                  | Unary plus, unary minus, and bitwise NOT    |
| *  /  //  %                 | Multiplication, division, floor division, and modulus |
| +  -                        | Addition and subtraction                   |
| <<  >>                      | Bitwise left and right shifts               |
| &                           | Bitwise AND                                 |
| ^                           | Bitwise XOR                                 |
| \|                          | Bitwise OR                                  |
| ==  !=  >  >=  <  <=  is  is not  in  not in | Comparisons, identity, and membership operators |
| not                         | Logical NOT                                 |
| and                         | Logical AND                                 |
| or                          | Logical OR                                  |

> Python integer division acts a bit weird with -ve numbers ex: -3//2 will give -2 answer instead of -1 so always use int(-3/2) for integer division in problems
    
## Data Structures

### Lists
- Mutable
- Higher memory consumption
- A lot of built-in methods are available
- Slower iteration
- Better for operations like insertion and deletion

| Operation          | Examples           | Complexity class   |
|--------------------|--------------------|--------------------|
| Append             | l.append(item)     | O(1)               |
| Clear              | l.clear()          | O(1)               |
| Containment        | item in/not in l   | O(N)               |
| Copy               | l.copy()           | O(N)               |
| Delete             | del l[i]           | O(N)               |
| Extend             | l.extend(...)      | O(N)               |
| Equality           | l1==l2, l1!=l2     | O(N)               |
| Index              | l[i]               | O(1)               |
| Iteration          | for item in l:     | O(N)               |
| Length             | len(l)             | O(1)               |
| Multiply           | k*l                | O(k*N)             |
| Min, Max           | min(l), max(l)     | O(N)               |
| Pop from end       | l.pop(-1)          | O(1)               |
| Pop intermediate   | l.pop(item)        | O(N)               |
| Remove             | l.remove(...)      | O(N)               |
| Reverse            | l.reverse()        | O(N)               |
| Slice              | l[x:y]             | O(y-x)             |
| Sort               | l.sort()           | O(N*log(N))        |
| Store              | l[i]=item          | O(1)               |

```python
nums = [1,2,3]

nums.index(1) # returns index
nums.append(1) # appends 1
nums.insert(0, 10) # inserts 10 at 0th index
nums.remove(3) # removes all instances of 3
nums.copy(1) # returns copy of the list
nums.count(1) # returns no.of times '1' is present in the list
nums.extend(someOtherList) # ...
nums.pop() # pops last element [which element to pop can also be given as optional argument]
nums.reverse() # reverses original list (nums in this case)
nums.sort() # sorts list [does NOT return sorted list]
# Python's default sort uses Tim Sort, which is a combination of both merge sort and insertion sort.
```

List slicing
```python
# 包含 start 但不包含 stop
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

# There is also the step value, which can be used with any of the above:
a[start:stop:step] # Start through not past stop, by step

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
# The step value may be negative as well
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```

### Dictionary

Dictionaries are used to store data values in key:value pairs.
Note: Lists cannot be used as key, whereas tuple can be used as key. [Reference](https://blog.hubspot.com/website/variables-python#:~:text=Unlike%20other%20programming%20languages%3B%20Python,assign%20a%20value%20to%20them.)

| Operation         | Examples          | Complexity class  |
|-------------------|-------------------|-------------------|
| Clear             | d.clear()         | O(1)              | O(1)              |
| Construction      | dict(...)         | O(len(d))         | O(len(d))         |
| Delete            | del d[k]          | O(1)              | O(N)              |
| Get               | d.get()           | O(1)              | O(N)              |
| Iteration (key, value, item) | for item in d: | O(N)      | O(N)              |
| Length            | len(d)            | O(1)              | O(1)              |
| Pop               | d.pop(item)       | O(1)              | O(N)              |
| Pop Item          | d.popitem()       | O(1)              | O(1)              |
| Returning Views   | d.values()        | O(1)              | O(1)              |
| Returning keys    | d.keys()          | O(1)              | O(1)              |
| Fromkeys          | d.fromkeys(seq)   | O(len(seq))       | O(len(seq))       |


```python
dict = {'a':1,'b':2,'c':3}
dict = dict()

dict.keys() # returns list of keys of dictionary
dict.values() # returns list of values of dictionary
dict.items() # returns [('a',1),('b',2),('c',3)]

dict.get('a') # returns value for any corresponding key
dict.copy() # returns copy of the dictionary
# NOTE : items() Returns view object that will be updated with any future
# changes to dict
dict.pop(KEY) # pops key-value pair with that key
dict.setDefault(KEY,DEFAULT_VALUE)
# returns value of key, if key exists, else default value returned
# If the key exist, this parameter(DEFAULT_VALUE) has no effect.
# If the key does not exist, DEFAULT_VALUE becomes the key's value. 2nd
# argument's default is None.
dict.update({KEY:VALUE})
```

### Sets

| Operation             | Examples                     | Complexity class               |
|-----------------------|------------------------------|--------------------------------|
| Add                   | s.add(item)                  | O(1)                           | O(N)                           |
| Clear                 | s.clear()                    | O(1)                           | O(1)                           |
| Copy                  | s.copy()                     | O(N)                           | O(N)                           |
| Containment           | item in/not in s             | O(1)                           | O(N)                           |
| Creation              | set(...)                     | O(len(s))                      | O(len(s))                      |
| Discard               | s.discard(item)              | O(1)                           | O(N)                           |
| Difference            | s1-s2                        | O(len(s1))                     | O(len(s1))                     |
| Difference Update     | s1.difference_update(s2)     | O(len(s2))                     | –                              |
| Equality              | s1==s2, s1!=s2               | O(min(len(s1), len(s2)))       | O(min(len(s1), len(s2)))       |
| Intersection          | s1 & s2                      | O(min(len(s1), len(s2)))       | O(min(len(s1), len(s2)))       |
| Iteration             | for item in s:               | O(N)                           | O(N)                           |
| Is Subset             | s1<=s2                       | O(len(s1))                     | O(len(s1))                     |
| Is Superset           | s1>=s2                       | O(len(s2))                     | O(len(s1))                     |
| Pop                   | s.pop()                      | O(1)                           | O(N)                           |
| Union                 | s1|s2                        | O(len(s1)+len(s2))             | –                              |
| Symmetric Difference  | s1^s2                        | len(s1)                        | O(len(s1)*len(s2))             |


A set is a collection which is unordered, immutable, unindexed, No Duplicates.

```python
set = set()
set = {1,2,3}

set.add(item)
set.remove(item)
set.discard(item) 
# Remove will throw error if item is not there, discard will not
```

### Tuples

A [tuple](https://www.scaler.com/topics/python/tuples-in-python/) is a collection which is ordered, **unchangeable** and can contain duplicate values
Time complexity is similar to list

- Immutable
- Lower memory consumption
- A small number of built-in methods available
- Faster iteration
- Better for accessing elements    

```python
tuple = (1, 2, 3, 1)

tuple.count(1) # returns occurence of an item
tuple.index(1) # returns index of 1 in array
```

### Strings

```python
# ** split Function **
# The split() method breaks up a string at the specified separator and returns
# a list of strings.
text = 'Python is a fun programming language'

# split the text from space
print(text.split(' '))
# Output: ['Python', 'is', 'a', 'fun', 'programming', 'language']

# convert string to list
s="abcd"
s=list(s)
print(s)
# Output: ['a', 'b', 'c', 'd']

# ** count Function **
# The count() method returns the number of occurrences of a substring in the given string.
# Example
message = 'python is popular programming language'
# number of occurrence of 'p'
print('Number of occurrence of p:', message.count('p')) # Output: Number of occurrence of p: 4

# The isnumeric() method returns True if all characters in a string are numeric characters. If not, it returns False.
s = '1242323'
print(s.isnumeric()) #Output: True

# The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
# check the index of 'fun'
print(message.find('fun')) # Output: 12

# The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

name = "M3onica Gell22er "
print(name.isalnum()) # Output : False

# The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False
name = "Monica"
print(name.isalpha()) #output true

# other important functions
string.strip([chars]) #The strip() method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).
string.upper() # The upper() method converts all lowercase characters in a string into uppercase characters and returns it.
string.lower() # The lower() method converts all uppercase characters in a string into lowercase characters and returns it.
string.islower() # The islower() method returns True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise.
string.isdigit() 
string.isupper() # The isupper() method returns True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise.
```

### Counter

Python Counter is a container that will hold the count of each of the elements present in the container. The counter is a sub-class available inside the dictionary class. Specifically used for element frequencies.

```python
from collections import Counter #(capital 'C')
# can also be used as 'collections.Counter()' in code

list1 = ['x','y','z','x','x','x','y', 'z']

# Initialization
Counter(list1) # => Counter({'x': 4, 'y': 2, 'z': 2})
Counter("Welcome to Guru99 Tutorials!") # => Counter({'o': 3, ' ': 3, 'u': 3, 'e': 2.....})

# Updating
counterObject = collections.Counter(list1)
most_common_element = counterObject.most_common(1) # [('x', 4)]
counterObject.update("some string") # => Counter({'o': 3, 'u': 3, 'e': 2, 's': 2})
counterObject['s'] += 1 # Increase/Decrease frequency

# Accessing
frequency_of_s = counterObject['s']
counterObject.keys() # [ 'x' , 'y' , 'z' ]
counterObject.items()
counterObject.values()

# Deleting
del couterObject['s']
```

### Deque
A double-ended queue, or deque, has the feature of adding and removing elements from either end.

```python
#in BFS(Breadth-first search) or other algorithms where we have to pop or add elements to the begining , deque is the best option 
#we can also use list, but list.pop(0) is O(n) operation where as dequeu.popleft() is O(1)

from collections import deque

queue = deque(['name','age','DOB'])

queue.append("append_from_right") # Append from right
queue.pop() # Pop from right

queue.appendleft("fromLeft") # Append from left
queue.popleft() # Pop from left

queue.index(element, begin_index, end_index) # Returns first index of element b/w the 2 indices.
queue.insert(index, element)
queue.remove() # removes first occurrance
queue.count()
queue.reverse() # reverses order of queue elements
```

### Heapq

As we know the Heap Data Structure is used to implement the Priority Queue ADT. In python we can directly access a Priority Queue implemented using a Heap by using the **Heapq** library/module.
The acceptable item in the lists are numerical var, string, tuple

```python
import heapq # (minHeap by Default)

nums = [5, 7, 9, 1, 3]

heapq.heapify(nums) # converts list into heap. Can be converted back to list by list(nums).
heapq.heappush(nums, element) # Push an element into the heap
heapq.heappop(nums) # Pop an element from the heap

# Used to return the k largest elements from the iterable specified 
# The key is a function with that accepts single element from iterable,
# and the returned value from that function is then used to rank that element in the heap
heapq.nlargest(k, iterable, key = fun)
heapq.nsmallest(k, iterable, key = fun)

# By default heapq in python is min heap
# If we want to use max heap we can simply invert the value
```
#### Customize cmp in heap
override __lt__ for the class
```python
# wrap dictionary to a class

class employee: 
    def __init__(self, n, d, yos, s): 
        self.name = n 
        self.des = d 
        self.yos = yos 
        self.sal = s 
    def print_me(self): 
        print("Name :", self.name) 
        print("Designation :", self.des) 
        print("Years of service :", str(self.yos)) 
        print("salary :", str(self.sal)) 
  
   # override the comparison operator 
    def __lt__(self, nxt): 
        return self.yos < nxt.yos 
  
e1 = employee('Anish', 'manager', 3, 24000) 
e2 = employee('kathy', 'programmer', 2, 15000) 
e3 = employee('Rina', 'Analyst', 5, 30000) 
e4 = employee('Vinay', 'programmer', 1, 10000) 
```

## OOP

### Class
```python
class automobile:
    # this is how initialize works
    # self pointer represent the class itself
	def __init__(self, size, speed):
		self.size = size
		self.speed = speed
```

### Inheritance
The super() function is a built-in function that returns the objects that represent the parent class.
```python
# parent class
class Bird:

	def __init__(self):
		print("Bird is ready")
	
	def whoisThis(self):
		print("Bird")
	
	def swim(self):
		print("Swim faster")

# child class
class Penguin(Bird):
	def __init__(self):
		# call super() init function
		super().__init__()
		# Note: super().__init__() will work for one inheritance
		# However, for multiple inheritance, we use Bird.__init__(self)
		print("Penguin is ready")

	def whoisThis(self): # 方法重写
		print("Penguin")
	
	def run(self):
		print("Run faster")
	
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
```

### Encapsulate
To define a private member prefix the member name with double underscore “__”. (can only be access by iteself)<br>
To define a protect member prefix the member name with single underscore “_”. (can only be access by itself and children class)<br>
**Note: Python’s private and protected members can be accessed outside the class through python name mangling.**<br>
Name mangling: python process any identifier with two leading underscore and one trailing underscore is textually replaced with _classname__identifier where classname is the name of the current class.

```python
class Student: 
	def __init__(self, name): 
		self.__name = name 

	def displayName(self): 
		print(self.__name) 

s1 = Student("Santhosh") 
s1.displayName() 

# Raises an error 
print(s1.__name) 

```

### Polymorphism
```python
# A simple Python function to demonstrate 
# Polymorphism

def add(x, y, z = 0): 
	return x + y+z

# Driver code 
print(add(2, 3))
print(add(2, 3, 4))
```
Polymorphism with Inheritance:
```python
class Bird:
def intro(self):
	print("There are many types of birds.")
	
def flight(self):
	print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
def flight(self):
	print("Sparrows can fly.")	
```
Polymorphism with a Function and objects: To create a function that can take any object, allowing for polymorphism.
```python
def func(obj):
	obj.capital()
	obj.language()
	obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)

```
## Built-in or Library functions

### *args **kargs
*args: non-keyworded, variable-length argument list passed by the function call.
```python
def myFun(*argv):
	for arg in argv:
		print(arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
```
**kargs: keyworded variable-length argument passed by the function call.
```python
def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))
myFun(first='Geeks', mid='for', last='Geeks')
```
### with
with statement is used in exception handling to make the code cleaner and much more readable
```python
# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')
```

### Generator
A generator function in Python is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.
**Yield** suspends a function’s execution and sends a value back to the caller, but retains enough state to enable the function to resume where it left off. 
```python
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value)
```

### Closure
Closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.
```python
def count():                # 建立一個 count 函式
    a = []                    # 函式內有區域變數 a 是串列
    def avg(val):             # 建立內置函式 avg ( 閉包 )
        a.append(val)           # 將參數數值加入變數 a
        print(a)                # 印出 a
        return sum(a)/len(a)    # 回傳 a 串列所有數值的平均
    return avg                # 回傳 avg

test = count()
test(10)      # 將 10 存入 a
test(11)      # 將 11 存入 a
test(12)      # 印出 11

'''
[10]
[10, 11]
[10, 11, 12]
'''
```
不過如果將上方的例子，改成變數的做法，可能就會發生錯誤，因為在 cal 函式裡的變數 a 後方使用了「等號」，意義等同於變數的「賦值」，換句話說是新建了一個區域變數 a，就造成了名稱空間裡名稱重疊的問題。
如果必須這麼做，可以使用 nonlocal 的方式，宣告這個變數是「自由變數」( 不是這個區域裡的變數 )，就能正常使用這個變數。
```python
def count():
    a = 1
    def cal(val):
        nonlocal a
        a = a + val
        return a
    return cal

test = count()
test(10)
test(11)
test(12)    # 34 ( 1 + 10 + 11 + 12 )
```

### Decorator
有一天老闆突然讓你統計每個程式都運行了多長時間並比較下運行效率，此時如果你去手動修改每個程序的代碼一定會讓你抓狂。[Reference](https://blog.csdn.net/weixin_42134789/article/details/84635252)

```python
def time_it(func): # outer function
    def inner(): # inner function
        start = time.time()
        func()
        end = time.time()
        print('need :{} sec'.format(end-start))
    return inner

@time_it
def func1():
    time.sleep(2)
    print("Func1 is running.")
```

General decorator
```python
def hint(func):
    def wrapper(*args, **kwargs):
        print('{} is running'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@hint
def hello():
    print("Hello!")


>>> hello()
hello is running.
Hello!
```
Advanced Decorator
```python
def hint(coder):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print('{} is running'.format(func.__name__))
            print('Coder: {}'.format(coder))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@hint(coder="John")
def hello():
    print("Hello!")
```

### map
map function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
    
```python
def a(x):
    return x+1

b = map(a, [1,2,3,4,5])
c = map(lambda x: x+1, [1,2,3,4,5])

print(list(b))    # [2, 3, 4, 5, 6]
print(tuple(c))   # (2, 3, 4, 5, 6)
```
### zip
```python
** zip(list,list) **
for elem1, elem2 in zip(firstList, secondList):
    # will merge both lists and produce tuples with both elements
    # Tuples will stop at shortest list (in case of both lists having different len)
# Example
'''
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(tuple(x))

o/p: (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
'''
```
### enumerate
```python
** enumerate(list|tuple) ** 
# [when you need to attach indexes to lists or tuples ]
enumerate(anyList) # ['a','b','c'] => [(0, 'a'), (1, 'b'), (2, 'c')]
```

### filter
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
```python
def a(x):
  return x>2
b = filter(a, [1,2,3,4,5])
c = filter(lambda x: x>2, [1,2,3,4,5])

print(list(b))    # [3, 4, 5]
print(tuple(c))   # (3, 4, 5)
```

### bisect
```python
** bisect.bisect(list,number, begin, end) ** O(log(n))
# [ returns the index where the element should be inserted 
#		such that sorting order is maintained ]
a = [1,2,4]
bisect.bisect(a,3,0,4) # [1,2,4] => 3 coz '3' should be inserted in 3rd index to maintain sorting order

# Suppose the element we want to insert is already present
# in the sorting list, the bisect_left() will return index left of the existing number
# bisect_right() or bisect() will return index right to the existing number

bisect.insort(list,number,begin,end)       # O(n) to insert
bisect.insort_right(list,number,begin,end)
bisect.insort_left(list,number,begin,end)

'''
The above 3 functions are exact same of bisect.bisect(), the only difference
is that they return the sorted list after inserting and not the index. The
left() right() logic is also same as above.
'''
```
### ord & chr 
Getting ASCII value of a character
```python
** ord(str) **
# returns ascii value of the character , Example ord("a") = 97
** chr(int) ** 
# return character of given ascii value , Example chr(97) = "a"
```
    

### Math
Important Python Math Functions
    
```python
# Syntax : math.log(a, Base)
import math
    
# Printing the log base e of 14
print ("Natural logarithm of 14 is : ", end="")
print (math.log(14))
    
# Printing the log base 5 of 14
print ("Logarithm base 5 of 14 is : ", end="")
print (math.log(14,5))

# Python code to demonstrate the working of
# ceil() and floor()
#   
a = 2.3
    
# returning the ceil of 2.3 (i.e 3)
print ("The ceil of 2.3 is : ", end="")
print (math.ceil(a))
    
# returning the floor of 2.3 (i.e 2)
print ("The floor of 2.3 is : ", end="")
print (math.floor(a))

# Constants
# Print the value of Euler e (2.718281828459045)
print (math.e)
# Print the value of pi (3.141592653589793)
print (math.pi)
print (math.gcd(b, a))
print (pow(3,4))
# print the square root of 4
print(math.sqrt(4))
a = math.pi/6
b = 30
    
# returning the converted value from radians to degrees
print ("The converted value from radians to degrees is : ", end="")
print (math.degrees(a))
    
# returning the converted value from degrees to radians
print ("The converted value from degrees to radians is : ", end="")
print (math.radians(b))

** bin(int) **
bin(anyNumber) # Returns binary version of number

** divmod(int,int) **
divmod(dividend,divisor) # returns tuple like (quotient, remainder)
```
### Custom cmp 
Python cmp_to_key function to sort list with custom compare function
return a negative value (`< 0`) when the left item should be sorted *before* the right item
return a positive value (`> 0`) when the left item should be sorted *after* the right item
return `0` when both the left and the right item have the same weight and should be ordered "equally" without precedence

```python
from functools import cmp_to_key
sorted(mylist, key=cmp_to_key(compare))

def compare(item1, item2):
    if fitness(item1) < fitness(item2):
        return -1
    elif fitness(item1) > fitness(item2):
        return 1
    else:
        return 0
```


## Reference
[steam python education](https://steam.oxxostudio.tw/category/python/library/re.html)
