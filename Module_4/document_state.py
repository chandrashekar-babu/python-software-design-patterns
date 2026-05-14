class DraftDocument:
    def __init__(self, document):
        self.document = document

    def publish(self):
        self.document._state = "published"

    def clear(self):
        self.document._title = ""
        self.document._content = ""

    @property
    def title(self):
        return self.document._title
    
    @title.setter
    def title(self, value):
        if type(value) is not str or not value.strip():
            raise ValueError("Title must be a non-empty string.")
        self.document._title = value

    @property
    def content(self):
        return self.document._content
   
    @content.setter
    def content(self, value):
        if type(value) is not str:
            raise ValueError("Content must be a string.")
        self.document._content = value

class PublishedDocument:
    def __init__(self, document):
        self.document = document

    def archive(self):
        self.document._state = "archived"

    def clear(self):
        raise Exception("Cannot clear a published document.")

    @property
    def title(self):
        return self.document._title
    
    @property
    def content(self):
        return self.document._content
    
class ArchivedDocument:
    def __init__(self, document):
        self.document = document

    def __getattr__(self, name):
        raise Exception("Archived documents cannot be accessed.")
    
    @property
    def title(self):
        raise Exception("Archived documents cannot be accessed.")
    
    @property
    def content(self):
        raise Exception("Archived documents cannot be accessed.")
    
class Document:
    def __init__(self, title, content):
        self.__dict__['_states'] = {
            "draft": DraftDocument(self),
            "published": PublishedDocument(self),
            "archived": ArchivedDocument(self)
        }
        self.__dict__['_state'] = "draft"
        self.title = title
        self.content = content
        
    def __getattr__(self, name):
        state_instance = self._states[self._state]
        
        if hasattr(state_instance, name):
            return getattr(state_instance, name)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
