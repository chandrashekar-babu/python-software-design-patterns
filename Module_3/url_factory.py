import urllib.request
from abc import ABC, abstractmethod

# --- The Interface ---
class URLReader(ABC):
    @abstractmethod
    def read(self, url: str) -> str:
        pass

# --- Concrete Implementations ---
class FileReader(URLReader):
    def read(self, url: str) -> str:
        # Strip 'file://' to get the local path
        path = url.replace("file://", "")
        with open(path, 'r') as f:
            return f.read()

class HttpReader(URLReader):
    def read(self, url: str) -> str:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')

# --- The Factory ---
class ReaderFactory:
    @staticmethod
    def get_reader(url: str) -> URLReader:
        if url.startswith("file://"):
            return FileReader()
        elif url.startswith("http://") or url.startswith("https://"):
            return HttpReader()
        else:
            raise ValueError(f"Unknown protocol in URL: {url}")

def open_url(url: str):
    try:
        reader = ReaderFactory.get_reader(url)
        content = reader.read(url)
        print(f"--- Content from {url[:30]}... ---")
        print(content[:200]) # Print first 200 chars
    except Exception as e:
        print(f"Error: {e}")

# Examples
# open_url("file:///path/to/your/local_file.txt")
# open_url("https://www.google.com")    
if __name__ == "__main__":
    open_url("file:///path/to/your/local_file.txt")
    open_url("https://www.google.com")
    