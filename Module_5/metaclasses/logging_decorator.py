import logging
from functools import wraps

class LoggedMeta(type):
    """Metaclass that adds logging to all public methods"""
    
    def __new__(cls, name, bases, attrs):
        # Configure logger for this class
        logger_name = f"{__name__}.{name}"
        attrs['_logger'] = logging.getLogger(logger_name)
        
        # Wrap all public methods with logging
        for attr_name, attr_value in attrs.items():
            if (callable(attr_value) and 
                not attr_name.startswith('_') and
                attr_name != 'logger'):
                attrs[attr_name] = cls._add_logging(attr_value, attr_name)
        
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def _add_logging(method, method_name):
        """Wrap method with logging"""
        @wraps(method)
        def logged_method(self, *args, **kwargs):
            self._logger.debug(f"Entering {method_name} with args={args}, kwargs={kwargs}")
            try:
                result = method(self, *args, **kwargs)
                self._logger.debug(f"Exiting {method_name}, returned {result}")
                return result
            except Exception as e:
                self._logger.error(f"Error in {method_name}: {e}", exc_info=True)
                raise
        
        return logged_method

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

class DataService(metaclass=LoggedMeta):
    def process_data(self, data):
        """Process data with automatic logging"""
        return [item.upper() for item in data]
    
    def validate(self, item):
        """Validate item with automatic logging"""
        if not item:
            raise ValueError("Item cannot be empty")
        return True

# Usage - all methods automatically logged!
service = DataService()
service.process_data(['a', 'b', 'c'])
service.validate('test')