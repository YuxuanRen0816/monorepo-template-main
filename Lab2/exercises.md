# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Answer: Then name of function is cruicial because it makes code more readable and user-friendly. For the "pop" function, in the dictionary and list they all have this method, and all remove last element and return it's value.
Like the function in dictionary class which names get(), when the key does not exit in the dictionary, it will return the default value. But in some language, can define the name as getOrDefault(), which is different with get() function.


2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

Lists are ordered collections of items where you access elements by their position.
Dictionaries are collections of key-value pairs where you access values using keys. They utilize hashing for efficient key lookups.
The choice between a list and a dictionary typically depends on the specific needs of your application. If you need fast lookups by a key, use a dictionary. If you need an ordered collection of items, use a list.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, a list in Python allows for random access, which means you can access any element directly using its index in constant time O(1). Random access is a feature of arrays (or dynamic arrays, in the case of Python's list implementation) where each element has a unique memory address calculated using the base address of the array and the size of each element. This enables direct access to any element based on its index.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

Answer:  Generic libraries and data structures offer a lot of flexibility and can reduce the amount of code you need to write, they also come with trade-offs in terms of performance, type safety, and predictability. The choice between a generic system and a type-specific one should be based on the specific requirements and constraints of a given project.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Answer: The requests library's function and method names are aptly chosen, mirroring the HTTP methods they represent. This makes the library intuitive for developers familiar with HTTP verbs. The method signatures, with parameters like url, data, params, and json, also provide a clear idea about the expected inputs, making the library user-friendly and easy to understand.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

The main class in the requests library that most users interact with is the requests.Request class, which represents a prepared request for sending. The associated requests.Session class is responsible for actually sending the prepared request and returning a requests.Response object.
One of the potential functions of interest regarding your question might be the request method in the Session class, which allows for creating and sending a request. The request method indeed has many parameters (more than 5). This is because it's designed to be a flexible, catch-all method that can handle any kind of HTTP request. The many parameters provide fine-grained control over the request.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

**kwargs is a convention in Python that stands for "keyword arguments". It allows you to pass a variable number of keyword (or named) arguments to a function. Inside the function, kwargs is treated as a dictionary where the keys are the argument names and the values are the corresponding passed values.
Because: Flexibility, Extensibility, Dynamic building

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

In Python, function or method arguments can be set with default values, which are specified by the assignment operation (=) in the function signature. These default values are used when the caller doesn't provide a value for that argument. This allows for optional arguments.
None is a commonly used default value in Python. It represents the absence of a value. Using None allows the function to differentiate between "no value provided" and other potential default values like 0, False, or an empty string.
Default values can be any valid Python expression, including:
Basic data types: int, str, float, bool
Data structures: list, dict, set, etc. 
Providing default values makes the function easier to use. Callers can skip optional arguments if they're fine with the default behavior.


