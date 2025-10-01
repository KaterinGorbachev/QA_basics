# Python 

## Syntaxis 

### Quotes ¨¨

- single ´´´ or double ¨¨¨¨ - up to three quotation marks in a row, can be outside, both single and double -
```python 
print ("""I like a lot "Lord of rings".""")
```

Triple quotes - to enclose multi-line string data:
```python 
print("""One 
Two
Three""")
```
String operators must be enclosed in quotes

### ,

- separate values ​​in one function using commas - print('I love pdf' , table)

	- When multiple arguments are passed to the print function, they are automatically separated by a space when printed.

### #

- After the barcode the code is not executed 

### equals =

-  assiment from right to the left - return function on the right 

	- to asignate

		- low priority

### exclamator and equals !=

- left part not equal to the right part 

### ==

- to compare values

	- the first step is to count expressions on the right  or left and only after that - compare

		- low priority

			- the result in print() is True or False

### 4 first spaces 

- to determine that the next part is used only for some conditions thar are above
  
```python
name = input("What's your name? ")

match name: 
    case "Harry" | "Hermione" | "Ron": 
         print("Gryffindor")
    #case "Hermione": 
        #print("Gryffindor")
    #case "Ron":
        #print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _: 
        print("Who?")
```

### |

- means or

### colon :

- to event a function 
```python
while i != 0: 
    print("meow")
```
```python
def main():
   x = int(input("What's x? "))
   if is_even(x): 
      print("Even")
   else: 
      print("Odd")
```
### +=

- to add smth to the  argument

	- i += 1 means i = i + 1

- to add one string to the other 
```python
full_name = first_name + ' ' + last_name
```
### _

- to add variable that name is not necessary (in loops)  - only for python 
```python
for _ in range(3):
    print("meow")
```
		

### asterisk *

- to multiply function print - only for python
```python
print ("meow" * 3) 
```
		 

### \

- to divide instruction in a few lines 
```python
result = var1 * 2 + var2 * 3 \
         var3 * 4 + var4 * 5
```

- when the functions argument is in the parentheses () - is not necessary to use \ for  such division by lines 

- screening

	- to put the new line
 
```python
print ("meow\n" * 3)
```

- \n

	- to make printing to the next gorizontal tab position 

		- \t

			- print('Mn\tTu\tWnd')

				- Horizontal Tab
```python
print ('\t' * level + 'indented text')
```

```python
print ((' ' * 4) * level + 'indented text')
```

- to print one quote 

	- \'

	- to print backslash

		- \\

	- \r

		- Carriage Return

	- \b

		- Backspace

	- \f

		- Formfeed

	- \v

		- Vertical Tab

	- \0

		- Null Character

### curly parentheses/ braces {}

- create dictionary

	- {"Hermiome": "Gryffindor", "Harry": "Gryffindor"}

		- keys : values

- create F-string
{} is a placeholder for a variable or expression

	- with F-string make messages which contain variable and do format of a numbers in different way 
	```python
		name = input("what's name? ")
		print(f'Hello, {name}.')
 	```

- using of variable in an expression in the {}, like {val + 2} - does not change the value of variable val

- specify a format 
the subsequence of markers
[align] [width] [,] [rounding] [type]

	- rounding floating point numbers

		- .2f or .3f or .1F y etc

	- to put coma as a separator 

		- {number:,.2f}

	- to convert a float number into percent's

		- {discount:.0%}

	- to show a number as an integer 

		- {number:d}

	- to specify the minimum field width, while it will be extended automaticaly  if necessary 

		- {number:10}

	- align to edge, note that automatically will be align at the left side

		- left 

			- {number:<10d}

		- right 

			- {number:>10d}

		- middle

			- {name:^20}

### brackets []

- to make a list

### keywords

- end=""

	- to eliminate additional blank line

		- only for python 

- sep=", "

	- to change a separator between arguments

	- needs to have min 2 arguments

- key words go after arguments of position always 

## Mathematical operators

### +

- Addition

### -

- Subtraction

### *

- Multiplication

### /

- Division

	- always returns float

### //

- Integer division

	- floor division

### %

- Remainder of the division

### **

- Exponentiation 

### priorities' of operators:
1. Exponentation
   ```python
		 **
   ```
2. ```python
   * / // %
   ```
3. ```python
   + -
   ```

## Variable naming rules

### Character case

- Variable names are case sensitive

### The use of Python keywords is prohibited

### Without spaces

### The first character must be one of the letters a through z / A through Z or an underscore _

### Names must not start with a number 

## Numeric literals

### It is forbidden to use currency symbols, spaces or commas

- for Python 3.6 - you can use underscore to separate parts in 1 number

	- 10_000_000 = 10000000

### The input function always returns the input as strings

- int(argument) 

	- Returns the argument as an integer type 

		- ```python
    		hours = int(input('How many hours you have been working? ')
    	```

- float(argument)

	- Returns the argument as a real type

		- operation with int y float returns float

			- 0.4 = .4

			- 4.0 = 4.

- exponent

	- 3E8

		- means 3 x 10 in 8 degree

	- the same 3e8

### negative number 

- -1,-2,-3

## str

### strings

- to connect strings in one  
	```python
	 name = "Jon" + "Adams"
 	```

- to multiply strings

	- 5 * 'a'

- immutable 

### methods

- index('a')

	- searches the sequence from the beginning, in order to find the first element of the value ('a') specified in its argument.

- .count("b")

	- count repeats of a character 

- isalnum()

	- returns True if all elements are letters or numbers and at least one symbol

	- if there are spaces - returns False

- isalpha()

	- returns True if all elements are letters and at least one symbol

- isdigit()

	- returns True if all elements are  numbers and at least one symbol

	- isnumeric()

	- isdecimal()

- islower()

	- all letters are lowercase and at least there are 1 letter

- isupper()

	- all letters are uppercase and at least there are 1 letter

- isspace()

	- returns True if contains spaces or new line (\n) or tabulation (\t) and at least one symbol 

	- if there are words or numbers also - returns False

- MODIFICATION METHODS: 

- split()

	- returns a list of words from the string that are separated with spaces, \n, \t 
split(separator) - the separator can be given

- join()

	- the method performs a join and expects an argument of type list; you must ensure that all elements in the list are strings; otherwise, the method will throw a TypeError exception.
All elements in the list will be joined into a single string, but...
...the string from which the method was called will be used as a separator, placed between the strings.
The newly created string is returned as the result.

	- ```python
   		print(",".join(["omicron", "pi", "rho"]))
   	```

- Output: omicron,pi,rho

	- works with tuple

		- ```python
    		",".join(("omicron", "pi", "rho"))
    	```

- center()

	- generates a copy of the original string, attempting to center it within a field of a specified width.

		- ```python
    		print('[' + 'gamma'.center(20, '*') + ']')
    	```

	- It is actually done by adding some spaces before and after the string

		- ```python
    		print('[' + 'alpha'.center(10) + ']')
    	```

- lower()

	- Generates a copy of a string, replaces all uppercase letters with their lowercase equivalents, and returns the string as the result. Again, the original string remains intact.

- upper()

	- It returns a new string where all characters that are lowercase letters are converted to their uppercase counterparts.

Non-alphabetic characters (like numbers, symbols, or spaces) are not affected.

The original string remains unchanged (strings are immutable in Python).

- title()

	- changes the first letter of each word to uppercase, converting all other letters to lowercase

- capitalize()

	- Creates a new string with the characters taken from the source string, but attempts to modify them as follows:
- If the first character in the string is a letter (note: the first character is the element with index equal to 0, not the first visible character), it will be converted to uppercase.
- All remaining letters in the string will be converted to lowercase.

- the result must be used or saved or it will be lost 

- swapcase()

	- creates a new string by swapping all letters to uppercase or lowercase within the original string: uppercase characters become lowercase and vice versa.

- lstrip()

	- all leading spaces deleted (spaces, \n, \t) - from the beginning of the string

	- lstrip(symbol)

		- returns string without the given symbol at the beginning

- rstrip()

	- returns string where all spaces at the end were deleted

	- rstrip(symbol)

		- returns string without the given symbol at the end

		- It keeps going from right to left, removing any of those characters until it hits a character not in that set.

			- print("cisco.com".rstrip(".com"))

				- cis

- strip()

	- returns string without the beginning and ending spaces symbols

	- strip(symbol)

		- returns string without the beginning and ending given symbols

- COMPARATING METHODS: 

