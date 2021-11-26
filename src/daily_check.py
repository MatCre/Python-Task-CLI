'''Daily check'''


import file_reader as fr
import file_writer as fw

def run_daily():
    '''Run a daily check on the status of tasks in the tasks file for this day'''
    daily_file_path = "./files/tasks.txt"
    tasks = fr.get_tasks_from_file(daily_file_path)

    print(tasks)

    complete, incomplete = split_task_list(tasks)

    report = f"Completed {len(complete)} out of {len(tasks)} tasks\n Complete: {complete}. Incomplete: {incomplete}"
    
    fw.write_daily_report(report)


def split_task_list(tasks_list):
    '''Split the tasks into an complete and incomplete list after prompting the user'''
    completed_tasks = []
    incomplete_tasks = []
    for task in tasks_list:
        current_task = tasks_list[task]
        while True:
            result = input(f"Did you do this > {current_task} y/n ?: ")
            if result == "y":
                completed_tasks.append(f"{current_task},")
                break
            if result == "n":
                incomplete_tasks.append(f"{current_task},")
                break
            else:
                print("Invalid Selection")

    return [completed_tasks,incomplete_tasks]

if __name__ == '__main__':
    run_daily()