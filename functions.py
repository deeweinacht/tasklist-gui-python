import pathlib
import os
"""
Necessary functions for Task List
"""

TASKS_FILEPATH = pathlib.Path('data', 'task list.txt')


def get_tasks():
    """ Opens a text file and returns the tasks as a list"""
    with open(TASKS_FILEPATH, 'r') as file:
        return file.readlines()


def save_tasks(tasks_to_write):
    """ Opens a text file and writes the given list of tasks to the file, replacing the content of the file"""
    with open(TASKS_FILEPATH, 'w') as file:
        file.writelines(tasks_to_write)


def display_tasks(tasks_to_display):
    """ Accepts a list of tasks and displays them in the console"""
    print(f'\nYour current tasks are:')
    for i, task in enumerate(tasks_to_display):
        task = task.strip('\n')
        print(f'\t{i + 1}. {task}')


def initialize_task_list():
    if not os.path.exists(TASKS_FILEPATH):
        open(TASKS_FILEPATH, 'w')
