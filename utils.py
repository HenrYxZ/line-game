def format_time(time: float) -> str:
    minutes, seconds = divmod(time, 60)
    return "%02d:%02d" % (minutes, seconds)
