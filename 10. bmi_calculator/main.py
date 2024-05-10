
print("It is a BMI Calculator, write your weight and height to estimate a body fat")

try:
    weight = int(input("Write your weight(kg) here: "))
    height_input = input("Write your height(cm or m, e.g., 187cm or 1.87m) here: ")
    
    if 'cm' in height_input:
        height = float(height_input.replace('cm', '')) / 100
    elif 'm' in height_input:
        height = float(height_input.replace('m', ''))
    else:
        height = float(height_input)
    
    bmi = weight / (height ** 2)
    rounded_bmi = round(bmi, 2)

    print("The result is: ", rounded_bmi)

    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 25:
        print("You have a normal weight")
    elif 25 <= bmi < 30:
        print("You are overweight")
    else:
        print("You are obese.")
except ValueError:
    print("Wrong data. Please provide correct weight in kg and height in meters.")