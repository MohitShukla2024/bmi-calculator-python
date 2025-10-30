# BMI Calculator (thoda casual version)
def calculate_bmi(w, h):
    # BMI ke liye simple formula
    return w / (h * h)

def bmi_status(bmi):
    # BMI category decide karne ke liye
    if bmi < 18.5:
        return "You are underweight."
    elif bmi < 25:
        return "You have a normal weight."
    elif bmi < 30:
        return "You are overweight."
    else:
        return "You have obesity."
    
print("Hello! This is a simple BMI checker.")
try:
    weight = float(input("Type your weight in kg: "))
    height = float(input("Type your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = bmi_status(bmi)

    print("\nYour BMI is about", round(bmi, 2))
    print(category)
    print("Take care of your health!😊")

except:
    print("Oops! Please enter valid numbers only, not letters or symbols.")
