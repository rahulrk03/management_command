from django.core.management.base import BaseCommand
import json
from sample.models import User_data, Activity_periods


class Command(BaseCommand):
    def handle(self, **options):
        self.readAs()

    def readAs(self):
        jsonFile = open('Test_JSON.json')
        data = json.load(jsonFile)
        user_list = []
        activity_list = []
        for member in data['members']:
            user_created = User_data(id=member['id'],
                                     real_name=member['real_name'],
                                     tz=member['tz'])
            user_list.append(user_created)
            for activity in member['activity_periods']:
                activity_created = Activity_periods(user=user_created,
                                                    start_time=activity['start_time'],
                                                    end_time=activity['start_time'])
                activity_list.append(activity_created)
        try:
            User_data.objects.bulk_create(user_list)
            Activity_periods.objects.bulk_create(activity_list)
        except Exception:
            pass

        jsonFile.close()
