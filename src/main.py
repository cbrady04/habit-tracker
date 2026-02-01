
from models import *
from tracker import Tracker


def main():
    my_tracker = Tracker()
    habit1 = Habit("Meditate", "Weekly", "Sit down and Meditate for 2 minutes.")
    habit2 = Habit("Run", "Daily", "Run at least a 5K.")
    habit3 = Habit("Brush Teeth", "Daily", "Brush teeth for two minutes")
    my_tracker.add_habit(habit1)
    my_tracker.add_habit(habit2)
    my_tracker.add_habit(habit3)

    for habit in my_tracker.list_habits():
        print(habit.name)

if __name__ == "__main__":
    main()


