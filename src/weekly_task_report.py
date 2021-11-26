'''Weekly check'''
import file_writer as fw


def run_weekly():
    '''Run the weekly report writer'''
    try:
        month_file_path = "./files/monthly_report.txt"

        fw.write_week_report(month_file_path)
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':
    run_weekly()