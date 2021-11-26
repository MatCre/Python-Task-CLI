'''Input tasks'''

import file_reader as fr
import file_writer as fw

import os 

dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname, 'files\\tasks.txt')


def tasks():
    '''Default Entry To View / Add Tasks'''
    running = True

    while running:
        print(""""
Welcome Mathew
1.) View Todays Tasks
2.) Add Task
3.) Delete Task
4.) Exit
        """)

        choice = input()

        if choice == str(1): 
            fr.print_tasks(file_path)
        if choice == str(2):
            fw.add_task(file_path)
        if choice == str(3):
            fw.del_task(file_path)
        if choice == str(4):
            break

