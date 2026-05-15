class BorgMeta(type):
    """Metaclass for Borg pattern (shared state, not same instance)"""
    
    def __new__(cls, name, bases, attrs):
        # Add _shared_state to class
        attrs['_shared_state'] = {}
        
        # Modify __init__ to use shared state
        original_init = attrs.get('__init__')
        
        def new_init(self, *args, **kwargs):
            self.__dict__ = self._shared_state
            if original_init:
                original_init(self, *args, **kwargs)
        
        attrs['__init__'] = new_init
        
        return super().__new__(cls, name, bases, attrs)

class SharedConfig(metaclass=BorgMeta):
    def __init__(self):
        # This will only run once per attribute access pattern
        if not hasattr(self, 'initialized'):
            self.settings = {}
            self.initialized = True
    
    def set(self, key, value):
        self.settings[key] = value

# Different instances but shared state
config1 = SharedConfig()
config2 = SharedConfig()

config1.set('timeout', 30)
print(config2.settings['timeout'])  # 30 - shared state!

print(config1 is config2)  # False - different instances
print(config1.__dict__ is config2.__dict__)  # True - same __dict__