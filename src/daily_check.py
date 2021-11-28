'''Daily check'''


import file_reader as fr
import file_writer as fw
import report_writer as rw
import path_finder

def parse_list(list):
    '''Parse List'''
    my_str = ''''''
    for i in list:
        my_str += (f"\t{i}\n")

    return my_str

def run_daily():
    '''Run a daily check on the status of tasks in the tasks file for this day'''
    tasks_list = fr.get_tasks_from_file(path_finder.tasks_file_path)

    print(tasks_list)

    complete, incomplete = get_task_results(tasks_list)

    report = f"Completed {len(complete)} out of {len(tasks_list)} tasks\n Complete:\n{parse_list(complete)}\n Incomplete:\n{parse_list(incomplete)}"
    
    rw.write_daily_report(report)


def get_task_results(tasks_list):
    '''Split the tasks into an complete and incomplete list after prompting the user'''
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