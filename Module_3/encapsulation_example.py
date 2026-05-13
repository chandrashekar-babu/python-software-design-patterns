def company(*founders):
    staff = []

    def hire(employee):
        staff.append(employee)
        print(f"{employee} is hired")

    def fire(employee):
        if employee in founders:
            print(f"Cannot fire {employee} as they are a founder")
        elif employee in staff:
            staff.remove(employee)
            print(f"{employee} is fired")
        else:
            print(f"{employee} is not an employee")
    
    def show():
        print("Founders:", founders)
        print("Staff:", staff)

    return hire, fire, show

hire, fire, show = company("Alice", "Bob")

hire("Charlie")
hire("Dave")
show()
fire("Charlie")
show()
fire("Alice")
show()