'''Task tasks and creates report strings'''
from datetime import datetime
import file_writer as fw
import file_reader as fr
from helpers import parse_list, week_start_string

def write_daily_report(report):
    '''Take daily task report and write to weekly report file'''
    tasks_list = fr.get_tasks_from_file()

    complete, incomplete = report

    report = f"Completed {len(complete)} out of {len(tasks_list)} tasks\n Complete:\n{parse_list(complete)}\n Incomplete:\n{parse_list(incomplete)}"
    day = datetime.today().strftime('%A')
    return f"On {day} {report}\n"


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