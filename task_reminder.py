from collections import namedtuple
from utils.utils import prompt_gpt

# record the todo tasks and then tell the user what task to do next based on priority and deadline.
class Task:
    def __init__(self, name: str, time: str, priority: int):
        self.name = name
        self.time = time
        self.priority = priority

def extract_task_from_sentence(sentence: str) -> Task:
    """
    Extracts task information from a sentence using the prompt_gpt method.

    Args:
        sentence (str): The input sentence describing the task.

    Returns:
        Task: An instance of the Task class with extracted information.
    """
    response = prompt_gpt(f"Extract task name, time, and priority from: '{sentence}. Respond in JSON format with keys 'name', 'time', and 'priority'.", options={"response_format": "json"})
    task_data = response.get("task", {})
    return Task(
        name=task_data.get("name", "Unnamed Task"),
        time=task_data.get("time", "No Time Specified"),
        priority=task_data.get("priority", 0)
    )