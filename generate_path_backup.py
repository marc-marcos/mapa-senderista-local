import datetime


def generate_path_backup():
    current_time = datetime.datetime.now()
    return "backup/backup_{}_{}_{}_{}_{}_{}.db".format(current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute, current_time.second)
