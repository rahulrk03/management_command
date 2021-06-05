from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from sample.models import User_data, Activity_periods
# timezone, timedelta


class DataList(APIView):
    def get(self, request):
        try:
            users = User_data.objects.all()
            user_list = []
            for user in users:
                activityList = []
                activities = Activity_periods.objects.filter(user=user)
                for activity in activities:
                    activity_data = {
                        "start_time": activity.start_time,
                        "end_time": activity.end_time
                    }
                    activityList.append(activity_data)
                data = {
                    "id": user.id,
                    "real_name": user.real_name,
                    "tz": user.tz,
                    "activity_periods": activityList
                }
                user_list.append(data)
            response_data = {
                        "ok": True,
                        "members": user_list
            }
        except Exception as e:
            response_data = {
                        "ok": False,
                        "error_message": str(e)
            }
        return Response({"data": response_data,
                         "message": "Success",
                         "requestStatus": 1},
                        status=status.HTTP_200_OK)