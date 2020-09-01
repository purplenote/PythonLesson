# Python Code Lesson-03
# You can find the source code at Github:
# https://github.com/purplenote/PythonLesson

# Dictionary     

a = {
    "Fish": 3.0,
    "Dog":  30,
    "Cat":  12.0,
    "Elephant": "Unknown"
}
print(a)

priceFish = a["Fish"]
a["Dog"] = 50

keys = a.keys()
values = a.values()
l = len(a)
a["Monkey"] = 60
a.pop("Fish")


print("Thank you!")

