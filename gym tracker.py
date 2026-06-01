# simple gym tracker

# functions - create workout, save workout template
# workout - exercise, weight, reps
workouts = {}
x=0

def personal_records():
    global w
    global h
    name = input("Name: ")
    w = float(input("Weight (in kgs): "))
    h = float(input("Height (in m): "))
    age = int(input("Age: "))
    gender = input("Gender: ")

    personal_record=[name, w, h, age, gender]
    return personal_record

def new_workout ():
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
    
    while x!=10:
        workouts[x]=[workout]


def bmi_cal(w, h):
    bmi = w/(h**2)
    print("BMI is: ", bmi)
    return bmi

w_temps = []
def workout_temp():
    n = input("name of the template: ")
    add = input("add exercise / finish: ")
    while add!="finish":
        exer = input("exercise: ")
        sets = input("number of sets: ")
        wt_temp = {n: {"exercise": exer, "sets": sets}}
    w_temps.append(wt_temp)

personal_records()

def menu():
    while True:
        print("\nGYM TRACKER")
        print("1. Add Workout")
        print("2. Make Workout - templates")
        print("3. View Workout - templates")
        print("4. BMI calculator")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_workout()
            break

        elif choice == "2":
            workout_temp()
            break

        elif choice == "3":
            workout_temp()
            break

        elif choice == "4":
            bmi_cal(w, h)
            break

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

menu()
