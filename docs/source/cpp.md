# C/C++

## Basics

### C vs C++

- new and delete
- reference
- auto
- virtual funciton
- template
- STL

### C/C++ Memory

**Stack**

- The stack is managed by the compiler
- It automatically allocates and deallocates memory for local variables and function parameters.
- It typically stores local variables, function arguments, and return addresses.
- The stack provides continuous memory space.
- It has limited space.

**Heap**

- Heap is managed by the programmer.
- Memory allocation and deallocation are manual (using **`new`**, **`malloc`**, **`delete`**, or **`free`**).
- It provides non-contiguous memory space.
- It offers more flexibility but requires responsible memory management.

**Global/static storage area**

- divided into two adjacent areas, initialized and uninitialized, to store initialized and uninitialized global variables and static variables.

**Constant storage area**

- stores constants, generally not allowed to modify.

### Pointer vs Reference
**Pointers**
- Definition: A pointer is a variable that holds the memory address of another variable
- A pointer needs to be dereferenced with the * operator to access the memory location it points to. 
- A pointer can be re-assigned.
- A pointer has its own memory address and size on the stack.
- A pointer can have multiple level of indirection.

**References**
- Definition: A reference variable is an alias, that is, another name for an already existing variable.
- A reference, like a pointer, is also implemented by storing the address of an object. 
- A reference cannot be re-assigned, and must be assigned at initialization. (need to initialize in a single line)
- A reference shares the same memory address with the original variable and takes up no space on the stack.
- A reference can only offer one level of indirection. 
```cpp
int i = 3
// A pointer to variable i or "stores the address of i"
int *ptr = &i; 
// A reference (or alias) for i.
int &ref = i; 
```
### Static
1. Static Variables in functions (local static)
    - When a variable is declared as static, space for it gets allocated for the lifetime of the program.
    - Even if the function is called multiple times, space for the static variable is allocated only once and the value of the variable in the previous call gets carried through the next function call.
    - The scope is still in the function
```cpp
void demo()
{
	static int count = 0;
	cout << count << " ";
	count++;
}

int main()
{
	for (int i = 0; i < 5; i++)
		demo();
	return 0;
}

// The output is 0, 1, 2, 3, 4
```
2. Static variables in a class (local static)
    - The static variables in a class are shared by the objects.
    - There can not be multiple copies of the same static variables for different objects.
    - Thus static variables can not be initialized using constructors
    - Can access without using an object of class
```cpp
// C++ program to demonstrate static
// variables inside a class

#include <iostream>
using namespace std;

class GfG {
public:
	static int i;
	GfG(){};
};
int GfG::i = 1;
int main()
{
	GfG obj1;
	GfG obj2;
	obj1.i = 2;
	obj2.i = 3;
	cout << obj1.i << " " << obj2.i;
}
// Output is 1
```
3. Static global variable (global static)
    - For a global variable, it can be accessed both in this file and in other source files in the same project (add extern for declaration). 
    - Modify global variables changes their scope from visible throughout the entire project to visible only within this file.
4. Class objects as static
    - Like variables, objects also when declared as static have a scope till the lifetime of the program.
```cpp
#include <iostream>
using namespace std;
 
class GfG {
    int i = 0;
 
public:
    GfG()
    {
        i = 0;
        cout << "Inside Constructor\n";
    }
 
    ~GfG() { cout << "Inside Destructor\n"; }
};
 
int main()
{
    int x = 0;
    if (x == 0) {
        static GfG obj;
    }
    cout << "End of main\n";
}
/* the destructor is invoke after end of main
Inside Constructor
End of main
Inside Destructor
*/
```
5. Static functions in a class
    - Static member functions also do not depend on the object of the class.
    - Static member functions are allowed to access only the static data members or other static member functions, they can not access the non-static data members or member functions of the class.
    - Can access without using an object of class
```cpp
class GfG {
public:
    // static member function
    static void printMsg() { cout << "Welcome to GfG!"; }
};
int main{
    // static data members and functions belong to the class and
    // can be accessed without using an object of class X
    GFG::printMsg();
}
```

### Constant
The constants in C are the read-only variables whose values cannot be modified once they are declared in the C program.
```cpp
// Syntax to Define Constant
// These will not work
// const int var;
// var = 5;
const data_type var_name = value;
```
### Smart Pointer (C++)
Some Issues with normal pointers are as follows:

