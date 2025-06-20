class x():
    def __init__(self):
        self.str1 = ""

    def get_S (self):
        self.str1 = input("Enter String: ")

    def print_S(self):
        print ("Result is: ", self.str1.upper())


str1 = x()

str1.get_S()
str1.print_S()