# Flask-like routing with metaclass registration
class RouteMeta(type):
    _routes = {}
    
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        
        # Register routes from class methods
        for attr_name, attr_value in attrs.items():
            if hasattr(attr_value, '_route'):
                route_path, methods = attr_value._route
                cls._routes[route_path] = {
                    'handler': attr_value,
                    'methods': methods,
                    'class': new_class
                }
        
        return new_class

def route(path, methods=None):
    """Decorator to mark methods as route handlers"""
    if methods is None:
        methods = ['GET']
    
    def decorator(method):
        method._route = (path, methods)
        return method
    return decorator

class Controller(metaclass=RouteMeta):
    pass

class UserController(Controller):
    @route('/users', methods=['GET'])
    def list_users(self):
        return {'users': []}
    
    @route('/users/<int:user_id>', methods=['GET'])
    def get_user(self, user_id):
        return {'user_id': user_id}

# Routes automatically registered!
print(RouteMeta._routes)