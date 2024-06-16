import math


def main():
        print("This program calculates your Body Mass Index (BMI).")
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        BMI_formula = weight / (height ** 2)
        print("Your BMI is", round(BMI_formula,2))
    
        if BMI_formula <= 18.5:
            print("You are below normal weight")
        elif BMI_formula >= 18.6  and BMI_formula <= 24.99:
            print("Your weight is normal")
        elif BMI_formula >= 25.0  and BMI_formula <= 29.99:
            print("You are overweight")
        elif BMI_formula >= 30.0 and BMI_formula <= 34.99:
            print("You are obese Class I")
        elif BMI_formula >= 35.0 and BMI_formula <= 39.99:
            print("You are obese Class II")
        elif BMI_formula >= 40.0:
            print("You are obese Class III (extreme obesity)")


if __name__ == '__main__':
    main()

