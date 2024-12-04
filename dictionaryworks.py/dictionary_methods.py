employee={"id":35,"name":"josh","department":"sales","age":35,"salary":35000}

print(employee.get("department"))

employee.pop("salary")

print(employee)

for k in employee.keys():

    print(k)

for v in employee.values():

    print(v)


for k,v in employee.items():

    print(k,v)