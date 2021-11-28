from time import strftime, localtime


def week_start_string():
    date_local = strftime("%d %b %Y", localtime())
    return f"For Week Starting:  {date_local}"


def parse_list(list):
    '''Parse List'''
    my_str = ''''''
    for i in list:
        my_str += (f"\t{i}\n")

    return my_str
    