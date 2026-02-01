class Habit:
    def __init__(self, name, frequency, description):
        self.name = name
        self.frequency = frequency
        self.description = description

    
class Entry:
    def __init__(self, habit_name, date, status):
        self.habit_name = habit_name
        self.date = date
        self.status = status

