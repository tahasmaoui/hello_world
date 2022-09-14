name = input("What is your name? ")
print("Hello " + name)
Birth_year = input("What is your birth year? ")
Your_age = (2022 - int(Birth_year))
print("your age is ", Your_age)
height_in_cm = input("what is your height in cm ")
height_in_m = int(height_in_cm) / 100
print("your height in m is ", height_in_m)
weight_in_kg = input("what is your weight in kg? ")
weight_in_lbs = int(weight_in_kg) * 2.2
print("your weight in lbs is ", weight_in_lbs)
if int(weight_in_kg) < 10 or int(height_in_cm) < 100:
    print("cut the crap")
else:
    print("You are in a good shape ", name, ".")