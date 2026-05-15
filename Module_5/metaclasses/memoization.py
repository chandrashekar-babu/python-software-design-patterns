class CacheMeta(type):
    """Metaclass that automatically adds caching to expensive methods"""
    
    def __new__(cls, name, bases, attrs):
        # Process methods with @cached decorator
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and hasattr(attr_value, '_cached'):
                # Replace method with cached version
                attrs[attr_name] = cls._create_cached_method(attr_value)
        
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def _create_cached_method(method):
        """Wrap method with caching logic"""
        cache_attr = f"_{method.__name__}_cache"
        
        def cached_method(self, *args, **kwargs):
            # Create cache if it doesn't exist
            if not hasattr(self, cache_attr):
                setattr(self, cache_attr, {})
            
            # Create cache key from arguments
            cache_key = (args, tuple(sorted(kwargs.items())))
            
            # Check cache
            cache = getattr(self, cache_attr)
            if cache_key in cache:
                return cache[cache_key]
            
            # Compute and cache
            result = method(self, *args, **kwargs)
            cache[cache_key] = result
            return result
        
        # Preserve original method name and docstring
        cached_method.__name__ = method.__name__
        cached_method.__doc__ = method.__doc__
        
        return cached_method

def cached(func):
    """Decorator to mark methods for caching"""
    func._cached = True
    return func

class DataProcessor(metaclass=CacheMeta):
    @cached
    def expensive_calculation(self, x, y):
        """This result will be cached"""
        print(f"Computing expensive calculation for {x}, {y}")
        import time
        time.sleep(1)  # Simulate expensive operation
        return x * y + x ** 2
    
    @cached
    def complex_operation(self, items, multiplier=1):
        """Another cached operation"""
        print(f"Computing complex operation for {len(items)} items")
        import time
        time.sleep(0.5)
        return sum(items) * multiplier

# Usage
processor = DataProcessor()

# First call - computes
result1 = processor.expensive_calculation(5, 3)  # Prints: Computing...
# Second call with same args - uses cache
result2 = processor.expensive_calculation(5, 3)  # No print - cached!

# Different args - computes again
result3 = processor.expensive_calculation(5, 4)  # Prints: Computing...

print(result1 == result2)  # True