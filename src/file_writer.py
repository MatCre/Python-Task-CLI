from file_reader import get_tasks_from_file
import path_finder as my_paths
       
def write_list_to_file(task_list):
    '''Ovewrite the current tasks in the files with the incoming task list'''

    #Clear the file
    try:
        open(my_paths.tasks_file_path,'w').close()
    except FileNotFoundError:
        print("File not found")

    #Write the updated task list to the file
    try:
        with open(my_paths.tasks_file_path, "a+") as file:
                for task in task_list:
                    file.write(f"{task} \n")
    except FileNotFoundError:
        print("File not found")

def add_task():
    '''Add A Task'''
    
    tasks = get_tasks_from_file()

    try :
        while True:
            task_input = input("Please Enter a Task: ")

            tasks.append(task_input)
            print(f"{task_input} added")

            exit = input("Add another task ?:  Y / N")

            if exit.lower() == "n":
                write_list_to_file(tasks)
                break
    except ValueError:
        print("Enter a valid option")
    finally:
        write_list_to_file(tasks)
    
def del_task():
    '''Remove a task from current task list'''
    tasks = get_tasks_from_file()

    while True:
        try:
            task_to_delete = input("Enter the task you want to delete: ")
            if task_to_delete in tasks:
                print(f"{task_to_delete} deleted.")
                tasks.remove(task_to_delete)
                break
            elif task_to_delete == 'cancel':
                break
            else:
                print("Task does not exist")
        except:
            print("Task Not In List")
    
    write_list_to_file(tasks)

def clear_file():
    try:
        with open(my_paths.tasks_file_path, "w") as file:
            print(f"Clearing task file from {file}")
    except FileNotFoundError:
        print("File Not Found")
    
