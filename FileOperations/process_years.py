years_path="C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\years.txt"

centuryyear_path="C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\centuryyear.txt"

leapyear_path="C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\leapyear.txt"

f_read=open(years_path,"r")

f_century=open(centuryyear_path,"w")

f_leapyear=open(leapyear_path,"w")

    
for year in f_read:

    year=int(year)

    if year%100==0:

        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        f_leapyear.write(str(year)+"\n")

f_read.close()
f_century.close()
f_leapyear.close()       










# years_path = "C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\years.txt"
# centuryyear_path = "C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\centuryyear.txt"
# leapyear_path = "C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\leapyear.txt"

# f_read = open(years_path, "r")
# f_century = open(centuryyear_path, "w")
# f_leapyear = open(leapyear_path, "w")


# def is_century_year(year):
#     return True if year % 100 == 0 else False


# def is_leap_year(year):
#     if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
#         return True
#     else:
#         return False


# for year in f_read:
#     year = int(year.strip())  

    
#     if is_century_year(year):
#         f_century.write(str(year) + "\n")

   
#     if is_leap_year(year):
#         f_leapyear.write(str(year) + "\n")


# f_read.close()
# f_century.close()
# f_leapyear.close()



   

