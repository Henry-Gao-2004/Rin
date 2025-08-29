from collections import namedtuple

# record the todo tasks and then tell the user what task to do next based on priority and deadline.
class Task:
    def __init__(self, name: str, time: str, priority: int):
        self.name = name
        self.time = time
        self.priority = priority