class Clerk:
    sal = 20000
    desig = "Clerk"

    def _init_(self):
        self.uid = input("Enter id: ")
        self.name = input("Enter name: ")
        self.age = input("Enter age : ")

    def display(self):
        print("==============")
        print("Name :", self.name)
        print("ID :", self.uid)
        print("Age: ", self.age)
        print("Salary: ", self.sal)
        print("Designation: ", self.desig)

    def raiseSal(self):
        print("==============")
        print("Name :", self.name)
        print("ID :", self.uid)
        print("Age: ", self.age)
        print("Salary: ", self.sal + 10000)
        print("Designation: ", self.desig)


class Tester:
    sal = 30000
    desig = "Tester"

    def _init_(self):
        self.uid = input("Enter id: ")
        self.name = input("Enter name: ")
        self.age = input("Enter age : ")

    def display(self):
        print("==============")
        print("Name :", self.name)
        print("ID :", self.uid)
        print("Age: ", self.age)
        print("Salary: ", self.sal)
        print("Designation: ", self.desig)

    def raiseSal(self):
        print("==============")
        print("Name :", self.name)
        print("ID :", self.uid)
        print("Age: ", self.age)
        print("Salary: ", self.sal + 20000)
        print("Designation: ", self.desig)


class Developer:
    sal = 35000
    desig = "Developer"

    def _init_(self):
        self.uid = input("Enter id: ")
        self.name = input("Enter name: ")
        self.age = input("Enter age : ")

    def display(self):
        print("==============")
        print("Name :", self.name)
        print("ID :", self.uid)
        print("Age: ", self.age)
        print("Salary: ", self.sal)
        print("Designation: ", self.desig)

    def raiseSal(self):
        print("==============")
        print("Name :", self.name)
        print("ID :", self.uid)
        print("Age: ", self.age)
        print("Salary: ", self.sal + 25000)
        print("Designation: ", self.desig)


class Manager:
    sal = 40000
    desig = "Manager"

    def _init_(self):
        self.uid = input("Enter id: ")
        self.name = input("Enter name: ")
        self.age = input("Enter age : ")

    def display(self):
        print("==============")
        print("Name :", self.name)
        print("ID :", self.uid)
        print("Age: ", self.age)
        print("Salary: ", self.sal)
        print("Designation: ", self.desig)

    def raiseSal(self):
        print("==============")
        print("Name :", self.name)
        print("ID :", self.uid)
        print("Age: ", self.age)
        print("Salary: ", self.sal + 30000)
        print("Designation: ", self.desig)


print("Select any one...")
while True:

    print("1. Create \n 2. Display \n 3. Raise Salary\n 4. Exit")
    ch = int(input("enter your choice: "))
    if ch != 4:
        if ch == 1:
            print("\n1. Clerk\n2. Tester\n3. Developer\n4. Manager\n 5. Exit")
            ch2 = int(input("Enter the Job Role: "))
            if ch2 == 1:
                c = Clerk()
            elif ch2 == 2:
                t = Tester()
            elif ch2 == 3:
                d = Developer()
            elif ch2 == 4:
                m = Manager()
            else:
                break;
        elif ch == 2:
            if ch2 == 1:
                c.display()
            elif ch2 == 2:
                t.display()
            elif ch2 == 3:
                d.display()
            elif ch2 == 4:
                m.display()
            else:
                break;
        elif ch == 3:
            if ch2 == 1:
                c.raiseSal()
            elif ch2 == 2:
                t.raiseSal()
            elif ch2 == 3:
                d.raiseSal()
            elif ch2 == 4:
                m.raiseSal()
            else:
                break;

        else:
            break;
    else:
        break;

print("!!-------Thank you-------!!")
