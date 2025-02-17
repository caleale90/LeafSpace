from datetime import datetime, timedelta


class DaytimeCheck:

    @staticmethod
    def is_daytime(offset_hours):
        current_time = datetime.now()

        new_time = current_time + timedelta(hours=offset_hours)

        daytime_start = new_time.replace(hour=6, minute=0, second=0, microsecond=0)
        daytime_end = new_time.replace(hour=18, minute=0, second=0, microsecond=0)

        if daytime_start <= new_time <= daytime_end:
            return True
        else:
            return False