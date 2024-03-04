class man :
    def __init__(self):
        self.name = str(input("enter your name:"))
        self.age = int(input("Enter Your Age: "))
        self.dob = str(input("enter your dob:dd/mm/yyyy"))

    def  display(self):
        print(f"\nhere is your info {self.name}:")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Date of Birth : ", self.dob)

# creating object of the class
person1 = man()
person2 = man()

person1.display()    
person2.display()    