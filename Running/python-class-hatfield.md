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

- With the `@property` we are able to return dynamic information without having to change the attribut











---
## Metadata
- `tags`: #class #python
- `Title`: python-class
- `Created`: [[20210128]] 09:37

==References==
- []()