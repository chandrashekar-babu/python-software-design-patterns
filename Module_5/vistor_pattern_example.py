from pathlib import Path
from typing import Any, Callable, Dict

# Simple visitor using functions (more Pythonic)
class FileVisitor:
    def __init__(self):
        self.handlers: Dict[str, Callable] = {}
    
    def register(self, extension: str, handler: Callable):
        """Register a handler for a specific file type"""
        self.handlers[extension] = handler
    
    def visit(self, filepath: Path):
        """Visit a file and apply the appropriate handler"""
        ext = filepath.suffix.lower()
        if ext in self.handlers:
            return self.handlers[ext](filepath)
        return self.handlers.get('*', lambda x: f"No handler for {x}")(filepath)

# Usage
visitor = FileVisitor()

# Define operations
def analyze_python(file: Path) -> str:
    return f" Analyzing Python file: {file.name}"

def analyze_text(file: Path) -> str:
    return f" Reading text file: {file.name}"

def analyze_json(file: Path) -> str:
    return f" Parsing JSON: {file.name}"

# Register visitors
visitor.register('.py', analyze_python)
visitor.register('.txt', analyze_text)
visitor.register('.json', analyze_json)
visitor.register('*', lambda x: f"❓ Unknown type: {x.name}")

# Use the visitor
files = [Path("main.py"), Path("data.json"), Path("notes.txt"), Path("image.png")]
for file in files:
    result = visitor.visit(file)
    print(result)