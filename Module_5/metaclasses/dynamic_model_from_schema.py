class ModelFromJSONMeta(type):
    """Create model classes from JSON Schema"""
    
    def __new__(cls, name, bases, attrs):
        if 'json_schema' in attrs:
            schema = attrs.pop('json_schema')
            cls._create_from_schema(attrs, schema, name)
        
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def _create_from_schema(attrs, schema, class_name):
        """Create attributes from JSON schema"""
        if 'properties' in schema:
            for prop_name, prop_schema in schema['properties'].items():
                # Create property with getter/setter
                def create_property(p_name=prop_name, p_schema=prop_schema):
                    storage_name = f"_{p_name}"
                    
                    def getter(self):
                        return getattr(self, storage_name, p_schema.get('default'))
                    
                    def setter(self, value):
                        # Type validation
                        expected_type = p_schema.get('type')
                        if expected_type == 'string' and not isinstance(value, str):
                            raise TypeError(f"{p_name} must be a string")
                        elif expected_type == 'integer' and not isinstance(value, int):
                            raise TypeError(f"{p_name} must be an integer")
                        # Add more type checks...
                        
                        setattr(self, storage_name, value)
                    
                    return property(getter, setter)
                
                attrs[prop_name] = create_property()
        
        # Add validation method
        def validate(self):
            errors = []
            for prop_name, prop_schema in schema.get('properties', {}).items():
                value = getattr(self, prop_name)
                if prop_schema.get('required', False) and value is None:
                    errors.append(f"{prop_name} is required")
            return errors
        
        attrs['validate'] = validate

# JSON Schema definition
user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "required": True},
        "email": {"type": "string", "required": True},
        "age": {"type": "integer", "default": 0}
    }
}

class User(metaclass=ModelFromJSONMeta):
    json_schema = user_schema
    
    def __init__(self, **kwargs):
        for key in user_schema['properties']:
            setattr(self, f"_{key}", kwargs.get(key))

# Usage - properties created from schema!
user = User(name="Alice", email="alice@example.com")
print(user.name)  # Alice
print(user.age)   # 0 (default)

user.age = 30
# user.age = "thirty"  # Would raise: TypeError: age must be an integer

errors = user.validate()
print(errors)  # []