- *Memory Leaks*: This occurs when memory is repeatedly allocated by a program but never freed. This leads to excessive memory consumption and eventually leads to a system crash. 
- *Dangling Pointers*: A dangling pointer is a pointer that points to a memory location that has been deleted.
- *Wild Pointers*: Wild pointers are pointers that are declared and allocated memory but the pointer is never initialized to point to any valid object or address.
- *Data Inconsistency*: Data inconsistency occurs when some data is stored in memory but is not updated in a consistent manner.
- *Buffer Overflow*: When a pointer is used to write data to a memory address that is outside of the allocated memory block. This leads to the corruption of data which can be exploited by malicious attackers.

```cpp
class Rectangle {
private:
	int length;
	int breadth;
};

void fun(){Rectangle* p = new Rectangle();}

int main()
{
	while (1) fun();
}
// The program wil cause memory leak
```
Smart Pointer is a wrapper class over a pointer with an operator like * and -> overloaded. The objects of the smart pointer class look like normal pointers. But, unlike Normal Pointers, it can deallocate and free destroyed object memory.

```cpp
class SmartPtr {
    int* ptr; // Actual pointer
public:
    // Constructor: Refer
    // https://www.geeksforgeeks.org/g-fact-93/ for use of explicit keyword
    explicit SmartPtr(int* p = NULL) { ptr = p; }

    // Destructor
    ~SmartPtr() { delete (ptr); }

    // Overloading dereferencing operator
    int& operator*() { return *ptr; }
    // Overloading arrow operator so that
    // members of T can be accessed
    // like a pointer (useful if T represents
    // a class or struct or union type)
    // T* operator->() { return ptr; }
};

int main()
{
    SmartPtr ptr(new int());
    *ptr = 20;
    cout << *ptr;
    // We don't need to call delete ptr: when the object
    // ptr goes out of scope, the destructor for it is
    // automatically called and destructor does delete ptr.
    return 0;
}
```

### Struct vs Class

總的來說，struct 更適合看成是一個數據結構的實現體，class 更適合看成是一個對象的實現體。

- 最本質的一個區別就是預設的訪問控制
    1. 默認的繼承訪問許可權。 struct 是 public 的，class 是 private 的。
    2. struct 作為數據結構的實現體，它預設的數據訪問控制是 public 的，而 class 作為對象的實現體，它預設的成員變數訪問控制是 private 的。

### Union
Similar to structure.
Member variables in a union share the same memory location, unlike a structure that allocates memory separately for each member variable.
When the available memory is limited, it can be used to achieve memory efficiency.

```cpp
union Union_Name {
    // Declaration of data members
}; union_variables;
```

### Extern

Extern is used before the declaration of a variable or a function, to indicate that “this variable/function is defined elsewhere, and is referenced here.

### Volatile

- Volatile is used to designate a data object as being mapped to memory that can be accessed by independent input/output processes and independent, asynchronously interrupting processes.
- Non-optimizability: volatile tells the compiler not to perform various aggressive optimizations on this variable, or even eliminate the variable directly, ensuring that the instructions written by the programmer in the code will be executed.
- Sequentiality: It can ensure the sequentiality between volatile variables, and the compiler will not perform out-of-order optimization.
- volatile 關鍵字聲明的變數，每次訪問時都必須從記憶體中取出值（沒有被 volatile 修飾的變數，可能由於編譯器的優化，從 CPU 寄存器中取值）
- const 可以是 volatile （如只讀的狀態寄存器）
- pointer can be volatile
```c
volatile bool stop = false;
```

### Define vs Constant vs Inline function

**Define (Marco)**
- Define is actually processed at the pre-compilation stage, without type or type checking.
- Simply does string expansion when encountering the specific words
- it is easy to produce boundary effects and fail to achieve the expected results
- runtime system does not allocate memory for define
- **A macro** is a piece of code that gets **replaced by its value** during compilation.
    
    ```c
    #include <stdio.h>
    #define AREA(l, b) (l * b)
    
    int main() {
        int length = 10, breadth = 5;
        int area = AREA(length, breadth);
        printf("Area of rectangle is: %d", area);
        return 0;
    }
    ```
**Constant**
- const is processed at compile time, with type and type checking
- runtime system allocates memory for const constants
- retaining only one copy of data, saving unnecessary memory space

