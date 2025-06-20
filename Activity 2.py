class Employee():
    def __init__(self):
       print ("Employee created")

    def __del__(self):
       print ("Destructor Called")

def create():
     print ("Making object...")
     obj = Employee()
     print ("Oject created")
     return obj

print ("Creating obj...")
obj = create()
print ("Program ending..")