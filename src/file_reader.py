'''File Reading / Writting functionality'''

import path_finder

def print_tasks():
    '''View Todays Tasks'''
    file_path = path_finder.tasks_file_path
    try:
        with open(file_path, "r") as file:
            print("Current tasks in file: ")
            for line in file:
                print(line)
    except FileNotFoundError:
        print("No Task File Yet Created")

def get_tasks_from_file(path):
    '''Get tasks from daily task file'''
    tasks = []
    try:
        with open(path, "r") as file:
            for line in file:
                task = line[:-1].strip()
                tasks.append(task)
    except FileNotFoundError:
        print("No task file found")

    return tasks