**Inline function**
- An inline function is one for which the compiler copies the code from the function definition directly into the code of the calling function rather than creating a separate set of instructions in memory.
- Using the inline specifier is only a suggestion to the compiler that an inline expansion can be performed; the compiler is free to ignore the suggestion.
- Normally, when a function is called, the CPU performs several steps, including storing the memory address of the instruction following the function call, copying arguments onto the stack, and transferring control to the specified function.
- For small, commonly used functions, the overhead of making the function call can be more significant than the actual execution time of the function.
- Inline functions eliminate this overhead.
- Similar to define, but with type checking, truly possessing function characteristics.

### Intrinsic

- An intrinsic function is a function which the compiler implements directly when possible, rather than linking to a library-provided implementation of the function.
- A common example is `strncpy()`
- For short strings, making a function call to `strncpy()`, which involves setting up a 'stack frame' with a return address, will consume more time than the actual copying of bytes does. Worse, the effect on CPU pre-fetch buffers will stall the CPU execution for several clock cycles.
- Instead, the intrinsic function is implemented by the compiler in lieu of a function call. In the example of `strncpy()`, the byte-copying code is emitted directly at the place where `strncpy()` is invoked.
- As compared to inline functions, the intrinsic function is provided by the compiler. There isn't a place in the source code of a C program where the intrinsic function is written, nor is there a library implementation that must be linked to. An inline function is different in that the compiler reads the source code for the inline function, but is similar in that later it may emit a compiled translation of the inline function directly into the object code, omitting the overhead of a function call.

### new/delete vs malloc/free

**How is it different from memory allocated to normal variables?**

For normal variables like “int a”, “char str[10]”, etc, memory is automatically allocated and deallocated. For dynamically allocated memory like “int *p = new int[10]”, it is the programmer’s responsibility to deallocate memory when no longer needed. If the programmer doesn’t deallocate memory, it causes a **[memory leak](https://www.geeksforgeeks.org/what-is-memory-leak-how-can-we-avoid/)** (memory is not deallocated until the program terminates).

**“new”** does call the constructor of a class whereas **“malloc()”** does not.

**“free”** frees memory but doesn’t call **[Destructor of a class](https://www.geeksforgeeks.org/destructors-c/)** whereas **“delete”** frees the memory and also calls the Destructor of the class.

#### malloc
Reserves a block of storage of size bytes.
Returns a pointer to the first byte of allocated memory.
```cpp
pointer_name = (cast-type*) malloc(size);
int* ptr = (int*) malloc(sizeof(int));
```

#### aligned_aloc
The aligned_alloc function allocates space for an object whose alignment is specified by alignment, whose size is specified by size, and whose value is indeterminate.
```cpp
void *aligned_alloc( size_t alignment, size_t size );
```

### memcpy vs memmove
memmove() and memcpy() are used to copy a block of memory from a location to another
- memcpy() simply copies data one by one from one location to another. 
- memcpy() leads to problems when strings overlap
- memmove() copies the data first to an intermediate buffer, then from the buffer to destination.

```cpp
// Sample program to show that memmove() is better than 
// memcpy() when addresses overlap. 
char str[100] = "Learningisfun"; 
char *first, *second; 
first = str; 
second = str; 
printf("Original string :%s\n ", str); 

// When overlap happens then it just ignore it
// Since the input addresses are overlapping, memcpy program overwrites the original string and causes data loss. 
/* Copies contents of str2 to str1 */
// memmove(str1, str2, sizeof(str2));  
memcpy(first + 8, first, 10); 
printf("memcpy overlap : %s\n ", str); 

// When overlap it start from first position 
// With memmove function whenever overlap happens the first pointer will start to print from the beginning
memmove(second + 8, first, 10); 
printf("memmove overlap : %s\n ", str);

/* OUTPUT
Original string :Learningisfun
memcpy overlap : LearningLearningis
memmove overlap : LearningLearningLe
*/
```

### Variable Length Argument in C

Variable length argument is a feature that allows a function to receive any number of arguments. There are situations where we want a function to handle variable number of arguments according to requirement. 1) Sum of given numbers. 2) Minimum of given numbers.

