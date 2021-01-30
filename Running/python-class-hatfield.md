# python-class
- You can turn off garbage collection with a context manager
- `@properties` - with properties you can make a method be a property of say the `__str__` dunder

```python
class Person:
	def __init__(self, **kwargs):
		self.first_name = kwargs['first_name']	
		self.last_name = kwags['last_name']
		self.full_name = f'{kwargs["first_name"]} {kwargs["last_name"]}'
		self.age = kwargs["age"]
		
	def __str__(self):
		return f'{self.first_name} {self.last_name}'
	
	@property
	def full_name(self):
		"""This call will be dynamic even if you changed the last name"""
		return f'{self.first_name} {self.last_name}'
```

- With the `@property` we are able to return dynamic information without having to change the attributes directly. 
- You want to use private variables in classes with a `@property`
- You can also write functions like a setter in `@property` like `@property.setter` to set anything like `person.full_name = "Joe Smith"`
- You want to use `@property` whenever you are just returning a static values or any `attributes` you do not want to call a full`method` just to return some values 

- `@classmethod` with class methods you can create another object of itself using the same class it is called from like 
```python
	@classmethod
	def from_path(file_name):
		with open(file_name) as infile:
			return cls(**json.load(infile))
			
with Person.from_path('test') as you:
	print(you)
```



### Web Stuff
 - `csrf` token is generated when you first get to a site and it tells the form that is submitted that it really came from a specific user. So you need to submit the token if you want to communicate with the web server such as a login. 










---
## Metadata
- `tags`: #class #python
- `Title`: python-class
- `Created`: [[20210128]] 09:37

==References==
- []()