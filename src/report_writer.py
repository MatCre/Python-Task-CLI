'''Task tasks and creates report strings'''
from datetime import datetime
from file_writer import get_tasks_from_file
from week_string import week_start_string

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