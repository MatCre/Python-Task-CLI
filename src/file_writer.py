from datetime import datetime
from file_reader import get_tasks_from_file
from week_string import week_start_string

import os 

dirname = os.path.dirname(__file__)
task_file_path = os.path.join(dirname, 'files\\tasks.txt')
weekreport_file_path = os.path.join(dirname, 'files\\weekly_report.txt')
       
def write_list_to_file(path,task_list):
    '''Ovewrite the current tasks in the files with the incoming task list'''

    #Clear the file
    try:
        open(path,'w').close()
    except FileNotFoundError:
        print("File not found")

    #Write the updated task list to the file
    try:
        with open(path, "a+") as file:
                for task in task_list:
                    file.write(f"{task} \n")
    except FileNotFoundError:
        print("File not found")

def add_task(path):
    '''Add A Task'''
    
    tasks = get_tasks_from_file(path)

    try :
        while True:
            task_input = input("Please Enter a Task: ")

            tasks.append(task_input)
            print(f"{task_input} added")

            exit = input("Add another task ?:  Y / N")

            if exit.lower() == "n":
                write_list_to_file(path,tasks)
                break
    except ValueError:
        print("Enter a valid option")
    finally:
        write_list_to_file(path,tasks)
    
def del_task(path):
    '''Remove a task from current task list'''
    tasks = get_tasks_from_file(path)

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
    
    write_list_to_file(path,tasks)

def write_daily_report(path):
    '''Take daily task report and write to weekly report file'''
    day = datetime.today().strftime('%A')
    tasks = get_tasks_from_file(path)
    task_breakdown_string = ""
    for task in tasks:
        task_breakdown_string += f"\n{task.upper()}: "
        
    # try:
    #     with open("./files/weekly_report.txt", "a+") as file:
    #         file.write(f"On {day} {daily_report}\n")
    #         file.write(task_breakdown_string)
    # except FileNotFoundError:
    #     print("File Not Found")

def write_week_report(week_report):
    '''Write the report of the week'''

    week_string = week_start_string()
    try:
        with open("./files/monthly_report.txt", "a+") as file:
            file.write(week_string)
            with open("./files/weekly_report.txt", "r") as week_file:
                for line in week_file:
                    file.write(line)       
    except FileNotFoundError:
        print("File not found")