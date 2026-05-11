class Company:
    def __init__(self, *founders):
        self.__founders = set(founders)
        self._staff = set(founders)

    def hire(self, name):
        self._staff.add(name) 

    def fire(self, name):
        if name in self.__founders:
            raise ValueError(f"Cannot fire founder {name}")
        self._staff.remove(name)

    def show(self):
        return ", ".join(self._staff)
    
