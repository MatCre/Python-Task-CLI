'''Create paths for files based on user directory'''

import os 

dirname = os.path.dirname(__file__)
tasks_file_path = os.path.join(dirname, 'files\\tasks.txt')
weekly_report_path = os.path.join(dirname, 'files\\weekly_report.txt')

