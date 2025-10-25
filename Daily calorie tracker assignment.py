# --------------------------------------------------
# Name: [Ansh Khan]
# Date: [25-oct-25]
# Project: Daily Calorie Tracker CLI (Mini Project)
# --------------------------------------------------

# This program helps you keep track of your daily calorie intake.
# You can add meals, see total and average calories, and check if
# you are within your daily calorie limit.

             # Task 1 : Setup & Introduction
import datetime

print("====================================")
print("      Daily Calorie Tracker App     ")
print("====================================\n")

print("This simple app will help you record your meals and calories.\n")

# ---------- Task 2: Taking User Input ----------

meals = []
calories = []

n = int(input("How many meals do you want to enter today? "))

for i in range(n):
    print(f"\nMeal #{i+1}")
    meal = input("Enter meal name: ")
    cal = float(input("Enter calories for this meal: "))
    meals.append(meal)
    calories.append(cal)

# ---------- Task 3: Calculations ----------

total = sum(calories)
average = total / len(calories)

limit = float(input("\nEnter your daily calorie limit: "))

# ---------- Task 4: Warning System ----------

if total > limit:
    msg = "You have exceeded your daily calorie limit!"
else:
    msg = "You are within your daily calorie limit!"

# ---------- Task 5: Formatted Output ----------
print("\n====================================")
print("           CALORIE REPORT           ")
print("====================================")
print("Meal Name\t\tCalories")
print("------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]:15}\t{calories[i]:.2f}")

print("------------------------------------")
print(f"Total:\t\t\t{total:.2f}")
print(f"Average:\t\t{average:.2f}")
print(msg)
print("====================================\n")