```c
// C program to demonstrate use of variable
// number of arguments.
#include <stdarg.h>
#include <stdio.h>

// this function returns minimum of integer
// numbers passed. First argument is count
// of numbers.
int min(int arg_count, ...)
{
	int i;
	int min, a;

	// va_list is a type to hold information about
	// variable arguments
	va_list ap;

	// va_start must be called before accessing
	// variable argument list
	va_start(ap, arg_count);

	// Now arguments can be accessed one by one
	// using va_arg macro. Initialize min as first
	// argument in list
	min = va_arg(ap, int);

	// traverse rest of the arguments to find out minimum
	for (i = 2; i <= arg_count; i++)
		if ((a = va_arg(ap, int)) < min)
			min = a;

	// va_end should be executed before the function
	// returns whenever va_start has been previously
	// used in that function
	va_end(ap);

	return min;
}

// Driver code
int main()
{
	int count = 5;
	printf("Minimum value is %d", min(count, 12, 67, 6, 7, 100));
	return 0;
}
```

### Process vs Thread
Process: Processes are the programs that are dispatched from the ready state and are scheduled in the CPU for execution. PCB(Process Control Block) holds the concept of process. A process can create other processes which are known as Child Processes. The process takes more time to terminate and it is isolated means it does not share the memory with any other process. 

Thread: Thread is the segment of a process which means a process can have multiple threads and these multiple threads are contained within a process. A thread has three states: Running, Ready, and Blocked. The thread takes less time to terminate as compared to the process but unlike the process, threads do not isolate (share data section = global variable, OS resources). Each thread has its own thread control block. 

| S.NO | Process                                                                   | Thread                                                                             |
|------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| 1.   | Process means any program is in execution.                              | Thread means a segment of a process.                                               |
| 2.   | The process takes more time to terminate.                                | The thread takes less time to terminate.                                            |
| 3.   | It takes more time for creation.                                         | It takes less time for creation.                                                   |
| 4.   | It also takes more time for context switching.                           | It takes less time for context switching.                                           |
| 5.   | The process is less efficient in terms of communication.                 | Thread is more efficient in terms of communication.                                 |
| 6.   | Multiprogramming holds the concepts of multi-process.                   | We don’t need multi programs in action for multiple threads because a single process consists of multiple threads. |
| 7.   | The process is isolated.                                                 | Threads share memory.                                                               |
| 8.   | The process is called the heavyweight process.                           | A Thread is lightweight as each thread in a process shares code, data, and resources.|
| 9.   | Process switching uses an interface in an operating system.             | Thread switching does not require calling an operating system and causes an interrupt to the kernel. |
| 10.  | If one process is blocked then it will not affect the execution of other processes | If a user-level thread is blocked, then all other user-level threads are blocked. |
| 11.  | The process has its own Process Control Block, Stack, and Address Space. | Thread has Parents’ PCB, its own Thread Control Block, and Stack and common Address space. |
| 12.  | Changes to the parent process do not affect child processes.             | Since all threads of the same process share address space and other resources so any changes to the main thread may affect the behavior of the other threads of the process. |
| 13.  | A system call is involved in it.                                         | No system call is involved, it is created using APIs.                              |
| 14.  | The process does not share data with each other.                         | Threads share data with each other.                                                |


## OOP

The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

### Constructor vs Destructor

| S. No. | Constructor | Destructor |
| --- | --- | --- |
| 1. | Constructor helps to initialize the object of a class. | Whereas destructor is used to destroy the instances. |
| 2. | It is declared as className( arguments if any ){Constructor’s Body }. | Whereas it is declared as ~ className( no arguments ){ }. |
| 3. | Constructor can either accept arguments or not. | While it can’t have any arguments. |
| 4. | A constructor is called when an instance or object of a class is created. | It is called while object of the class is freed or deleted. |
| 5. | Constructor is used to allocate the memory to an instance or object. | While it is used to deallocate the memory of an object of a class. |
| 6. | Constructor can be overloaded. | While it can’t be overloaded. |
| 7. | The constructor’s name is same as the class name. | Here, its name is also same as the class name preceded by the tiled (~) operator. |
| 8. | In a class, there can be multiple constructors. | While in a class, there is always a single destructor. |
| 9. | There is a concept of copy constructor which is used to initialize an object from another object. | While here, there is no copy destructor concept. |
| 10. | They are often called in successive order. | They are often called in reverse order of constructor. |

### Constructor
Constructors are used to create, and can initialize, objects of their class type.
You cannot declare a constructor as virtual or static, const, volatile.
You do not specify a return type for a constructor.

When a derived class object is created using constructors, it is created in the following order:
1. Virtual base classes are initialized, in the order they appear in the base list.
2. Nonvirtual base classes are initialized, in declaration order.
3. Class members are initialized in declaration order (regardless of their order in the initialization list).
4. The body of the constructor is executed.

