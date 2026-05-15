# Without metaclass - verbose and repetitive
from pydantic import ValidationError

class TextField:
    def __init__(self, required=False, max_length=None):
        self.required = required
        self.max_length = max_length
    
    def validate(self, value):
        if self.required and value is None:
            raise ValidationError("This field is required.")
        if self.max_length and value and len(value) > self.max_length:
            raise ValidationError(f"Max length is {self.max_length}.")

class EmailField:
    def __init__(self, required=False):
        self.required = required
    
    def validate(self, value):
        if self.required and value is None:
            raise ValidationError("This field is required.")
        if value and "@" not in value:
            raise ValidationError("Invalid email address.")

class IntegerField:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def validate(self, value):
        if value is None:
            return
        if not isinstance(value, int):
            raise ValidationError("Value must be an integer.")
        if self.min_value is not None and value < self.min_value:
            raise ValidationError(f"Value must be at least {self.min_value}.")
        if self.max_value is not None and value > self.max_value:
            raise ValidationError(f"Value must be at most {self.max_value}.") 

class UserForm:
    def __init__(self):
        self.fields = {
            'name': TextField(required=True, max_length=100),
            'email': EmailField(required=True),
            'age': IntegerField(min_value=0, max_value=150)
        }
    
    def validate(self, data):
        errors = {}
        for field_name, field in self.fields.items():
            try:
                field.validate(data.get(field_name))
            except ValidationError as e:
                errors[field_name] = str(e)
        return errors

# With metaclass - clean and declarative
class Field:
    """Base field class"""
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def validate(self, value):
        pass

class TextField(Field): pass
class EmailField(Field): pass
class IntegerField(Field): pass

class ModelMeta(type):
    """Metaclass that collects field declarations"""
    def __new__(cls, name, bases, attrs):
        # Collect all Field instances
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
                attrs.pop(key)  # Remove from class attributes
        
        # Add fields to class
        attrs['_fields'] = fields
        
        # Create class
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

class Model(metaclass=ModelMeta):
    """Base class using our metaclass"""
    def __init__(self, **kwargs):
        for field_name, field in self._fields.items():
            value = kwargs.get(field_name)
            setattr(self, field_name, value)
    
    def validate(self):
        errors = {}
        for field_name, field in self._fields.items():
            try:
                field.validate(getattr(self, field_name))
            except ValidationError as e:
                errors[field_name] = str(e)
        return errors

# Usage - Beautiful, declarative syntax!
class UserForm(Model):
    name = TextField(required=True, max_length=100)
    email = EmailField(required=True)
    age = IntegerField(min_value=0, max_value=150)

# Create instance
user = UserForm(name="Alice", email="alice@example.com", age=30)
errors = user.validate()

# Django, SQLAlchemy, and many frameworks use exactly this pattern!