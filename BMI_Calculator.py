# Asking the user their body mass and height.
user_mass = int(input("Enter year of your body mass "))
user_height = float(input("Enter year of your height "))

# Formula to calculate the BMI
total_height = (user_height **2)
bmi = (user_mass/total_height)

# Print the result
print("Your BMI is", bmi)