#### Explicit
The explicit function specifier controls unwanted implicit type conversions.
It can only be used in declarations of constructors within a class declaration
For example, except for the default constructor, the constructors in the following class are conversion constructors.
```cpp
class A
{  public:
   A();
   A(int);
   A(const char*, int = 0);
};
// A c = A(1) by default converter in constructor
// If specify explicit, then the following is illegal
A c = 1; 
A d = "Venditti";
```
### Destructor
A destructor is a member function with the same name as its class prefixed by a ~ (tilde).
Destructors cannot be declared const, volatile, const volatile or static.
**Destructor can be declared virtual or pure virtual.**

The destructors of base classes and members are called in the reverse order of the completion of their constructor:
1. The destructor for a class object is called before destructors for members and bases are called.
2. Destructors for nonstatic members are called before destructors for base classes are called.
3. Destructors for nonvirtual base classes are called before destructors for virtual base classes are called.

#### Virtual Destructor
Deleting a derived class object using a pointer of base class type that has a non-virtual destructor results in undefined behavior. 
To correct this situation, the base class should be defined with a virtual destructor. 
```cpp
class base {
  public:
    base()     
    { cout << "Constructing base\n"; }
    virtual ~base()
    { cout << "Destructing base\n"; }     
};
 
class derived : public base {
  public:
    derived()     
    { cout << "Constructing derived\n"; }
    ~derived()
    { cout << "Destructing derived\n"; }
};

int main()
{
    derived *d = new derived(); 
    base *b = d;
    delete b;
    getchar();
    return 0;
}
/*
Output:
Constructing base
Constructing derived
Destructing derived
Destructing base //!!!! if no virtual, then this will not output
*/
```

### Encapsulate

Encapsulation is the process of wrapping up objective things into abstract classes, and allowing the class to expose its data and methods only to trusted classes or objects, while hiding information from untrusted ones.

- `public`成員：可以被任意實體訪問
- `protected`成員：只允許被子類及本類的成員函數訪問
- `private`成員：只允許被本類的成員函數、友元類或友元函數訪問

### Inheritance

