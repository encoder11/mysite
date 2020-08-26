from django.urls import path
from . import views

#해당 앱에 있는 views파일 안의 index함수를 호출하는 코드
urlpatterns = [
    path('', views.index, name='index'),
]