# initiate a class
class Employee:

    # constructor
    def __init__(self):
        print("Started executing sttributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("this travel function is called manually")
        print(f"Employee is now travelling to {destination}")


# creating an object/instance of the class
sam = Employee()


print(type(sam))