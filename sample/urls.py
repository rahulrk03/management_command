from django.urls import path
from .views import (DataList)

urlpatterns = [
    path('dataList/', DataList.as_view(), name="dataList")
]
