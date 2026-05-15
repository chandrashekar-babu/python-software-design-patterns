import json

class APIClientMeta(type):
    """Metaclass that creates API methods from OpenAPI specification"""
    
    def __new__(cls, name, bases, attrs):
        # Check if we have an OpenAPI spec
        if 'openapi_spec' in attrs:
            spec = attrs.pop('openapi_spec')
            cls._create_api_methods(attrs, spec)
        
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def _create_api_methods(attrs, spec):
        """Create methods for each API endpoint"""
        for path, methods in spec['paths'].items():
            for http_method, details in methods.items():
                method_name = details.get('operationId', 
                                         f"{http_method}_{path.replace('/', '_').strip('_')}")
                
                # Create the API method
                def create_api_method(path=path, http_method=http_method, details=details):
                    def api_method(self, **kwargs):
                        # This would make the actual HTTP request
                        url = f"{self.base_url}{path}"
                        print(f"Making {http_method.upper()} request to {url}")
                        print(f"Parameters: {kwargs}")
                        print(f"Expected responses: {details.get('responses', {})}")
                        # In real implementation: requests.request(http_method, url, **kwargs)
                        return {"status": "mock_response", "url": url}
                    
                    # Add docstring from OpenAPI spec
                    api_method.__doc__ = details.get('description', 'API endpoint')
                    api_method.__name__ = method_name
                    
                    return api_method
                
                # Add method to class
                attrs[method_name] = create_api_method()

# Example OpenAPI spec
openapi_spec = {
    "openapi": "3.0.0",
    "paths": {
        "/users": {
            "get": {
                "operationId": "list_users",
                "description": "Get list of users",
                "responses": {"200": {"description": "List of users"}}
            },
            "post": {
                "operationId": "create_user",
                "description": "Create a new user",
                "responses": {"201": {"description": "User created"}}
            }
        },
        "/users/{user_id}": {
            "get": {
                "operationId": "get_user",
                "description": "Get user by ID",
                "responses": {"200": {"description": "User details"}}
            }
        }
    }
}

class APIClient(metaclass=APIClientMeta):
    openapi_spec = openapi_spec
    
    def __init__(self, base_url="https://api.example.com"):
        self.base_url = base_url

# Usage - methods created automatically!
client = APIClient()

# These methods were created by the metaclass!
users = client.list_users()  # Makes GET request to /users
user = client.get_user(user_id=123)  # Makes GET request to /users/123
new_user = client.create_user(name="Alice")  # Makes POST request to /users

print(users)  # {'status': 'mock_response', 'url': 'https://api.example.com/users'}