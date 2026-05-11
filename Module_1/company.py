founders = {"Alice", "Bob"}
staff = set(founders)

def hire(name):
    staff.add(name)

def fire(name):
    if name in founders:
        raise ValueError(f"Cannot fire founder {name}")
    staff.remove(name)

def show():
    return ", ".join(staff)

