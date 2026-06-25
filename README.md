# gym-tracker-project
<<<<<<< HEAD
=======
# Gym Tracker

A simple command-line gym tracker built in Python. It lets you set up a profile, log workouts, build reusable workout templates, and calculate your BMI — all saved persistently to a local JSON file.

## Features

- **Set up / edit profile** — create or update your personal profile info
- **Add workout** — log a new workout by name
- **Make workout template** — create a reusable workout template to follow in future sessions
- **View template** — look up and view a specific saved template by name
- **View all workout templates** — list every saved template
- **BMI calculator** — calculate your Body Mass Index
- **Exit** — close the program

## How it works

The app runs on a simple text menu loop. On launch, you're shown a numbered list of options and prompted to enter a choice:

```
GYM TRACKER
0. Set up profile/edit profile
1. Add Workout
2. Make Workout - templates
3. View Template
4. View all workout templates list
5. BMI calculator
6. Exit
```

Each option calls its own function:

| Choice | Action | Function |
|--------|--------|----------|
| 0 | Set up or edit your profile | `personal_records()` |
| 1 | Add a new workout | `new_workout(name)` |
| 2 | Create a new workout template | `workout_temp(n)` |
| 3 | View a specific saved template | `view_temp(temp_name)` |
| 4 | View all saved templates | `list_temps()` |
| 5 | Calculate BMI | `bmi_cal()` |
| 6 | Exit the program | — |

## Data storage

All data is saved locally in `gym_data.json`, so your profile, workouts, and templates persist between runs of the program.

## Getting started

1. Make sure you have Python 3 installed.
2. Clone or download this project.
3. Run the tracker:
   ```bash
   python3 "gym tracker.py"
   ```
4. Follow the on-screen menu to set up your profile and start logging workouts.

## Project structure

```
gym tracker/
├── gym tracker.py     # Main program with menu and functions
├── gym_data.json       # Stores profile, workouts, and templates
└── README.md
```

## Notes

This is a beginner-friendly project built and improved incrementally — focused on getting core functionality (data persistence, menu flow, and function connectivity) working correctly before adding more advanced features.
>>>>>>> cbc2e13bdcebc95dfc088d722b089fdb10124abe
