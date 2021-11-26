from time import strftime, localtime


def week_start_string():
    date_local = strftime("%d %b %Y", localtime())
    return f"For Week Starting:  {date_local}"
    