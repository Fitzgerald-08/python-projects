def my_function(*fruits):
    print("For dinner i am going to have " + fruits[3])


my_function("apple", "orange", "banana", "grapes", "watermelon")


def my_function(**fullname):
    print("My name is " + fullname["fname"] + ", and my last name is " + fullname["lname"])


my_function(fname="Alex", lname="Márquez")


def my_function(country="México"):
    print("I am from " + country)


my_function()
my_function("Italy")
my_function("France")
my_function("Switzerland")