**[Inheritance](https://www.geeksforgeeks.org/inheritance-in-c/) i**s one in which a new class is created that inherits the properties of the already exist class. It supports the concept of code reusability and reduces the length of the code in object-oriented programming.

```c
class A {
    int a, b;
 
public:
    void add(int x, int y)
    {
        a = x;
        b = y;
        cout << "addition of a+b is:" << (a + b) << endl;
    }
};
 
class B : public A {
public:
    void print(int x, int y)
    {
        add(x, y);
    }
};
```

### Polymorphism

Polymorphism is that in which we can perform a task in multiple forms or ways. It is applied to the functions or methods. 

Polymorphism allows the object to decide which form of the function to implement at compile-time as well as run-time.

Static Polymorphism (Compile-time polymorphism)

```c
class A
{
public:
    void do(int a);
    void do(int a, int b);
};
```

Dynamic Polymorphism ((Run-time polymorphism or call override): use virtual function.

```c
#include "iostream"
using namespace std;
 
class A {
    int a, b, c;
 
public:
    void add(int x, int y)
    {
        a = x;
        b = y;
        cout << "addition of a+b is:" << (a + b) << endl;
    }
 
    void add(int x, int y, int z)
    {
        a = x;
        b = y;
        c = z;
        cout << "addition of a+b+c is:" << (a + b + c) << endl;
    }
 
    virtual void print()
    {
        cout << "Class A's method is running" << endl;
    }
};
 
class B : public A {
public:
    void print()
    {
        cout << "Class B's method is running" << endl;
    }
};
 
int main()
{
    A a1;
 
    // method overloading (Compile-time polymorphism)
    a1.add(6, 5);
 
    // method overloading (Compile-time polymorphism)
    a1.add(1, 2, 3);
 
    B b1;
    // Method overriding (Run-time polymorphism)
    b1.print();
}
```

### Overload
Specify more than one definition for a function name or an operator in the same scope, you have overloaded that function name or operator.
Above is method (function) overload and below is operator overload.

```c
public:
    ComplexNumber(double r, double i) : real(r), imag(i) {}

    // Overload the + operator
    ComplexNumber operator+(const ComplexNumber& other) const {
        return ComplexNumber(real + other.real, imag + other.imag);
    }

    // Display the complex number
    void display() const {
        std::cout << real << " + " << imag << "i" << std::endl;
    }
};
```

### Derive & Override

When you call a function with the same name in the derived class, it **overrides** the base class function (instead of the virtual function).
Derivation allows you to derive a class, called a derived class, from another class, called a base class.

```c
#include <iostream>

class Base {
public:
    void show() {
        std::cout << "Base class function" << std::endl;
    }
};

class Derived : public Base {
public:
    void show() {
        std::cout << "Derived class function" << std::endl;
    }
};

int main() {
    Derived obj;
    obj.show(); // Calls the derived class function
    return 0;
}
```

### Template

Function template

```c
template <typename T> T myMax(T x, T y)
{
    return (x > y) ? x : y;
}
```

Class template

```c
template <typename T> class Array {
private:
    T* ptr;
    int size;
 
public:
    Array(T arr[], int s);
    void print();
};
```

### What is the difference between function overloading and templates?

Both function overloading and templates are examples of polymorphism features of OOP. Function overloading is used when multiple functions do quite similar (not identical) operations, templates are used when multiple functions do identical operations.

### Abstractions

Abstraction means displaying only essential information and hiding the details, abstraction can be use in class and header files. 

1. **Data abstraction –** This type only shows the required information about the data and hides the unnecessary data.

2. **Control Abstraction –** This type only shows the required information about the implementation and hides unnecessary information.

**Abstraction using Access Specifiers: Access specifiers are the main pillar of implementing abstraction in C++. We can use access specifiers to enforce restrictions on class members.**

```c
// C++ Program to Demonstrate the
// working of Abstraction
#include <iostream>
using namespace std;

class implementAbstraction {
private:
	int a, b;

public:
	// method to set values of
	// private members
	void set(int x, int y)
	{
		a = x;
		b = y;
	}

	void display()
	{
		cout << "a = " << a << endl;
		cout << "b = " << b << endl;
	}
};

int main()
{
	implementAbstraction obj;
	obj.set(10, 20);
	obj.display();
	return 0;
}
```

You can see in the above program we are not allowed to access the variables a and b directly, however, one can call the function set() to set the values in a and b and the function display() to display the values of a and b.

### Interfaces

**Interfaces** are nothing but a way to describe the behavior of a class without committing to the implementation of the class. 

In **[C++ programming](https://www.geeksforgeeks.org/c-plus-plus/)** there is no built-in concept of interfaces.

In order to create an interface, we need to create an abstract class which is having only pure virtual methods.

A **[Pure Virtual Function](https://www.geeksforgeeks.org/pure-virtual-functions-and-abstract-classes/)** is a function where we only declare the function but not the function definition.

```c
class GFG  
{ 
  public: 
		// pure virtual function
    virtual string returnString() = 0; 
};
```

### Mutable
**What is the need of mutable?**
Sometimes there is requirement to modify one or more data members of class / struct through const function even though you don’t want the function to update other members of class / struct. This task can be easily performed by using mutable keyword. 
Consider this example where use of mutable can be useful. Suppose you go to hotel and you give the order to waiter to bring some food dish. After giving order, you suddenly decide to change the order of food. Assume that hotel provides facility to change the ordered food and again take the order of new food within 10 minutes after giving the 1st order. After 10 minutes order can’t be cancelled and old order can’t be replaced by new order. See the following code for details.

```c
#include <bits/stdc++.h>
#include <string.h>
using namespace std;

// Customer Class
class Customer {
	
	// class Variables
	string name;
	mutable string placedorder;
	int tableno;
	mutable int bill;

	// member methods
public:

	
	// constructor
	Customer(string s, string m, int a, int p)
	{
		name= s;
		placedorder=m;
		tableno = a;
		bill = p;
	}
	
	// to change the place holder
	void changePlacedOrder(string p) const
	{
		placedorder=p;
	}

	// change the bill
	void changeBill(int s) const { bill = s; }

	// to display
	void display() const
	{
		cout << "Customer name is: " << name << endl;
		cout << "Food ordered by customer is: "
			<< placedorder << endl;
		cout << "table no is: " << tableno << endl;
		cout << "Total payable amount: " << bill << endl;
	}
};

// Driver code
int main()
{
	const Customer c1("Pravasi Meet", "Ice Cream", 3, 100);
	c1.display();
	c1.changePlacedOrder("GulabJammuns");
	c1.changeBill(150);
	c1.display();
	return 0;
}
```

## References
[interview_huihut](https://interview.huihut.com/#/?id=volatile) <br>
[C++八股文](https://www.nowcoder.com/discuss/353158831435882496)