class Person:
    def __init__(self, first, last, add):
        self.first = first
        self.last = last
        self.adress = add

    # Getter Method
    @property
    def email(self):
        return self.first + "." + self.last + "@email.com"

    @property
    def fullname(self):
        return self.first + " " + self.last

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("Full name deleted...")


per = Person("Sam", "Edison", "India")
print(per.fullname)
print(per.email)
per.fullname = "Blesson Jordan"
per.first = "Samuel"
print(per.fullname)
print(per.email)
del per.fullname
print(per.first)
print(per.last)