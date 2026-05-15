# WITHOUT metaclass - manual registration (error-prone)
class Plugin:
    plugins = {}  # Manual registry
    
    @classmethod
    def register(cls, name):
        def decorator(plugin_class):
            cls.plugins[name] = plugin_class
            return plugin_class
        return decorator

@Plugin.register('json')
class JSONPlugin(Plugin):
    def process(self, data):
        import json
        return json.loads(data)

@Plugin.register('yaml')
class YAMLPlugin(Plugin):
    def process(self, data):
        import yaml
        return yaml.safe_load(data)

# Problem: Easy to forget @Plugin.register decorator!

# WITH metaclass - automatic registration
class PluginMeta(type):
    """Metaclass that automatically registers plugins"""
    
    # Registry shared by all plugin classes
    _registry = {}
    
    def __new__(cls, name, bases, attrs):
        # Create the class
        new_class = super().__new__(cls, name, bases, attrs)
        
        # Don't register the base Plugin class
        if bases and name != 'Plugin':
            # Get plugin name from class or use class name
            plugin_name = attrs.get('plugin_name', name.lower())
            cls._registry[plugin_name] = new_class
        
        return new_class
    
    @classmethod
    def get_plugin(cls, name):
        return cls._registry.get(name)
    
    @classmethod
    def list_plugins(cls):
        return list(cls._registry.keys())

class Plugin(metaclass=PluginMeta):
    """Base plugin class with automatic registration"""
    
    def process(self, data):
        raise NotImplementedError

# Usage - Automatic registration!
class JSONPlugin(Plugin):
    plugin_name = 'json'  # Optional: custom name
    
    def process(self, data):
        import json
        return json.loads(data)

class YAMLPlugin(Plugin):
    # No plugin_name specified, uses 'yamlplugin'
    def process(self, data):
        import yaml
        return yaml.safe_load(data)

class CSVPlugin(Plugin):
    plugin_name = 'csv'
    
    def process(self, data):
        import csv
        from io import StringIO
        return list(csv.reader(StringIO(data)))

# Plugins are automatically registered!
print("Available plugins:", PluginMeta.list_plugins())
# Output: ['json', 'yamlplugin', 'csv']

# Get plugin by name
json_plugin = PluginMeta.get_plugin('json')()
result = json_plugin.process('{"key": "value"}')