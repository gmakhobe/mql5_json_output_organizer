from datetime import datetime


def get_duration_in_seconds(start_time, end_time):
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    duration = (end - start).total_seconds()
    return int(duration)


def get_duration_in_minutes(start_time, end_time):
    seconds = get_duration_in_seconds(start_time, end_time)
    minutes = seconds / 60
    return int(minutes)


def get_duration_in_hours(start_time, end_time):
    minutes = get_duration_in_minutes(start_time, end_time)
    hours = minutes / 60
    return float(hours)
