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

**Stack**:

- The stack is managed by the compiler
- It automatically allocates and deallocates memory for local variables and function parameters.
- It typically stores local variables, function arguments, and return addresses.
- The stack provides continuous memory space.
- It has limited space.

**Heap**:

- Heap is managed by the programmer.
- Memory allocation and deallocation are manual (using **`new`**, **`malloc`**, **`delete`**, or **`free`**).
- It provides non-contiguous memory space.
- It offers more flexibility but requires responsible memory management.

Global/static storage area

- divided into two adjacent areas, initialized and uninitialized, to store initialized and uninitialized global variables and static variables.

Constant storage area

- stores constants, generally not allowed to modify.

### Struct vs Class

總的來說，struct 更適合看成是一個數據結構的實現體，class 更適合看成是一個對象的實現體。

- 最本質的一個區別就是預設的訪問控制
    1. 默認的繼承訪問許可權。 struct 是 public 的，class 是 private 的。
    2. struct 作為數據結構的實現體，它預設的數據訪問控制是 public 的，而 class 作為對象的實現體，它預設的成員變數訪問控制是 private 的。

### Extern

Extern is used before the declaration of a variable or a function, to indicate that “this variable/function is defined elsewhere, and is referenced here.

### Volatile

- Variability: This is reflected at the assembly level, that is, the next statement will not directly use the register content of the volatile variable corresponding to the previous statement but will read it again from memory.
- Non-optimizability: volatile tells the compiler not to perform various aggressive optimizations on this variable, or even eliminate the variable directly, ensuring that the instructions written by the programmer in the code will be executed.
- Sequentiality: It can ensure the sequentiality between volatile variables, and the compiler will not perform out-of-order optimization.
- volatile 關鍵字是一種類型修飾符，用它聲明的類型變數表示可以被某些編譯器未知的因素（操作系統、硬體、其它線程等）更改。 所以使用 volatile 告訴編譯器不應對這樣的對象進行優化。
- volatile 關鍵字聲明的變數，每次訪問時都必須從記憶體中取出值（沒有被 volatile 修飾的變數，可能由於編譯器的優化，從 CPU 寄存器中取值）
- const 可以是 volatile （如只讀的狀態寄存器）
- 指標可以是 volatile

```c
volatile bool stop = false;
```

### Define vs Constant vs Inline function

Define (Marco)

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
    

Constant

- const is processed at compile time, with type and type checking
- runtime system allocates memory for const constants
- retaining only one copy of data, saving unnecessary memory space

Inline function: a function that is **expanded in line** when it is called.

- Normally, when a function is called, the CPU performs several steps, including storing the memory address of the instruction following the function call, copying arguments onto the stack, and transferring control to the specified function.
- For small, commonly used functions, the overhead of making the function call can be more significant than the actual execution time of the function.
- Inline functions eliminate this overhead by directly inserting the function code where it’s called.
- 相當於define，卻比 define 多了類型檢查，真正具有函數特性;

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

“free” frees memory but doesn’t call **[Destructor of a class](https://www.geeksforgeeks.org/destructors-c/)** whereas **“delete”** frees the memory and also calls the Destructor of the class.

### **Variable Length Argument in C**

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

## OOP

The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

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

### **Polymorphism**

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

Above is method overload.

Below is operator overload.

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

### Derive

When you call a function with the same name in the derived class, it **overrides** the base class function (instead of the virtual function).

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

### **What is the difference between function overloading and templates?**

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

### Mutable

**What is the need of mutable?**

Sometimes there is requirement to modify one or more data members of class / struct through const function even though you don’t want the function to update other members of class / struct. This task can be easily performed by using mutable keyword. Consider this example where use of mutable can be useful. Suppose you go to hotel and you give the order to waiter to bring some food dish. After giving order, you suddenly decide to change the order of food. Assume that hotel provides facility to change the ordered food and again take the order of new food within 10 minutes after giving the 1st order. After 10 minutes order can’t be cancelled and old order can’t be replaced by new order. See the following code for details.

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