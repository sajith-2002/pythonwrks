# f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\all_students.txt", 'r')
   
# all_students = []
# for line in f:
        
#         all_students.append(line.strip())


# f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\failed.txt", 'r')

# failed_students = []
# for line in f:
        
#         failed_students.append(line.strip())

# passed_students = []
# for student in all_students:
#     if student not in failed_students:
#         passed_students.append(student)


# print("Passed students:")
# for student in passed_students:
#     print(student)







# f1=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\all_students.txt", 'r')
# f2=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\failed.txt", 'r')

# all_students=set()

# failed_students=set()

# for line in f1:
      
#       line=line.rstrip("\n")

#       all_students.add(line)

# for line in f2:
      
#       line=line.rstrip("\n")

#       failed_students.add(line)

# passed_students=all_students.difference(failed_students)

# print(passed_students)









f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\all_students.txt", 'r')

all_students = [line.strip() for line in f]


f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\failed.txt", 'r') 

failed_students = [line.strip() for line in f]


passed_students = [student for student in all_students if student not in failed_students]


for student in passed_students:

    print(student)

f.close()