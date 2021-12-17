import shelve
import logging

'''
I need to create a workflow chart of how i want this to work fist
'''

logging.basicConfig(level=logging.DEBUG)

def add_task_to_shelv():
    logging.debug('Adding task to shelf')
    _tasks = get_shelf('tasks')

    task_input = input("Please Enter a Task: ")

    

    print(_tasks['Today'])

    _tasks.close()

add_task_to_shelv()

def get_shelf(key):
    logging.debug('Getting shelf with key %s', key)
    shelf_obj = shelve.open(key)
    return shelf_obj

def update_shelf(shelf_obj,key,value):
    logging.debug('Updated shelf %s:%s with values: %s',shelf_obj,key,value)
    shelf_obj[key] = value