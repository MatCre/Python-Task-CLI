'''Daily check'''


import file_reader as fr
import file_writer as fw
import report_writer as rw
import path_finder

def run_daily():
    '''Run a daily check on the status of tasks in the tasks file for this day'''
    user_report = get_task_results()
    report_string = rw.write_daily_report(user_report)
    try:
        with open(path_finder.weekly_report_path, 'a+') as file:
            file.write(report_string)
    except FileNotFoundError:
        print("File not found")


def get_task_results():
    '''Split the tasks into an complete and incomplete list after prompting the user'''
    tasks_list = fr.get_tasks_from_file()
    completed_tasks = []
    incomplete_tasks = []
    for i,v in enumerate(tasks_list):
        current_task = v
        while True:
            result = input(f"Did you do this > {current_task} y/n ?: ")
            if result == "y":
                completed_tasks.append(f"{current_task}")
                break
            if result == "n":
                incomplete_tasks.append(f"{current_task}")
                break
            else:
                print("Invalid Selection")

    return [completed_tasks,incomplete_tasks]

if __name__ == '__main__':
    run_daily()