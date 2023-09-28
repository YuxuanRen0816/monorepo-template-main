# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- *The MObject class in the given code is a concrete class. In this case, MObject doesn’t have any abstract methods (it doesn’t have any methods at all), and it doesn’t use the ABC module. It also does not contain any implementation.*
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *The __del__ method in Python is a special method, also known as a dunder method because of its double underscores. It is called the destructor method and is analogous to the constructor method __init__, but it is called when an object is about to be destroyed (garbage collected).*
1. What class does Texture inherit from?
	- *The Texture class inherits from the Image class. This is indicated by the class definition class Texture(Image): pass. The pass statement is used as a placeholder.*
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- *The Texture class inherits all the methods and attributes from the Image class, as it does not override or add any. Here are the methods and attributes that Texture inherits from Image
	* Attributes:m_width, m_height, m_colorChannels and m_Pixels
	* Methods: __init__, getWidth, getHeight, getPixelColorR, getPixels and setPixelsToRandomValue
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- *The decision between using a "has-a" (composition) relationship or an "is-a" (inheritance) relationship depends on the specific use case, requirements, and the nature of the relationship between Texture and Image.
	* I prefer Composition ("has-a" relationship), Texture is not conceptually a type of Image, but instead contains or utilizes an Image. In my experience, textures and images are seen as distinct entities that interact with each other, with textures utilizing images to achieve their functionalities, then composition might be more appropriate.
	* At this condition, the code should change I change in oop.py.

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- *Yes, in Python, even we do not provide a constructor (the __init__ method) for a class, Python will automatically create a default constructor. The default constructor does not take any parameters apart from self, which represents the instance being created, and it does not perform any actions.*

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
- Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

* Singletons in Python are not inherently thread-safe. When multiple threads are involved, there's a possibility that two or more threads might create separate instances of the singleton class before any one of them gets a chance to set the instance variable, thereby violating the singleton pattern.

* This is because the process of creating an instance involves multiple steps:

	1. Checking whether the instance already exists.
	2. If not, creating a new instance.
	3. Assigning the newly created instance to the class variable.
* If context-switching between threads occurs between step 1 and step 3, multiple instances might be created, which breaks the singleton property. This scenario is known as a "race condition."

* To make the singleton pattern thread-safe in Python, we can use threading locks or other synchronization mechanisms.

  
