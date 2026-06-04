# simple gym tracker

# functions - create workout, save workout template
# workout - exercise, weight, reps
import json
import os
from datetime import date

file = "gym_data.json"


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

def personal_records():
    global w
    global h
    name = input("Name: ")
    w = float(input("Weight (in kgs): "))
    h = float(input("Height (in m): "))
    age = int(input("Age: "))
    gender = input("Gender: ")
    data = load()

    data["profile"]={"Name":name,"Weight":w, "Height":h, "Age":age, "Gender":gender}
    save(data)

def new_workout (name):
    print("enter exercises")
    a = input("add exercise / finish: ")
    workout=[]
    volume = 0
    while a!="finish":
        exercise = input("exercsie: ")
        weight = int(input("weight: "))
        reps = int(input("reps: "))
        a = input("add exercise / finish: ")
        workout.append([exercise, weight, reps])
        volume = volume + (weight*reps)
        return volume;
    data = load()
    sesh = { "date": str(date.today()), "name":name, "total volume": volume, "exercises": workout}
    data["history"].append(sesh)
    save(data)
    print("workout saved. total volume ", volume, "kg")

def bmi_cal():
    data = load()
    profile = data.get("profile")

    if not profile:
        print("set up profile first")
        return
    w = profile["weight"]
    h = profile["height"]
    bmi = w/(h**2)
    print("BMI is: ", bmi)
    return bmi

w_temps = []

def workout_temp(n):
    exercises = []
    add = input("add exercise / finish: ")
    while add!="finish":
        exer = input("exercise: ")
        sets = input("number of sets: ")
        wt = {"exercise": exer, "sets": sets}
        exercises.append(wt)
        add = input("add exercise/finish: ")
    data = load()
    data["templates"][n]=exercises
    save(data)
    print("template ",n," is saved")

def view_temp(temp_name):
    data = load()
    return data["templates"].get(temp_name)

def list_temps():
    data = load()
    for name in data["templates"]:
        print(name)
        exercises = data["templates"][name]
    

def menu():
    while True:
        print("\nGYM TRACKER")
        print("0. Set up profile/edit profile")
        print("1. Add Workout")
        print("2. Make Workout - templates")
        print("3. View Template")
        print("4. View all workout templates list")
        print("5. BMI calculator")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            personal_records()

        elif choice == "1":
            name = input("name of the workout: ")
            new_workout(name)

        elif choice == "2":
            n = input("name of the new template to create: ")
            workout_temp(n)

        elif choice == "3":
            temp_name = input("name of template to get: ")
            view_temp(temp_name)
        
        elif choice == "4":
            temp_name = input("name of template to get: ")
            list_temps()

        elif choice == "5":
            bmi_cal()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

menu()
