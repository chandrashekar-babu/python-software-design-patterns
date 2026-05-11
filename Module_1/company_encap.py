def company(*founders):
    staff = set(founders)

    def hire(name):
        staff.add(name) # Local-variable of company is accessed as 'enclosing scope'

    def fire(name):
        if name in founders:
            raise ValueError(f"Cannot fire founder {name}")
        staff.remove(name)

    def show():
        return ", ".join(staff)

    return hire, fire, show