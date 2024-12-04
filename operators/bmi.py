w_in_kg=int(input('enter the w in kg:'))
h_in_cm=int(input('enter the h in cm:'))

h_in_m=h_in_cm/100

BMI=w_in_kg/h_in_m**2

BMI=round(BMI)

print(BMI)