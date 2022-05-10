"""
Object definition for the reminder
"""
from datetime import datetime

from src.utils import read_config, read_reminder_list, round_up, determine_number_suffix


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
            if reminder_type == 'anniversary':
                result = self.handle_anniversary(reminder)
                if result is not None:
                    due_reminders.append(result)
        return due_reminders

    def handle_anniversary(self, reminder):
        # Get date of anniversary
        year = reminder.get('year')
        month = reminder.get('month')
        day = reminder.get('day')
        remind_after = reminder.get('remind_after')
        description = reminder.get('description')

        ann_date = datetime(year=year, month=month, day=day)
        time_to_ann = self.now - ann_date
        days_to_ann = (datetime(year=self.now.year, month=month, day=day) - self.now)
        n_ann = round_up(time_to_ann.days/365)
        if days_to_ann.days < remind_after:
            result = {
                "description": f'{n_ann}{determine_number_suffix(n_ann)} {description}',
                "due_in": days_to_ann
            }
        else:
            result = None
        return result
