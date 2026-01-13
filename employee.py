class Employee:
    def __init__(self, name, id, experience, salary):
        self.name = name
        self.id = id
        self.experience = experience
        self.salary = salary

    def display_employee(self):
        print("Employee Name", self.name)
        print("Employee ID", self.id)
        print("Employee Experience", self.experience)
        print("Employee Salary", self.salary)

    class Address():
        def __init__(self, street, city, state, zip_code,):
            self.street = street
            self.city = city
            self.state = state
            self.zip_code = zip_code

        def display_address(self):
            print("Street:", self.street)
            print("City:", self.city)
            print("State:", self.state)
            print("Zip Code:", self.zip_code)   
    
emp1 = Employee("Chris Hemsworth", "101", 9, 750000)
emp2 = Employee("Chris Evans", "102", 6, 600000)

emp1.Address = emp1.Address("123 Main St", "Los Angeles", "CA", "90001")
emp2.Address = emp2.Address("456 Elm St", "New York", "NY", "10001")
emp1.display_employee()
emp1.Address.display_address()
emp2.display_employee()
emp2.Address.display_address()