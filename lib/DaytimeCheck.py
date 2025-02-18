from datetime import datetime, timedelta


class DaytimeCheck:

    def is_daytime(self, offset_hours):
        current_time = datetime.now()

        new_time = current_time + self.parse_offset(offset_hours)

        daytime_start = new_time.replace(hour=6, minute=0, second=0, microsecond=0)
        daytime_end = new_time.replace(hour=18, minute=0, second=0, microsecond=0)

        if daytime_start <= new_time <= daytime_end:
            return True
        else:
            return False

    @staticmethod
    def parse_offset(offset_str):
        print(offset_str)
        if offset_str == "0:00":
            return timedelta()

        sign = 1 if offset_str.startswith("+") else -1
        hours, minutes = map(int, offset_str[1:].split(":"))
        return timedelta(hours=sign * hours, minutes=sign * minutes)