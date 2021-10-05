from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('rec/',views.index,name = 'FIRSTPAGE'),
    path('logincheck/',views.logincheck,name = 'logincheck'),
    url(r'^logincheck/RecommendLectures/$',views.RecommendLecture,name = 'RecommendLecture')
]