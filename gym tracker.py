# simple gym tracker

# functions - create workout, save workout template
# workout - exercise, weight, reps
import json
import os
from datetime import date
import pandas as pd

file = "gym_data.json"

data = pd.read_csv("exercises.csv")

print(data.head())


workouts = {}
x=0

def load():
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {"templates": {}, "personal_records": {}, "history": []}

def save(data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def get_number(prompt, number_type=float):
    while True:
        value = input(prompt)
        try:
            return number_type(value)
        except ValueError:
            print("That's not a valid number, please try again.")

def personal_records():
    name = input("Name: ")
    w = get_number("Weight (in kgs): ", float)
    h = get_number("Height (in m): ", float)
    age = int(input("Age: "))
    gender = input("Gender: ")
    data = load()

    data["profile"]={"Name":name,"Weight":w, "Height":h, "Age":age, "Gender":gender}
    save(data)

def new_workout(name):
    print("enter exercises")
    a = input("add exercise / finish: ")
    workout = []
    volume = 0
    while a != "finish":
        exercise = input("exercise: ")
        weight = get_number("weight: ",int)
        reps = get_number("reps: ",int)
        workout.append([exercise, weight, reps])
        volume = volume + (weight * reps)
        a = input("add exercise / finish: ")

    data = load()
    sesh = {"date": str(date.today()), "name": name, "total volume": volume, "exercises": workout}
    data["history"].append(sesh)
    save(data)
    print("workout saved. total volume ", volume, "kg")

def bmi_cal():
    data = load()
    profile = data.get("profile")

    if not profile:
        print("set up profile first")
        return
    w = profile["Weight"]
    h = profile["Height"]
    bmi = w/(h**2)
    print("BMI is: ", bmi)
    return bmi

w_temps = []

def workout_temp(n):
    data = load()

    if n in data["templates"]:
        print(f"A template named '{n}' already exists.")
        overwrite = input("Overwrite it? (y/n): ").strip().lower()
        if overwrite != "y":
            print("Cancelled. Try a different name.")
            return

    exercises = []
    add = input("add exercise / finish: ")
    while add != "finish":
        exer = input("exercise: ")
        sets = input("number of sets: ")
        wt = {"exercise": exer, "sets": sets}
        exercises.append(wt)
        add = input("add exercise/finish: ")

    data["templates"][n] = exercises
    save(data)
    print("template ", n, " is saved")

def view_temp(temp_name):
    data = load()
    return data["templates"].get(temp_name)


STANDARD_TEMPLATES = {
    "Push Day": [{"exercise": "Bench Press", "sets": "3"},
                 {"exercise": "Overhead Press", "sets": "3"},
                 {"exercise": "Tricep Dip", "sets": "3"}],
    "Pull Day": [{"exercise": "Pull-up", "sets": "3"},
                 {"exercise": "Barbell Row", "sets": "3"},
                 {"exercise": "Bicep Curl", "sets": "3"}],
    "Leg Day": [{"exercise": "Squat", "sets": "3"},
                {"exercise": "Lunge", "sets": "3"},
                {"exercise": "Leg Press", "sets": "3"}]
}


def view_all_templates():
    """Show every template — both user-created and standard — in one combined view."""
    data = load()

    print("\nYour templates:")
    if not data["templates"]:
        print("  (none yet)")
    for name in data["templates"]:
        print(f"\n{name}:")
        for ex in data["templates"][name]:
            print(f"  - {ex['exercise']} ({ex['sets']} sets)")

    print("\nStandard templates:")
    for name in STANDARD_TEMPLATES:
        print(f"\n{name}:")
        for ex in STANDARD_TEMPLATES[name]:
            print(f"  - {ex['exercise']} ({ex['sets']} sets)")

def see_exercises():
    muscles = data["primary_muscle"].unique()
    print("Choose which muscle: ")
    print(muscles)
    muscle = input("enter muscle : ")

    if muscle in muscles:
        print("Exercises for ", muscle)

        exer_list = data[data["primary_muscle"] == muscle]["name"].tolist()
        for i in exer_list:
            print(i)
    
    else:
        print("invalid muscle")
    

def delete_temp():
    data = load()

    if not data["templates"]:
        print("No templates to delete.")
        return

    print("Your templates:")
    for name in data["templates"]:
        print(f"  - {name}")

    temp_name = input("Enter the name of the template to delete: ")

    if temp_name in data["templates"]:
        del data["templates"][temp_name]
        save(data)
        print(f"'{temp_name}' deleted.")
    else:
        print("That template doesn't exist.")

def edit_temp():
    data = load()

    if not data["templates"]:
        print("No templates to edit.")
        return

    print("Your templates:")
    for name in data["templates"]:
        print(f"  - {name}")

    temp_name = input("Enter the name of the template to edit: ")

    if temp_name not in data["templates"]:
        print("That template doesn't exist.")
        return

    while True:
        exercises = data["templates"][temp_name]

        print(f"\nCurrent exercises in '{temp_name}':")
        for i, ex in enumerate(exercises):
            print(f"  {i + 1}. {ex['exercise']} ({ex['sets']} sets)")

        print("\na. Add exercise")
        print("d. Delete exercise")
        print("f. Finish editing")
        action = input("Choose an option: ").strip().lower()

        if action == "a":
            exer = input("exercise name: ")
            sets = input("number of sets: ")
            exercises.append({"exercise": exer, "sets": sets})
            print(f"Added {exer}.")

        elif action == "d":
            if not exercises:
                print("Nothing to delete.")
                continue
            num = get_number("Enter the number of the exercise to delete: ", int)
            if 1 <= num <= len(exercises):
                removed = exercises.pop(num - 1)
                print(f"Removed {removed['exercise']}.")
            else:
                print("Invalid number.")

        elif action == "f":
            break

        else:
            print("Invalid choice.")

    data["templates"][temp_name] = exercises
    save(data)
    print(f"'{temp_name}' updated.")
    

def menu():
    while True:
        print("\nGYM TRACKER")
        print("0. Set up profile/edit profile")
        print("1. Add Workout")
        print("2. Make Workout - templates")
        print("3. View Template")
        print("4. View all workout templates list")
        print("5. View exercises")
        print("6. Delete Template")
        print("7. Edit Templates")
        print("8. BMI calculator")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "0": # set up profile
            personal_records()

        elif choice == "1": # add workout
            name = input("name of the workout: ")
            new_workout(name)

        elif choice == "2": # make template
            n = input("name of the new template to create: ")
            workout_temp(n)

        elif choice == "3": # view template
            temp_name = input("name of template to get: ")
            view_temp(temp_name)
        
        elif choice == "4": # list of all templates
            view_all_templates()

        elif choice == "5": # see exercises
            see_exercises()

        elif choice == "6": # delete template
            delete_temp()

        elif choice == "7": # edit temps
            edit_temp()

        elif choice == "8": # bmi calculator
            bmi_cal()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

menu()