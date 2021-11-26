'''File Reading / Writting functionality'''
        
def print_tasks(file_path):
    '''View Todays Tasks'''
    try:
        with open(file_path, "r") as file:
            print("Current tasks in file: ")
            for line in file:
                print(line)
    except FileNotFoundError:
        print("No Task File Yet Created")

def get_tasks_from_file(file_path):
    '''Get tasks from daily task file'''
    tasks = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                task = line[:-1].strip()
                tasks.append(task)
    except FileNotFoundError:
        print("No task file found")

    return tasks
