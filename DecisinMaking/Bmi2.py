weight=int(input("Enter weight in kg:"))

height=int(input("Enter height in cm:"))

age=int(input("Enter age:"))

gender=input("Enter gender:").lower()

print(weight,height,age,gender)

if gender=="male":

    BMR= 10*weight + 6.25*height - 5*age + 5
    print(f"BMR={BMR}")

elif gender=="female":
    BMR= 10*weight + 6.25*height - 5*age + 161
    print(f"BMR={BMR}")

else :
    print("Please enter valid gender ")

activity_level=int(input("""
    select acitivity level
    press 1 for sedentary
    press 2 for lightly active
    press 3 for moderatly active
    press 4 for very active
    press 5 for extra active
                        
 """))

if activity_level==1:
    calorie=BMR*1.2

elif activity_level==2:
    calorie=BMR*1.375
elif activity_level==3:
    calorie=BMR*1.55

elif activity_level==4:
    calorie=BMR*1.725

elif activity_level==5:
    calorie=BMR*1.9

else :
    print("Enter valid number for activity level.....")
    
print(f"calorie={calorie}")