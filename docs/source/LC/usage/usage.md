# C/C++ Usage

## STL

### vector
```cpp
// Initialize 1D vector
vector<> v(size, val)
vector <int> A = {1,2,3};
vector<> v({element})

// Initialize 2D vector
vector<vector<int>> vec(m, vector<int> (n, 0));
vector<vector<int>> A = {{1,2},{3,4},{5,6}};

// Access
v.front();
v.back();

// Operations
vector.push_back // Time complexity O(1)
vector_name.insert(vector_name.begin() + 1, 500);  // Time complexity O(N)
sort(vector.begin(), vector.end())
// it==vector.end() if not found
vector<>::iterator it = find(vector.begin(), vector.end()) 
// clean the vector
vector.clear() 
// Binary search
binary_search (v.begin(), v.end(), 6, cmp)

```

### Unordered_map
```cpp
// Initialize
unordered_map<Key,T> m;
unordered_map<int,int> second = {{1,10},{2,20},{3,30}};

// Access
m->first // key value
m->second //  mapped value

// Find with a specific key, =0 if not found
m.count(key) 

// Erase by iterator
m.erase (m.begin()+2);  
// Erase by a range of iterator
m.erase(m.begin()+3, m.end()) 
m.clear()
```

### Queue
```cpp
// Initialzie
queue<type> q 

// Access
q.front() // the top of a queue
q.pop() // pop out top element
q.push() // push to the end of the queue

//queue has no clear function in C++
while (!Q.empty()) 
    Q.pop();
```

### Priority_queue
Default pq is max heap
```cpp
template <class T, class Container=vector<T>, class Compare = less<typename Container::value_type> > class priority_queue;
```
Define custom comparator 
```cpp
// Min Heap
priority_queue<T,Container, !cmp>

//Max Heap 
priority_queue<T,Container, cmp>

Example:
// use priority queue to implement min heap
auto cmp = [](ListNode*& a, ListNode*& b) {
    return (a->val>b->val);
};

priority_queue<int,vector<int>,greater<int> >
priority_queue<int,vector<int>, !greater<int> >

// decltype : get the type of something
//有時候難以得知一些物件的type，此時就可以透過auto或decltype來解決這個問題。
priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> q(cmp);
```

### Double Linked List
Timing: O(1) remove time and add time, O(n) access time
```cpp
list<pair<int, int>> l; // initialize
l.front()
l.back()
l.push_front(pair<int,int>) // push to the front
l.push_back(pair<int,int>) // push to the back
l.pop_front()
l.pop_back()
list<pair<int, int>>::iterator l.begin(),l.end(), l.rbegin(),l.rend()
l.reverse() // reverse the linked list
l.clear() // clean the linked list
l.splice
/*
 * 
 * The splice() function can be used in three ways:

    1.Transfer all the elements of list x into another list at some position.
    2.Transfer only the element pointed by i from list x into the list at some position.
    3.Transfers the range [first, last) from list x into another list at some position.
*/
list1_name.splice (iterator position, list2)
                or 
list1_name.splice (iterator position, list2, iterator i)
                or 
list1_name.splice (iterator position, list2, iterator first, iterator last)
```
### String
The operation is similar to vector
```cpp
string str = "123";
str.push_back('4');
str.pop_back();

// Operations

// str.begin() + shift 3 = str.end() , "456" is the words to insert
int shift = 3;
str.insert(str.begin()+shift, "456"); 
// Copy three characters from position 1
str.substr(1,3); 
// Compare two strings
compare(str1,str2)  
// 2 and the 3rd arguments is optional
str.find(" ",start_position, length) 
// include begin()+1, but not include end
reverse(str,begin()+1, str.end()); 

string::npos // EOF of the string
```
### Set and multiset
multiset 允許加入重複的資料(排列好)
set不允許加入重複的資料 (排列好 A binary search tree)
unordered_set 即沒有排列的set

```cpp
// Initialize
multiset<int> m;
set<int> s

// Access
m.begin(), m.end(), m.rbegin(), m.rend();

// Operations
int x = 1;
m.insert(x); // m.emplace(x)
m.erase(x);
m.empty();
m.size();
m.find(x);
m.count(x);

// multi set with cmp
auto cmp = [](int a, int b) { return ... };
std::set<int, decltype(cmp)> s;
set<int, function<bool(int,int)>> s([]{return ...;});
```

### Iterator

```cpp
// normal iterator
vector<int>::iterator it;
// reverse iterator
vector<int>::reverse_iterator it;

//Iterate unordered_map
for (auto i = m.begin(); i != m.end(); i++) 
    cout << i->first << " \t\t\t" << i->second << endl; 

//Iterate the vector by reverse order
for(it=vector.rbegin();it!=vector.rend();it++)
```

### Stringstream
Int to string
```cpp
stringstream ss;
int number  = 123456;
ss << number; //把int型態變數寫入到stringstream
string convert_str;
ss >>  convert_str;  //透過串流運算子寫到string類別即可
```
String to Int
```cpp
stringstream ss;
int num;
string numberStr="12345";
ss << numberStr; 
ss >> num;
```
Clean stringstream
```cpp
ss.str("");
ss.clear();
```
#### Split the string
```cpp
string str1 = "/d2/d4/f1";
string str2 = "/d1/../../d2";
string str3 = "hello world hcq!";
string dir;
string dir_list[50];
int i=0;

stringstream ss(str3);
while(getline(ss, dir, ' ')){
    dir_list[i] = dir;
    cout<<dir_list[i]<<endl;
    i++;
}
```