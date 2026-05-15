# Instead of metaclass for simple cases:
class Base:
    # Use __init_subclass__ for subclass registration
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Subclass created: {cls.__name__}")
    
    # Use class decorators for method transformation
    @classmethod
    def register(cls, name):
        def decorator(subclass):
            cls.registry[name] = subclass
            return subclass
        return decorator
    
    # Use descriptors for attribute control
    class ValidatedAttribute:
        def __set_name__(self, owner, name):
            self.name = name
        
        def __set__(self, instance, value):
            # Validation logic here
            instance.__dict__[self.name] = value

# Use dataclasses for boilerplate reduction
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    color: str = "black"