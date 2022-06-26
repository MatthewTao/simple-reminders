"""
Object definition for the reminder
"""
import calendar
from datetime import datetime

from src.utils import (
    read_config, read_reminder_list, round_up, determine_number_suffix, next_day_of_week,
    str_fmt_minutes, str_fmt_days)


class Reminder:
    def __init__(self):
        # Read configs
        config = read_config()

        # Read list of reminders
        self.reminder_list = read_reminder_list(config)

        self.now = datetime.now()

    def determine_time_remaining(self):
        """
        For each item that is being tracked,
        determine when the item is due.
        """
        self.now = datetime.now()
        due_reminders = []
        for reminder in self.reminder_list:
            reminder_type = reminder.get('reminder_type')
            if reminder_type == 'annual':
                result = self.handle_annual(reminder)
            elif reminder_type == 'monthly':
                result = self.handle_monthly(reminder)
            elif reminder_type == 'weekly':
                result = self.handle_weekly(reminder)
            elif reminder_type == 'daily':
                result = self.handle_daily(reminder)

            if result is not None:
                due_reminders.append(result)
        return due_reminders

    def handle_annual(self, reminder):
        # Get date of anniversary
        year = reminder.get('year', self.now.year)
        month = reminder.get('month')
        day = reminder.get('day')
        remind_after = reminder.get('remind_after')
        description = reminder.get('description')

        ann_date = datetime(year=year, month=month, day=day)
        time_to_ann = self.now - ann_date
        time_to_next_ann = (datetime(year=self.now.year, month=month, day=day) - self.now)
        n_ann = round_up(time_to_ann.days/365) if time_to_ann.days > 365 else ''

        description_suffix = f'{n_ann}{determine_number_suffix(n_ann)} ' if n_ann != '' else ''
        if 0 < time_to_next_ann.days < remind_after:
            result = {
                "description": f'{description_suffix}{description}',
                "due_in": str_fmt_days(time_to_next_ann)
            }
        else:
            result = None
        return result

    def handle_monthly(self, reminder):
        # Get day of month to remind
        day = reminder.get('day')
        remind_after = reminder.get('remind_after')
        description = reminder.get('description')

        if isinstance(day, int) is True:
            remind_date = datetime(
                year=self.now.year,
                month=self.now.month,
                day=day)
        elif day == 'last':
            last_day_of_month = calendar.monthrange(self.now.year, self.now.month)[1]
            remind_date = datetime(
                year=self.now.year,
                month=self.now.month,
                day=last_day_of_month,
                hour=23,
                minute=59)
        elif day == 'first':
            remind_date = datetime(
                year=self.now.year,
                month=self.now.month,
                day=1)

        days_to_remind = (remind_date - self.now)
        if 0 <= days_to_remind.days < remind_after:
            result = {
                "description": description,
                "due_in": str_fmt_days(days_to_remind)
            }
        else:
            result = None
        return result
    
    def handle_weekly(self, reminder):
        # Get day of week to remind
        day = reminder.get('day')
        remind_after = reminder.get('remind_after')
        description = reminder.get('description')

        remind_date = next_day_of_week(day, self.now)
        days_to_remind = (remind_date - self.now)

        if 0 < days_to_remind.days < remind_after:
            result = {
                "description": description,
                "due_in": str_fmt_days(days_to_remind)
            }
        else:
            result = None
        return result

    def handle_daily(self, reminder):
        # Get hour and minute of reminder
        hour = reminder.get('hour')
        minute = reminder.get('minute')
        description = reminder.get('description')

        remind_date = datetime(
            year=self.now.year,
            month=self.now.month,
            day=self.now.day,
            hour=hour,
            minute=minute)
        time_to_remind = (remind_date - self.now)
        result = {
            "description": description,
            "due_in": str_fmt_minutes(time_to_remind.seconds / 60)
        }
        return result
