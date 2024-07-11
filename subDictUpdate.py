student = {
        "name" : "azam",
        "subjects" : {
                "sci" : 98,
                "maths": 78,
                "eng" : 89
        }
}
print(student)
print(student["subjects"])
print(student["subjects"]["eng"])
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(student.items())
student.update({"city": "delhi"})
newdict = {"country" : "India"}
student.update(newdict)
print(student)
