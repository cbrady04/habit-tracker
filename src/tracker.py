class Tracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def list_habits(self):
        return self.habits
    