- endswith(substring)

	- returns True or False

- startswith(substring)

	- Subtopic 1

- find(substring)

	- returns the lowest index where substring was found, or if not found - returns -1

		- to find the first position

	- find('a', 100)

		- starts finding from the position 100 

	- rfind()

		- the same functionality, but starts from the end of a string (r - reverse)

- replace(old, new)

	- returns a changed copy of a string 

		- ```python
    		print("This is it!".replace("is", "are"))
    	```

	Output: Thare are it!

	- used to delete symbols

		- ```python
    		print("Apple juice".replace("juice", ""))
    	```

	- with a limit of replacing in 1

		- ```python
    		print("This is it!".replace("is", "are", 1))
          ```

- CHAIN METHODS

	- ```python
   		s = s.replace('fácil', 'difícil').replace('im', '')
   

- filter()

	- Using Python’s filter function allows us to return a subset of a sequence for which a certain condition is true.

		- gryffindors = filter(is_gryffindor, students)

### to search in a string

- for item in string: 
```python
name = "Julia"
for item in name: 
     item = "x"
print name
```
- will print "Julia", operation in for does not affect string

- immutable: cant be changed after creating

- indexes

	- name[0] J - name[4] a


	- -index : to access end of the string
it plus negative index to the length of the string 

		- name[-1]a - name[-5]J

### slices

- string[start : end]

- string[start : end : step size]

### to check the sting elements

- in

- not in

### functions

- ord(string[0])

	- to know the ASCII/UNICODE code point value of a specific character

		- print(ord(char_1))

- chr(string[0])

	- takes a code point and returns its character.

		- def mi_capitalize(line: str): 
    if ord(line[0]) in range(97,123): 
        return chr(ord(line[0]) - 32) + line[1:]
    else:
        return line
    
lines = 'zipaTata'
print(mi_capitalize(lines))

- min(string)

	- finds the minimum element of the sequence passed as an argument

- max(string)

	- finds the maximum element of the sequence passed as an argument

- len(string)

- list(string)

	- takes its argument (a string) and creates a new list containing all the string's characters, one per list element.

	- sorted(lista)

		- does not change original

	- lista.sorted()

		- does change original

- str()

## list

### list is an enterable object 

- Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory 

- Pass-by-reference

### for i in [0,1,2]:

- values ​​in square brackets are list

	- print([0]) = print the 0, print([2]) = print 2 when it is the third number in the list

### methods 

- nameOfList.method()

	- changes ususally the list and does not need a new variable to save changings

		- changes the object of the method - changes the state of the list

- append()

	- list.append(value) - adds the value (1 argument)  to the end of the list

		- list = []

for i in range(10): 
    n = int(i+1)
    list.append(n)

print(list)

			- exit

				- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

- insert()

	- 2 arguments: first position 
second - value

		- list.insert(location, value)

			- list = []

for i in range(10):
    #n = int(i+1)
    list.insert(-10, i+1)

print(list)

				- exit

					- [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

- to sort list

	- list.sort()

		- method

			- changes the list and does not need a new variable to save changings

	- list.reverse()

		- method

	- sorted(list)

		- function - need to save in one variable the result of function

- index(value)

	- shows the index, position of the element in the list

		- nameOfList.index()

- enumerate()

	- returns tuple with position and value in the list

- copy()

	- other way to make a copy 

		- list = list [:]

		- list2 = [] + list1

- count()

	- returns number of elements that repeats

- remove(value)

	- removes the first appearance of the value in the list

- reverse()

	- inversion of the values order in the list 

### functions

- function list()

- range()

	- is a function for range of values

		- for i in range(3):

			- more info in Loops

- function len()

	- gives the length of the list

		- the last position in the list is len(list) - 1

		- always gives the normal number length, starting counting the elements from 1

### operations with lists

- del

	- del list[]  - to delete content of the list

		- del list[:]   -   slice does not make any new list

			- will give error if del list[:] is on the right of = 

	- del list   - to delete whole list

- to check if element is in the list 

	- returns True or False 

		- elem in my_list

		- elem not in my_list

- list comprehension 

	- row = [WHITE_PAWN for i in range(8)]

- change the value in one position 

	- auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary


		- only for python  - right part

			- variable_1, variable_2 = variable_2, variable_1

			- my_list[1], my_list[2] = my_list[3], my_list[5]

- *

	- Unpacking We can use * to unpack the list so that all the elements in the list can be passed as different parameters

		- print(*([c] * 5), sep = ' | ')
rabble | rabble | rabble | rabble | rabble

- min(my_list)

	- max(my_list)

### index

- positive

- negative

	- the last element - list[-1]

### slices 

- Slices work on lists just as with strings, and can also be used to change sub-parts of the list

	- list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']


- my_list[start:end]

	- index

		- positive

			- [0:len(my_list) - 1]

		- negative

			- first element - my_list[len(my_list)*-1]

		- 3 indexes - the third gives the pass

			- list[::2] every third element 

			- list[::1] every second element

	- start is included in the new list 

	- end is excluded in the new list

- allows you to make a new copy of a list, or parts of a list

	- to copy list with list inside 

		- copy.deepcopy()

			- import copy 
c = copy.deepcopy(a)

	- list_1 = [1]
list_2 = list_1[:] #copy all the list_1
list_1[0] = 2
print(list_2) #[1]

- lists inside the list 
nested list

	- board[1][0] 

		-  [0] is position in row, in the internal list

		- [1] is position in column, is the position of internal list in the external list

		- >>> list1 = [[10,13,17],[3,5,1],[13,11,12]]
>>> list1[0][2]
17


	- list 3 dimensions

		- red - room, green - plant, violet - hotel

		- rooms = [ [ [ [1,2,3], [4,5,6] ],[  ] ], [] ]

		- rooms[hotel][plant][room]

- list[0:0]   - is an empty list 

### list comprehension 

- to fill the list 

	- row = [WHITE_PAWN for i in range(8)]

	- board = [[EMPTY for i in range(8)] for j in range(8)]



- condition comprehension

	- expression_one if condition else expression_two

		- the_list = [(1 if x % 2 == 0 else 0) for x in range(10)]

### [lista[0]]

- to make smth to be a list

	- return [lista[-1]] + invert_list(lista[:-1])

## tuple

### immutable collection of data
can not change the value

- def main():
    name, house = get_student()   #student = get_student()   to assign value tuple to variable student
    print(f"{name} from {house}")   #print(f"{student[0]} from {student[1]}")    


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)                #returns 1 value - tuple


if __name__ == "__main__":
    main()



- Type error 

	- tuple object does not support item assignment

- nested tuple is possible

### a = (1,)     - a is tuple 
a = 1,       - a is tuple

### can work with positions in tuple

- my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

### to delete last element

- t3 = t2[:-1]

### functions

- count() - 	returns number of elements that repeats

- len()

- tuple()

	- makes a tuple from a list

### join tuples

- t2 + t3

### multiply tuples

- t2*3

### The in and not in operators work the same way as they do in lists.

### tuples may appear on the left side of the assignment operator

- x,y = y,x

### tuple with 1 element 

- my_tuple = (1, )

## dictionary

### dictionaries or dict, are a data structure that allows you to associate one value with another

- keys - values

- key must be unique

- print(phone_numbers['Suzy'])

	- returns phone number 

### use curly quotes {}

### None

- key word in Python for absence of a value 

### The order in which a dictionary stores its data is beyond our control.

### def get_student():
    student = {}
    student["name"] = input("Name: ")   #first key
    student["house"] = input("House: ")  #second key
    return student

- def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house} 

 #introducing keys in the return line

### print(dictionary['gato'])  -----> valor

- if key is not exists ----> Key Error

	- Keys are case sensitive

	- Keys are type sensitive - str or int or float y etc

	-     if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")


### methods for dictionaries

- keys()

	- A dictionary is not a sequential data type - the for loop is not useful here.

	- dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

	- with function sorted()

		- for key in sorted(dictionary.keys()):

	- The keys() method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion

- items()

	- returns a list of tuples

		- where each tuple is a pair of each key with its value

			- dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)


- values()

	- returns only values

		- my_dict = {'a': 10, 'b': 20, 'c': 30}
values = my_dict.values()

print(values)  # Output: dict_values([10, 20, 30])

- update()

	- dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary.update({"pato": "canard"})
print(dictionary)

- get()

	- print(dictionary.get("gato"))

		- if you use wrong key in get() --- returns None

			- you can use None in the condition   if None:

		- Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError

		- if he does not find key can return a specified value

			- print(dictionary.get("gatos", "patatas"))       ---- returns patatas

	- the same as print(dictionary["gato"])

- del dictionary["perro"]

	- deletes key and value

- popitem()

	- delete the last element of a dictionary, a key and a value

- pop()

	- result = dictionary.pop("gato")
print(result)
print(dictionary)

		- chat 
{"perro" : "chien", "caballo" : "cheval"}


			- pop deletes the key and value of a specific key

- clear()

	- empties dictionary 

- copy()

	- copies dictionary in full

		- b = dictionary.copy()

	- to copy one element use tuple and assignation 

### functions

- len(dict)

- sorted(dict)  

- dict()

	- makes a dictionary from tuple or from a list with 2 elements 

### dictionaries are mutable

- to add

	- to add new key

		- dict['newkey'] = 'newvalue"

	- You just need to assign a value to a new key that has not existed before.

- to change 

	- dictionary = {"gato" : "perro", "dog" : "chien", "caballo" : "cheval"}

dictionary['gato'] = 'minou'

	- cant change key, only delete and add new key

	- dictionary = {"gato" : 1, "dog" : "chien", "caballo" : "cheval"}

dictionary['gato'] += 1

		- gato: 2

## class

### creation of an object

creating custom data type

- class Student:       #may or may not have some
                             # future functionality as well
    ...


def get_student():        
    student = Student()   #creating object from class
    student.name = input("Name: ")   #instant variables
    student.house = input("House: ")   #atribute for house
    return student


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

- mutable, but you can make them immutable

- Composition is the process of composing an object using other different objects

	- composition projects a class as a container able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior.

		- class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())


### Inheritance

- create a class that “inherits” methods, variables, and attributes from another class.

	- class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  ##access to the Wizard class
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
...



		-  Both students and professors have names. Also, both students and professors are wizards. Therefore, both Student and Professor inherit the characteristics of Wizard. Within the “child” class Student, Student can inherit from the “parent” or “super” class Wizard as the line super().__init__(name) runs the init method of Wizard

	- Python forces you to explicitly invoke a superclass's constructor

		- by using class name

			- class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

		- by using function super()

			- super().__init__(name)

				- class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


			- you can use this mechanism not only to invoke the superclass constructor, but also to get access to any of the resources available inside the superclass.

	- how to check if there is inheritance 

		- function

			- issubclass()

				- issubclass(ClassOne, ClassTwo)

				- returns True and False

					- if a particular class is a subclass of any other class

				- each class is considered to be a subclass of itself.

			- isinstance()

				- whether it is an object of a certain class/ superclass or not.

				- isinstance(objectName, ClassName)

	- is

		- The is operator checks whether two variables (object_one and object_two here) refer to the same object.

		- object_one is object_two

	- object1 == object2

		- checks if the objects content is the same

- multiple inheritance

	- when a class has more than one superclass

		- class Sub(SuperA, SuperB):
    pass


	- overriding

		- class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())

			- -----> 200 201 

The entity defined later (in the inheritance sense) overrides the same entity defined earlier

	- class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Right, Left):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())


		- checks a variable var first in the class Right and then in the class Left

- Inheritance and Exceptions

	- BaseException
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- KeyError
      +-- NameError
      +-- SyntaxError
      |    +-- IndentationError
      +-- ValueError
 ...

- Class hierarchies

	- the hierarchy grows from top to bottom, like tree roots, not branches. The most general, and the widest, class is always at the top (the superclass) while its descendants are located below (the subclasses).

- adding functionality to the child class

	- class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


    def push(self, val): 
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
    val = Stack.pop(self)
    self.__sum -= val
    return val


		- using superclass method in the child class, which already exists

		- __sum is totally hidden variable - requires a get method to return it 

			- def get_sum(self):
    return self.__sum


- polymorphism

	- the subclass is able to modify its superclass behavior 

	- abstract method

		- class Animal: 
    
    def __init__(self, especie, edad):
          self.especie = especie
          self.edad = edad

    def hablar(self): 
         pass       

			- class Perro(Animal): 
     
     def hablar(self): 
          print("Gua")  

### operating overloading

- class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)



### variables global and private 

- balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance    ###reserved word global
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()



	- Classes allow us to solve this issue of needing a global variable more cleanly because these instance variables are accessible to all the methods of this class utilizing self

		- class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()



		- self._balance

			- only indicates that variable is private, but that can be changed from outside

		- self.__balance

			- two _ - changes the name of variable, so that its harder to change from the outside

			- obj = Account()
print(dir(obj)) 

				- to see the new name of a balance

- private

	- 1 underscore

		- self._balance

	- 2 undercsores

		- By using a leading double underscore, you can ensure that certain attributes or methods of your class are only accessible from within the class itself. This can help to prevent accidental modification of important internal state, and make your code more robust and maintainable. However, it’s important to note that this does not provide true encapsulation, as the mangled name can still be accessed from outside the class if you know the name.

			- is still accessible from outside the class using a mangled name constructed as _ClassName__PrivatePropertyName

			- version_2._Python__venomous = not version_2._Python__venomous

		- self.__my_private_variable = 42

		- The mangling won't work if you add a private instance variable outside the class code.

- class Persona: 

    ## variables Class
    fallecido = False 
    contador = 0 

    ## variables Objects
    def __init__(self, nombre, apellido, edad=30): 

        self.nombre = nombre
        self.apellido = apellido 
        self.edad = edad 
        #self.fallecido = True
        self.poderes = []
        Persona.contador +=1 



    def nombre_completo(self): 

        ## variables of Methods 
        patata = 27

        return "{} {} {}".format(self.nombre, self.apellido, self.edad)
    

- instance variables

	- closely connected to the object not to the class

		- class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

- A class variable is a property which exists in just one copy and is stored outside any object.
A class variable exists in one copy even if there are no objects in the class.

	- a class variable always presents the same value in all class instances (objects)

		- class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

- AttributeError

	- Different objects of the same class may have different attributes 

		- checking attribute existence

			- try:
except:

			- function

				- hasattr(example_object, 'b')

					- 
the class or the object being checked;
the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)


					- can use it to find out if a class variable is available

					- returns True or False

### methods

- method is obliged to have at least one parameter 

	- The self parameter is used to obtain access to the object's instance and class variables.

- of a class

	- @classmethod

		- is a function that we can use to add functionality to a class as a whole

			- class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()



				- Notice that get_student is removed and a @classmethod called get is created. This method can now be called without having to create a student first.

			- import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):           #cls - ref to class
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")



			- class Pastel: 
    def __init__(self, ingredients, tam): 
        self.ingredients = ingredients
        self.tamanyo = tam 

    def estado(self): 

        return "Pastel --> Ingredientes: {}, Tamaño: {}".format(self.ingredients, self.tamanyo)
        

    @classmethod
    def Pastel_Chocolate(cls, tam): 

        return cls('Harina, Leche, Huevos, Chocolate', tam)
    
    @classmethod
    def Pastel_Vainilla(cls, tam): 

        return cls('Harina, Leche, Huevos, Vainilla', tam)
    ## devuelva un objeto

	- prescribed functions for a class
actions they can perform

		- class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"



			- function charm(self) by convention must take at least 1 argument called self - to get access to the current object of a class Student

			- def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

	- methods for classes 

		- __init__

			- class Student:
    def __init__(self, name, house):   #gives the opportunity  to customize the class object
        self.name = name
        self.house = house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)     # a constructor call
    return student


				- initialization method

		- __str__

			- Python allows you to create a specific function by which you can print the attributes of an object.

				- class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


					- only takes 1 argument called (self) by convention

				- class Mouse:
    def __str__(self):
        return "Mouse"


class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()




			- the return object is a string and so print() is useful

	- to check the class name

		- the __name__ attribute is absent from the object - it exists only inside classes

			- print(Classy.__name__)

		- function

			- type(object)

	- to check direct superclasses for the class

		- __bases__

		- a class without explicit superclasses points to object (a predefined Python class) as its direct ancestor

	- to check the name of the module that contains a class

		- __module__

			- print(Classy.__module__)

- of an object

	- __dict__

		- The variable contains the names and values of all the properties (variables) the object is currently carrying

			- print(example_object_1.__dict__)

		- does not work with a class

- decorators

	- @staticmethod

		- @staticmethod
    def tam_area(t): 
        return t**2*math.pi
    ### t is a size given from outside 

			- does not need self

	- class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house  #calling the setter method from the class  #.house because the setter method called house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for house
    @property
    def house(self):    
        return self._house     #inside the class you should use different names for variables, functions, values 

    # Setter for house
    @house.setter
    def house(self, house):     
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()



		- class Student:
    def __init__(self, name, house):
        self.name = name    #self.name without underscore to make this lines call setter 
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


	- deleter

		- @mi_atributo.deleter
    def mi_atributo(self): 

        del self.__mi_atributo


- __privateMethod

### introspection, which is the ability of a program to examine the type or properties of an object at runtime

### reflection, which goes a step further, and is the ability of a program to manipulate the values, properties and/or functions of an object at runtime

## generators 

### __iter__() which should return the object itself and which is invoked once (it's needed for Python to successfully start the iteration)

- def __iter__(self):
        print("__iter__")
        return self

### __next__() which is intended to return the next value (first, second, and so on) of the desired series

- if there are no more values to provide, the method should raise the StopIteration exception

- def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

### yield instead of return

- def fun(n):
    for i in range(n):
        yield i


	- such a function should not be invoked explicitly

	- the invocation will return the object's identifier, not the series we expect from the generator

- from backend.db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

	- Instead of the caller worrying about cleanup, get_db ensures that:

It gives the caller a usable session (yield db).

After the caller is done, the session is always closed (finally: db.close())

		- from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(MyModel).all()

			- FastAPI sees get_db() is a generator.

It runs it until the first yield → gives db to your endpoint function.

After the endpoint finishes, FastAPI continues the generator, executing finally: db.close().

### the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

## Loops

### event a condition 

- while

	- for loop with condition 

		- i = 3 
while i != 0: 
    print("meow")
    i = i - 1

			- indefinite loop 

				- one that goes forever 

					- while True:  + condition 

						- input() can be inside the loop while True

					- while False + condition 

				- to have a conditions for the loop termination - that checks in while that the condition is False

					- condition is 

while True:
    n = int(input()) 
    if n < 0:
           continue 
    else: 
        break

	- while i<5:
    i = i+1 
    print(i)

		- gives 5

- for 

	- for i in range(5): 
     print(i)

		- gives 4

	- for loops with counter
does not have a condition

		- for 

			- for student in students: 
      print(student)  

				- in dictionary prints keys by design 

			- loop inside the loop 

				- the syntax of the for loop requires at least one statement within the body 

			- power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

				- expo is control variable that starts with 0

					- control variable - is that one after for

			- inerrable object is after in - always must be 

				- for i in (10): - tuple 
for i in [1,2]: - list 
for i in "idea": - string 

			- range()

				- for i in range(5): 
    print(i)

					- range is - 0,1,2,3,4 but not 1,2,3,4,5 - 5 does not enter the loop

				- argument only int

				- can take 3 arguments 

					- 2 arguments means initial and the last -1
range(2,10) - from 2 to 9 


					- 3arguments 
- first initial 
- second - second is the end 
- third is the step - means the difference between each number in the sequence of numbers generated by the function

					- an ascending order only

						- range(10,2, 1) does not function without Error message

						- range(10,2,-1)  does function 

- 
break 

continue 

	- always inside for or while

		- break in while 

			- break - stop executing the condition after the first interaction 

				- i = 1
while i < 5:
    print(i)
    i += 1
    break 
else:
    print("else:", i)


					- output  else:1

		- break in for 

			- print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

				- breaks the loop at 3

					- The exit of the program will be:

						- La instrucción break:

Dentro del bucle. 1

Dentro del bucle. 2

Fuera del bucle.


			- end = 6
or i in range (0, end-1) :
    print(i)
    break 
else: 
    print("else", i) 

				- output 0
else does not execute

		- while:
    .
    .
    break
else: 

			- for:
    .
    .
    break
else: 

		- continue

			- print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

				- skips 3 

					- The exit of the program will be:

						- La instrucción continue:

Dentro del bucle. 1

Dentro del bucle. 2

Dentro del bucle. 4

Dentro del bucle. 5

Fuera del bucle.

### bool type of data

- True

	- ==1

		- if number%2 == 1:
 is the same as 
if number%2:

	- all symbols but not 0 are True in Python 

- False

	- ==0

		- while number != 0: 
is the same as 
while number:

	- 0 is the same as False

- after operations ==, !=, >, >=,  <, <=

	- first are <, <=, >, >=

### conditions

- if condition True or False: 

	- always needs min 1 line of code inside

	- if-else

		- if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

	- elif

		- else - if

			- the sequence/ order is important 

				- if condition: 
   action  
elif condition:
   action 
elif condition:
    action 
else: 

					- can be called waterfall 

					- one first if is obligated 

					- do not pass the other lines after he finds first true line

					- else always is at the end / else is optional 

	- conditions

		- cant use x == "A" or "B" 

			- should use x == "A" or x == "B"

				- condition and condition 

					- if any is False the if does not work as all is a False 

						- = multiplication

				- condition or condition 

					- if one or both are True - the if works as the sum of conditions is True 

						- if x == 0 and (x == 10 or x == 20): 

							- the use of brackets ()

				- not condition 

					- not True 

						- Morgan laws 

							- not (p and q) == not p or not q 

							- not (p or q) == (not p) and (not q)

					- not not True == True

### lambda function

- A lambda function is a function without a name (anonymous function)

	- returns the value of the expression when taking into account the current value of the current lambda argument

- declaration

	- lambda parameters: expression

- def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

- map()

	- this function applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent function results

		- list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

- filter()

	- it filters its second argument while being guided by directions flowing from the function specified as the first argument

		- from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

## Regular expressions

### import re 

- you specify the rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like. You can then ask questions such as “Does this string match the pattern?”, or “Is there a match for the pattern anywhere in this string?”. You can also use REs to modify a string or to split it apart in various ways.

	- https://regex101.com/

### operations bit - bit 

- a&b 

	- a and b

- a|b

	- a or b 

- ~a

	- not a

- ^a

	- xor

### non-exhaustive list of patterns

- .   any character except a new line (point)

- *   0 or more repetitions

- +   1 or more repetitions

- ?   0 or 1 repetition

- {m} m repetitions

- {m,n} m-n repetitions

- ^   matches the start of the string

- $   matches the end of the string or just before the newline at the end of the string

- [ ] set of characters

- [^] complementing the set

- \d    decimal digit

- \D    not a decimal digit

- \s    whitespace characters

- \S    not a whitespace character

- \w    word character, as well as numbers and the underscore

- \W    not a word character

- A|B     either A or B

- (...)   a group

- (?:...) non-capturing version

### re

- regular expressions library

	- re.IGNORECASE

	- re.MULTILINE

	- re.DOTALL

- import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")



	- in the documentation of the function use group from 1 not from 0

- import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")



	- :=   only equal 

- re.sub(pattern, repl, string, count=0, flags=0)

	- import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))



		- re.search

		- matches.group(1) catches (www.)

			- import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))



### import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")



- if re.search(r".+@.+\.edu", email):

	- \ to read point as a point
r"...." to read the row as a regular expression not to make \ be read as a new line

- if re.search(r"^[^@]+@[^@]+\.edu$", email):

	- [^@] any character except @

- [a-zA-Z0-9_]

- if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):

	- to do search in different top level domains

- if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):

	- to add second low level domain with 0 or 1 repetition -  (\w+\.)?

- oficial browsers regular expression 

	- ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

### import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = first + " " + last
print(f"hello, {name}")



## Code Style

### PEP 8

- Python enhancement proposal

	- peps.python.org/pep-0008/

		- readability counts

 

			- indentation

			- Tabs or Spaces?

				- no Tab only 4 Spaces

			- Maximum Line Length 

			- Blank Lines

			- Imports

		- pylint - program that check your code style

pycodestyle.pycqa.org

		- pycodestyle - program to check style and reformating code style for you 

		- black - program to check style 

black.readthedocs.io

command line: black file.py

### closure 

- is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore

	- def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

	- def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

		- it can also modify its behavior by using values taken from the outside

## Special constructs

### if __name__ == "__main__":

- use of Python's name equals main syntax is considered a best practice, especially in applications that might contain multiple components or several files that contain runnable code

	- if __name__ == "__main__":
      print("Hello world")

		- The if name equals main block guards the print statement, to ensure it executes only when the file is intentionally run directly as a script or application.

			- the developer protects the print statement from being executed as unguarded, top-level code.

	- if __name__ == "__main__":
       main()

## File I/O  - input y output of files 

### code car read from or write to files themselvs

- sorting in the file

	- names = []

with open("names.txt") as file:
     for line in file: 
         names.append(line.rstrip())
         #appending to the list not to the file

#outside from with cycle
for name in sorted(names): 
     print(f"hello, {name}")


		- more simply for python 
to use sorted function on the file themselves 
but cant do the changings to the text only sorting

			- with open("names.txt") as file:
     for line in sorted(file): 
         print("hello,", line.rstrip())

	- docs.python.org/3/library/functions.html#sorted 

		- sorted(iterable, /, *, key=None, reverse=False)

iterable - names

			- for name in sorted(names, reverse=True): 
     print(f"hello, {name}")

- to add more than 1 parameter 

	- code students.csv

		- code to read columns 

			- with open("students.csv") as file: 
    for line in file: 
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

				- more readable 
when the text is positioned like here

					- with open("students.csv") as file: 
    for line in file: 
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

	- students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name is in {house}")
#appending to a list


for student in sorted(students): 
     print(student)

		- not to sort by the sentences 
to collect info before sintering
with supports dictionary 

			- students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {} #empty dictionary 
        student["name"] = name  
        student["house"] = house 
        students.append(student)    #to fill dictionary

for student in students: 
      print(f"{student['name']} is in {student['house']}")   #student is a name of a variable, [for name and house] #ordinary quotes 
        

### functions

- open file

	- function - open 

		- docs.python.org/3/library/functions.html#open

		- stream = open(file, mode = 'r', encoding = None)



		- Text mode 	Binary mode 	Description
rt 	                 rb 	                  read
wt 	                 wb 	                 write
at 	                 ab 	                 append
r+t 	                 r+b 	                 read and update
w+t 	                 w+b 	         write and update


x - only creates file


	- open only for reading, file cant be changed or modyfied

		- customer_file = open('customers.txt', 'r')

	- open file for writing
if file exists => removes its content! 
if file does not exists => creates a file

		- customer_file = open('customers.txt', 'w')

	- open file in which lines will be added. New adds at the END of the file. If file does not exists => creates file

		- customer_file = open('customers.txt', 'a')

	- if there are no path for the file, it is thought that the file 'customers.txt' is in the same place as the main program/ or the file is created in the same folder

		- specificize the path

			- test_file = open(r'C:\Users\temp\test.txt', 'w')

			- have to use two different separators for the directory names: \ in Windows, and / in Unix/Linux

- import os 
to use functions remove and rename

	- os.remove('old.txt')
os.rename('temp.txt', 'old.txt'

		- emulates changing data in a file, but more effective is to use database

- import sys



	- Three predefined streams are already open when the program starts

	- sys.stdin

		- the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs

		- input()

	- sys.stdout

		- the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program

		- print()

	- sys.stderr

		- associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors encountered during its work

### methods

- write into the file

	- list 

		- names = []

for _ in range(3):
   # name = input("Whats your nme? ")
    names.append(input("Whats your nme? "))

for name in sorted(names):
    print(f"hello, {name}")


		- with new imput the previous info will be lost 
to save them use open function 
file - is the name of variable you give to it
write() - is a function 

			- name = input("What is your name? ")
file = open("names.txt", "w")
file.write(name)
file.close()

				- "w" is for write

					- to check the result print in console - 

						- code names.txt

					- to remove text from file - 

						- re names.txt

				- "w" not only create file for you, it will also recreate the file for you every time you open the file in that mode 

			- name = input("What is your name? ")
file = open("names.txt", "a")
file.write(name)
file.close()

				- "a" - to add to the bottom of the document  in the same line 

					- for the new line 
file.write(f"{name}\n")

			- importance of closing file 

				- name = input("What is your name? ")
with open("names.txt", "a") as file: 
      file.write(f"{name}\n")
     #automate closing after the last line

	- by lines

		- myfile.write(name1 + '\n')

	- always close file at the end for not to lose data

		- customer_file.close()

	- strings can be written as it is into the file
numbers must be converted into the string before writing 

- read from the file

	- read all

		- infile = open('names.txt', 'r')
file_contents = infile.read()
infile.close()

			- data from the file is save in file_contents as a string

		- from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))


			- trait of the object returned by the open() function in text mode  => the object is an instance of the iterable class.

	- read by lines

		- readline()

			- returns only one line of the file as a string with \n at the end
if the last line does not have \n => readline() returns it without \n

				- line1=infile.readline()
line1=infile.readline()
line1=infile.readline()

#to read 3 lines from the file

			- returns empty string ('') when tried to read out of the file borders

				- sales_file = open('sales.txt', 'r')
line = sales_file.readline()
while line != '':
    amount = float(line)
    print(amount)
    line = sales_file.readline()

sales_file.close()

				- sales_file = open('sales.txt', 'r')
for line in sales_file: 
    amount = float(line)
    print(amount)
    

sales_file.close()

		- readlines()

			- with open("names.txt", "r") as file: 
     lines = file.readlines()  #reading all of the lines and storing them in the variable lines as a list

for line in lines: 
     print("hello,", line.rstrip()) #or use line, end="" to eliminate extra line

				- with open("names.txt", "r") as file:  
    for line in file: 
         print("hello,", line.rstrip())

			- has limit on a buffer

				- from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

	- read numbers

		- value = int(infile.readline())

		- value = float(infile.readline())

### IOError 

- try:
    # Some stream operations.
except IOError as exc:
    print(exc.errno)

	- errno.EACCES

		- Permission denied

	- errno.EBADF

		- Bad file number

	- errno.EEXIST

		- File exists

	- errno.EFBIG

		- File too large

	- errno.EISDIR

		- Is a directory

	- errno.EMFILE

		- Too many open files

	- errno.ENOENT

		- No such file or directory

	- errno.ENOSPC

		- No space left on device

- from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))

## Errors 

### Loops to prevent them

- to catch and then to ignore the error 

	- if type(value) is int: 

	- pass

		- def main():
     x = get_int()
     print(f"x is{x}")

def get_int():  
    while True:
          try: 
                return int(inpup("What's x? "))
          except ValueError: 
                pass
#to stay in the loop without instructions for user

             
main()

			- if x name not is the same in both functions - prompt

				- def main():
     x = get_int("What's x? ")
     print(f"x is{x}")

def get_int():  
    while True:
          try: 
                return int(inpup(prompt))
          except ValueError: 
                pass
#to stay in the loop without instructions for user

             
main()

- try:


except:

	- all exceptions are by except:

		- except can be assigned to a variable

			- except ValueError as err: 
     print(err)

--> invalid literal for int() with base 10

				- except Exception as err: 
     print(err)

			- try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())

	- variable inside try in Python exists for all the other part of program

	- each block try or except may contain several instructions

		- def main():
    total = 0.0
    try: 
        infile = open('sales_data.txt', 'r')
        for line in infile: 
             amount = float(line)
             total += amount 
        infile.close()
        
        print(f'{total:.2f}')

    except IOError: 
        print('Error happened trying to open file')
    except ValueError: 
        print('Non digit characters in file')
    except: 
        print('Error happened')


	- to catch 2 exceptions with the same manner 

		- try:
    :
except (exc1, exc2):
    :


- try:

except:

else:

	- while True:
    try: 
         x = int(input("What's x? "))
    except ValueError: 
         print("x is not an integer")
    else:
          break 


print(f"x is {x}")

		- def main():
     x = get_int()
     print(f"x is{x}")

def get_int():  
    while True:
          try: 
               x = int(input("What's x? "))   #other way is return int(inpup("What's x? "))
#return x  - can put here 

          except ValueError: 
               print("x is not an integer")
          else:
               return x     
 #return is stronger than break it is also breaks the loop

main()

			- else functions if the program does not fall into except

	- If exception arises => else does not execute

- try:

except:

finally:
	

	- instructions in finally always execute: even if  except raised. Its purpose to do cleaning operations: close files, ets

- exceptions in the functions 

	- If an exception is raised inside a function, it can be handled:

		- inside the function

			- def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

			-  the exception raised can cross function and module boundaries, and travel through the invocation chain looking for a matching except clause able to handle it.

		- outside the function

			- def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

### raise

- class includes all the necessary checks of the values correctness

	- class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

		- class Student:
    def __init__(self, name, house):   #gives the opportunity  to customize the class object
        self.name = name
        self.house = house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)    
    except ValueError: 
        ......
   

- to call exception 

	- return Exception - does not catch error

- raise without the name of exception can be putted inside the except

	- def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

### assert

- import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

	- assert expression

		- It evaluates the expression;

if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value different than None, it won't do anything else;

otherwise, it automatically and immediately raises an exception named AssertionError (in this case, we say that the assertion has failed)


### hierarchy of errors

- hierarchy of errors

	- ArithmeticError

		- BaseException ← Exception ← ArithmeticError

		- an abstract exception including all exceptions caused by arithmetic operations like zero division or an argument's invalid domain

	- AssertionError

		- BaseException ← Exception ← AssertionError

		- a concrete exception raised by the assert instruction when its argument evaluates to False, None, 0, or an empty string

	- BaseException

		- the following two except branches are equivalent: except: and except BaseException:.

	- IndexError

		- BaseException ← Exception ← LookupError ← IndexError

		- when you try to access a non-existent sequence's element (e.g., a list's element)

	- KeyboardInterrupt

		- BaseException ← KeyboardInterrupt

		-  a concrete exception raised when the user uses a keyboard shortcut designed to terminate a program's execution (Ctrl-C in most OSs); if handling this exception doesn't lead to program termination, the program continues its execution.

	- LookupError

		- BaseException ← Exception ← LookupError

		- an abstract exception including all exceptions caused by errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)

	- MemoryError

		- BaseException ← Exception ← MemoryError

		- a concrete exception raised when an operation cannot be completed due to a lack of free memory

	- OverflowError

		- BaseException ← Exception ← ArithmeticError ← OverflowError

		- a concrete exception raised when an operation produces a number too big to be successfully stored

	- ImportError

		- BaseException ← Exception ← StandardError ← ImportError

		- a concrete exception raised when an import operation fails

	- KeyError

		- BaseException ← Exception ← LookupError ← KeyError

		-  a concrete exception raised when you try to access a collection's non-existent element (e.g., a dictionary's element)

- def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)


- errors that do not let execute the program

	- TypeError

		- to input str for number

			- with pytest

				- import pytest

from calculator import square 

def test_positive():
      assert square(2) == 4
      assert square(3) == 9

def test_positive():
       assert square(-2) == 4

       assert square(-3) == 9


def test_zero():
      assert square(0) == 0

def test_str():
       with pytest.raises(TypeError):
              square("cat")


		- It is not allowed to use a float value as an index of a list (the same rule also applies to tuples)

	- AttributeError

		- This exception occurs, among other things, when you try to call a method that does not exist on an element you are dealing with.

	- NameError

		- local variables exist in the function otherwise are global variables 

		- ValueError occurs first then the necessity of execute the function with Value or others reasons of incorrectnes 

			- else 

	- SyntaxError

		- is raised when control reaches a line of code that violates Python syntax rules

	- MemoryError 

		- the size/ length of the string 

	- ValueError 


		- try

		- except

			- to raise exceptions 

			- raise key word 

				- raise key word to raise exceptions by yourself

		- int() or float()) receives an argument of a suitable type, but its value is unacceptable.

	- StackOverflowError

		- infinite recursion

	- RecursionError

		- recursion without cases if and else

			- memory explodes

- first most specific errors

	- ZeroDivisionError

		- try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

	- KeyError 

		- the key does not exist in the dictionary

			- try:
   au = float(distance[spacecraft])
except KeyError:
    ...
except ValueError: 
    print(f"Can't convert")
    return

				- the ... helps to handle both exceptions the same way

- default except  should be the last always

### https://docs.python.org/3.11/library/exceptions.html

- https://docs.python.org/3/library/exceptions.html

### define own exception

-  if you want to create an exception which will be utilized as a specialized case of any built-in exception, derive it from just this one. If you want to build your own hierarchy, and don't want it to be closely connected to Python's exception tree, derive it from any of the top exception classes, like Exception.

	- class MyZeroDivisionError(ZeroDivisionError):	
    pass

	- class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")


	- self.args is a tuple that stores the arguments passed to the exception when it's raised. It's used by the base Exception class to represent the error message when you print an exception.

		- class Ex(Exception): 
	def __init__(self, msg): 
		Exception.__init__(self, msg + msg)
		self.args = (msg,)
		
try: 
	raise Ex('ex')

except Exception as e: 
	print(e)
	
except Ex as e: 
	print(e)

			- self.args overwrite the msg

			- and automatically used by Python for message representation

## Debugging

### mario.py 

- breakpoints

	- to slow down the execution of the program 

		- arrow down - step by step

## Libraries

### types of libraries

- random 

	- random.choice(seq)

		- function choice exists in the module random, seq means a list

		- chooses a "random" element from the input sequence and returns it

		- sample(sequence, elements_to_select=1)

		- from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))



	- random.randint(a, b)

	- random.shuffle(x)

	- random.sample(list, k=2)

		- sampling, the items do not repeat

	- debug repititnes

		- random.seed(1)

			- sets the seed to the int_value

		- seed()

			- sets the seed to the current time

	- from random import random

		- random()

			- produces a floating point number x between the range (0.0, 1.0)

	- randrange(end)

	- randrange(start, end)

	- randrange(start, end, increment)

	- randint(left, right)

		- does not implicit exclusion of the right side

- statistics

	- average.py

- csv

	- to read files

- pillow 

	- to manipulate fotos

- API - application programming interface

	- requests library 

		- pypi.org/project/requests

	- json library 

		- to format JSON data

- python-dotenv

- tabulate

- mysql-connector-python

- math

- platform

	- allows access to underlying platform data, i.e. hardware, operating system and interpreter version information.

		- platform(aliased = False, terse = False)

		- machine()

		- processor()

		- system()

		- version()

		- python_implementation()

		- python_version_tuple()

- operational system

	- Creating directories

		- FileExistsError

			- we cannot create a directory if it already exists

		- import os

os.mkdir("my_first_directory")
print(os.listdir())

		- import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())


			- To move between directories, you can use a function called chdir, which changes the current working directory to the specified path. As an argument, it takes any relative or absolute path.

	- Deleting directories

		- os.rmdir("my_first_directory")

		- os.removedirs("my_first_directory/my_second_directory")

			- To remove a directory and its subdirectories

	- 
    my_first_directory — this is a relative path which will create the my_first_directory directory in the current working directory;
    ./my_first_directory — this is a relative path that explicitly points to the current working directory. It has the same effect as the path above;
    ../my_first_directory — this is a relative path that will create the my_first_directory directory in the parent directory of the current working directory;
    /python/my_first_directory — this is the absolute path that will create the my_first_directory directory, which in turn is in the python directory in the root directory.


- date-time

	- from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

		- create a date object

			- from datetime import date

my_date = date(2019, 11, 4)
print(my_date)


	- creating a date from timestamp

		- from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)


#Timestamp: 1758894231.5100257
#Date: 2025-09-26


		- In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC)

	- year-month-day format

		- from datetime import date

d = date.fromisoformat('2019-11-04')
print(d)

	- changing date

		- from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

d = d.replace(month=5)
print(d)

	- day of the week

		- from datetime import date

d = date(2019, 11, 4)
print(d.weekday())  #0 is Monday and 6 is Sunday
print(d.isoweekday()) #1 is Monday, and 7 is Sunday

	- time

		- from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)   #0-23
print("Hour:", t.hour) #0-59
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


		- import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)   #takes integer or a float

		- import time

timestamp = 1572879180
print(time.ctime(timestamp))

#Mon Nov  4 14:53:00 2019


		- time.struct_time:
    tm_year   # specifies the year
    tm_mon    # specifies the month (value from 1 to 12)
    tm_mday   # specifies the day of the month (value from 1 to 31)
    tm_hour   # specifies the hour (value from 0 to 23)
    tm_min    # specifies the minute (value from 0 to 59)
    tm_sec    # specifies the second (value from 0 to 61 )
    tm_wday   # specifies the weekday (value from 0 to 6)
    tm_yday   # specifies the year day (value from 1 to 366)
    tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
    tm_zone   # specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # specifies the offset east of UTC (value in seconds)


			- import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))


			- import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))


#Mon Nov  4 14:53:00 2019

#1572879180.0


				- 2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst

		- import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

#2019/11/04 14:53:00
#2025/09/26 15:00:42


			- If you don't pass a tuple or struct_time object, the formatting will be done using the current local time.

	- date and time

		- from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())

			- datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

		- The datetime class has several methods that return the current date and time. These methods are:

    today() — returns the current local date and time with the tzinfo attribute set to None;
    now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it. The argument of this method must be an object of the tzinfo subclass;
    utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.


		- from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

#2020/01/04


			-  the separator character / can be replaced by another character, or even by a string

		- from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%Y/%b/%d %H:%M:%S"))

#14:53:00
#2020/Nov/04 14:53:00

#Y for full version
#y for short version


		- from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

#2019-11-04 14:53:00

			- import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

#time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)

	- timestamp

		- The timestamp method returns a float value expressing the number of seconds elapsed between the date and time indicated by the datetime object and January 1, 1970, 00:00:00 (UTC).

		- from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())


	- date and time operations

		- from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

		- timedelta objects

			- from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

			- from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)



			- from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)


- calendar

	- Day of the week 	Int   	Constant
Monday 	                0 	calendar.MONDAY
Tuesday 	                1 	calendar.TUESDAY
Wednesday 	        2 	calendar.WEDNESDAY
Thursday 	        3 	calendar.THURSDAY
Friday 	                4 	calendar.FRIDAY
Saturday            	5 	calendar.SATURDAY
Sunday            	6 	calendar.SUNDAY

		- change first day

			- import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)

	- display the calendar for the whole year

		- import calendar
print(calendar.calendar(2020))

		- print(calendar.calendar(2020, w=5))

			- w – date column width (default 2)
l – number of lines per week (default 1)
c – number of spaces between month columns (default 6)
m – number of columns (default 3)

			- requires to specify the year, while the other parameters responsible for formatting are optional

		- import calendar
calendar.prcal(2020, w=5)

			- prints by itself

	- for the month

	- import calendar
print(calendar.weekday(2020, 12, 24))

		- days 0-6

	- import calendar
print(calendar.weekheader(2))

#Mo Tu We Th Fr Sa Su


		- import calendar
calendar.setfirstweekday(calendar.SUNDAY)
calendar.weekheader(2)
calendar.prmonth(2020, 12)

	- import calendar
print(calendar.month(2025, 10))
calendar.prmonth(2025,9)

		- 
    w – date column width (default 2)
    l – number of lines per week (default 1)


	- import calendar

print(calendar.isleap(2024))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.

	- classes

		- 
    calendar.Calendar – provides methods to prepare calendar data for formatting;
    calendar.TextCalendar – is used to create regular text calendars;
    calendar.HTMLCalendar – is used to create HTML calendars;
    calendar.LocalTextCalendar – is a subclass of the calendar.TextCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.
    calendar.LocalHTMLCalendar – is a subclass of the calendar.HTMLCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.


			- import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")


				- The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday).

### modules/ librerias  - part of code with one or several functions

- create library

	- const

		- all letters must be UPPERCASE

			- does not change

	- variable

		- starts with lowercase letter

			- can be changed

	- Class

		- Object

	- in 2 different folders

		- /progs

			- main.py

				- from sys import path

path.append('..\\modules')

import module


		- /modules

			- module.py

				- #!/usr/bin/env python3 

""" module.py - an example of a Python module """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)



		- variable  path

			- import sys

for p in sys.path:
    print(p)

	- in 1 folder 

		- /folder

			- /folder/module.py

			- /folder/main.py

			- subfolder

__pycache__

	- packages

		- create a file in the folder to start package

			- __init.py__

		- folder /packages with folders for modules files

		- main.py

			- from sys import path
path.append('..\\packages')

import extra.iota
print(extra.iota.funI())



			- from sys import path

path.append('..\\packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())



		- packages

			- navigation in the folders

				- extra.ugly.psi.funP()

				- extra.good.best.tau.funT()

			- initialization 

				- Python expects a file with a very unique name inside the package folder: __init__.py.

					- __init__.py can be empty

					- only one - in the main folder "extra"

				- __init.py__, you can also place it inside any of its subfolders (subpackages). This can be useful if some of the subpackages require individual handling or a special type of initialization.

					- for example in FLASK

					- for example: connections with DATABASE URI

			- sys

				- import sys 

print("hello, my name is", sys.argv[1])

					- to print in the command line: python name.py Kate  - it works with the arguments from the command line 

						- IndexError - try to use any element that does not exist in with the [index]

							- name.py

								- import sys 


if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is ", sys.argv[1])

									- multiple else is not possible

								- to do the modules in the programing code 

									- import sys 

# 1 module
#Check for errors 

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# 2 module
#Print name tags 
print("hello, my name is ", sys.argv[1])

								- for loop

									- import sys 

#to make distincts blocks of code 
#Check for errors 

if len(sys.argv) < 2:
    sys.exit("Too few arguments")


#Print name tags 
for arg in sys.argv:
     print("hello, my name is ", arg)

										- Error: prints all the names from the list 

											- slices  - to take a subset of the list 

												- for arg in sys.argv[1:]:

												- for arg in sys.argv[1:-1]:

													- negative number exclude the last one from the print 

					- command-line arguments

				- package compressed 

					- from sys import path

path.append('..\\packages\\extrapack.zip')

				- pacakge in the folder

					- from sys import path
path.append('..\\packages')


				- If you want to convince Python to take into account the directory of a non-standard package, its name must be inserted/added to/in the list of import directories stored in the path variable contained in the sys module.

				- import sys

if __name__ == "__main__":
    print "Dont do this!"
    sys.exit()

- import library

	- namespace problem

		- all names defined in the module are made known, but they do not enter the code namespace.

			- math.pi
math.sin


				- This is mandatory if a module has been imported with the import statement. It doesn't matter whether any of the module's code and namespace names conflict.

				- This means that you can have your own entities named sin or pi and they won't be affected by the import in any way.

	- pieces of code to be used

		- key word - import - to import module

			- import random 

coin = random.choice(["heads", "tails"])
print(coin)

		- key word - from - to do the import more scpecific 

			- from random import choice 

coin = choice(["heads", "tails"])
print(coin)

				-  namespace problem

the danger of causing conflicts with names derived from importing the code's namespace. 

					- Imported entity names can be accessed within code without specifying the source module name.

						- cant be used print(math.e) for imported variable

					- No other entities are imported, only those specified.

			- from library_name import *

				- imports all entities from the indicated module.

					- Namespace problem

						- Is it unsafe

			- as

				- from module import name as alias

					- from math import pi as pi_m, cos as cos_m

						- to change the name of imported variables or functions of module. 

				- import math as m

				- after successful execution of an aliased import, the original module name becomes inaccessible and must not be used.

		- import module as alias

			- can give a library another name: this is called aliasing or renaming.


	- dir()

		- The function returns an alphabetically sorted list containing all the names of the entities available in the module.

		- dir(module)

	- https://pypi.org/

		- 3d party libraries

		- pip - package manager program

			- commands in cmd

				- pip help

					- pip help install

				- pip --version

				- pip search

				- pip list

		- dependencies between packages

			- The connections between the packages are crucial, and if someone decides to use your code (but remember, we already claimed it first) you'll also need to make sure all the required packages are in place.

			- pip check 

			- pip show package_name

				- Requires: packages that this package needs
Required-by: packages that need the package virtualenv


		- install pip

			- apt install python3-pip

				- each pip for different installations/ versions of python 

			- install as a user

				- pip install --user

					- path only for a particular user

			- install as an administrator

				- pip install

					- global path for all users

## Unit Tests

### test_calculator.py

- from calculator import square 

def main(): 
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9: 
        print("3 squared was not 9")


if __name__ == "__main__":
    main()


### key word

- assert

	- AssertionError

		- from calculator import square 

def main(): 
    test_square()

def test_square():
    try: 
         assert square(2) == 4
    except AssertionError:
          print("2 squared was not 4")

     try: 
         assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()

### pytest - 3d party program

- from calculator import square 

def test_square():
      assert square(2) == 4
      assert square(-2) == 4
      assert square(3) == 9
      assert square(-3) == 9
      assert square(0) == 4


	- better practice - test functions

		- from calculator import square 

def test_positive():
      assert square(2) == 4
      assert square(3) == 9

def test_positive():
       assert square(-2) == 4

       assert square(-3) == 9


def test_zero():
      assert square(0) == 0


			- name of the testing function always begins with test_

- pip install pytest

	- docs.pytest.org

		- pytest file.py

			- keep tests in different files and run a folder for test

				- within directory with test files - create a file named __init__.py - this file even empty tells the python to treat that folder as a package

- for programs that do not return value but have side affects like print("hello, ", name) - pytest does not applicable - only mnual tests

the program better change for automation testing 

	- def main(): 
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
     return f"hello, {to}"

if __name__ == "__main__":
    main()

		- from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

			- from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():

    for name in ["Hermione", "Harry", "Ron"]:
         assert hello("David") == f"hello, {name}"

- Type Error

	- if not isinstance(au, (int, float)):
    raise TypeError("au must be int or float")
return au * 18279798302

		- in pytest

			- def test_error():
    with pytest.raises(TypeError):
         convert("1")

## Functions

### definition of a function 

- definition of function in the first lines 

- parameters and arguments

	- def message():                          #function parameter - you cant pass any  argument 
    print("Ingresa un valor: ")
    a = input()
    return a 

b = message()                          #function argument
print(b)


	- def f(n):              #solo 1 parameter 
    print = n*2 

f(3)                   #result is 6, argument is 3

	- def message(what, number):
    print("Ingresa", what, "número", number)

#2 parameters

	- passing positional parameters

		- position is important

			- def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

#function uses parameters in their order of introduction

		- position is not important 

			- def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


		- Positional arguments should be placed first, followed by keyword arguments

			- adding(3, a = 1, b = 2)

			- TypeError: adding() got multiple values for argument 'a'

		-  predefined parameters/ values

			- def introduction(first_name, last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

			- can pass other last_name or no pass nothing for the last_name

			- predefined parameters should be always at the end

	- arguments can be every data type like lists and so on 

		- function can be an argument in the other function 

	- a variable that exists outside a function has scope within the body of the function - only in Python 

		- The variable var created inside the function is not the same as the one defined outside of it, it seems that there are two different variables with the same name.

The variable in the function is a shadow of the variable outside the function.

			- def my_function():
    var = 2
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)

				- ¿Conozco a aquella variable? 2
1

		- exeptions

			- global

				- extend the scope of a variable by including the body of functions in order to be able to not only read the values ​​of the variables but also modify them

				- forces Python to refrain from creating a new variable inside the function; it will use the one that can be accessed from outside

					- def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)


						- ¿Conozco a aquella variable? 2
2

				- balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()



					- to use class instead of a global variable

						- class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()



			- lists

				- list will be modificated inside the function for all the program, not only for one case of function usage

					- not to change the list inside the function - pass copy of the list  function(my_list[:])

			- pip install mypy

				- def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)



				- typehints

					- https://docs.python.org/3/library/typing.html

- instructions

	- to get results - values

		- return

			- with expression 

			- without expression 

				- returns None

				- functions like break in while

		- without return returns None 

			- def strange_function(n):
    if(n % 2 == 0):
        return True

				- for numbers odd returns None

	- to pass 

		- pass

			- to not to give error if function does not have any instruction

			- Indentation Error expected an indented block

if pass was not used for the empty function 

def liters_100km_to_miles_gallon(liters):

### integrated functions

- list()

	- print(list(range(10)))

- range()

	- for numbers / the developer put the number of lists items

		- range(3)

- def()

	- to make a new function 

- len()

	- the program counts how long is the list 

		- for i in range(len(students)):

- print()

	- print()

		- print without an argument opens the new line like Enter do

	- not to open new line 

		- end=' '

	- to change the separator from the space to smth else 

		- sep=''

	- f string

		- print(f"Prints {variable}") 

			- to format variable inside the Fstring

				- print(f"{variable:>20,.2f}")

					- should be put after : in the order [alignment] [width] [,] [.precision] [type]

					- aligment 
< on the left
> on the right
^ in the center

### preinstalled modules in libraries

### lambda

## DATA BASES

### import sqlite3

- import mysql.connector
import os

	- os: Lets Python access environment variables.

	- mysql.connector: Library to interact with MySQL databases.

- from dotenv import load_dotenv     


load_dotenv()     #descargar .env  para usar variables de intornos desde fichero .env 




	- Subtopprogram reads user and password from environment

	- load_dotenv() (from dotenv): Loads variables from a .env file into the environment.

		- This reads variables like MYSQL_USER and MYSQL_PASSWORD from a .env file and makes them accessible with os.getenv().

### connection with DB

- my_con = sqlite3.connect('art_color_picker_BD_1')

	- set a connection with existing DB

	- if file doesn't exist: function will create it

	- sqlite3.connect(r'C:\Users\......\DBname.db')

- def conectar(ususario, passwd): 
    try: 
        mi_conex = mysql.connector.connect(
            host = 'localhost',
            user = ususario,
            password = passwd)
    
        if mi_conex.is_connected(): 
            print("Conexión establecida de forma correcta")

        
    except Exception as e: 
        mi_conex = None
        print("Error de conexion")
        print(e)

    
    return mi_conex

### CREATE DB

- def crearBD(conex):
    nombre = input("Introduce el nombre de la base de datos: ")
    sql = 'CREATE DATABASE %s'
    cursor = conex.cursor()
    cursor.execute(sql % (nombre,))
    cursor.close()

### queries to DB

- def consultas(mi_conex): 
    mi_cursor = mi_conex.cursor()
    mi_cursor.execute('SHOW DATABASES;')

    for bd in mi_cursor:    #muestra tupla
        for i in bd:        #printea elemento de tupla
            print(i, '\n*******')


    mi_cursor.execute("SELECT user, host, plugin FROM mysql.user")
    for query in mi_cursor: 
        print(query, '\n******')


### disconnect

- def desconectar(mi_conex): 
    
    if mi_conex:       #check that mi_conex not None
        mi_conex.close()

    if not mi_conex.is_connected(): 
        print("Conexion finalizada de forma correcta.")

### main()

- print(os.getenv('python_mysql'))
    print(os.getenv('python_mysql_password'))
    u = os.getenv('python_mysql')
    p = os.getenv('python_mysql_password')


    
    
    mi_conexion = conectar(u, p)
    if mi_conexion: 
        consultas(mi_conexion)
        desconectar(mi_conexion)


### to safe passwords secretly

- import getpass  #  para camuflar input in consola

	- def main(): 
    
    
    u = input("Dime nombre de ususario: ")
    p = getpass.getpass(prompt='Password: ')   #se contiene input
    ##password = input("Password: ")

    mi_conexion = conectar(u, p)
    if mi_conexion: 
        consultas(mi_conexion)
        desconectar(mi_conexion)

### my_pointer = my_con.cursor()

- to iterate with DB

### query = 'CREATE TABLE colors( rgb INTEGER UNSIGNED NOT NULL PRIMARY KEY, name VARCHAR(100) NOT NULL, cmyk TEXT)'

### my_pointer.execute(query)

- .executemany

### my_con.commit()

- Always necessary if changes to DB have been made

### colors = [(0xFBE6A0, "Naples Yellow", "{'C':2, 'M':7, 'Y':44, 'K':0}" ), 
          (0xF15A30, "Peach Red", "{'C':0, 'M':80, 'Y':90, 'K':0}"),
          (0x112F2C, "Deep Slate Green", "{'C':80, 'M':50, 'Y':60, 'K':70}", ), 
          (0xE2B540, "Yellow Ocher", "{'C':12, 'M':28, 'Y':88, 'K':0}" ) ]     

query = "INSERT INTO colors VALUES(?, ?, ?, NULL)" 
my_pointer.executemany(query, colors)
my_con.commit()

- always use TUPLE to pass a value to the column 

	- try: 
    palletes = [(14,),(115,),(166,),(325,)]
    query = 'INSERT INTO palletes VALUES(?)'
    my_pointer.executemany(query, palletes)
    my_con.commit()
    print("Palleta añadida")

except sqlite3.IntegrityError:
    print("Clave duplicada")   

### my_con.close()

- At the end always close the connection

### SQL injections

- dont pass f strings

	- f'VALUES ({name})'

- dont use concatenation

	- 'INSERT INTO column (name, name2)' + 'VALUES ("' + name + '", ' + str(price) + ')'

- to prevent them use pseudocode

	- cur.execute("SELECT Description, RealPrice FROM Products WHERE RealPrice >= ?", (min_price,))

### data types

- SQL

NULL

INTEGER

REAL

TEXT

BLOB

	- PYTHON

None

int

float

str

can be any object

- for PRIMARY KEY add NOT NULL



