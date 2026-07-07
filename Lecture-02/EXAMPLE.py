age = input("Enter your age:")
age = int(age)

height = input("Enter your height: ")
height = float(height)

print("You are " + str(age) + " years old and " + str(height) + "feet tall .")

weight = int(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters:"))
bmi = weight / (height ** 2)
print("your BMI is:" ,format (bmi, ".2f"))

celsius = float(input("Enter temperature in Celsius:"))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit is", fahrenheit)