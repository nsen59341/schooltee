from django.urls import path
from .views import home, loginuser, registrationuser, logoutuser, assignment, check_ans, check_sess, stote_points

urlpatterns = [

    path('', home, name="home"),

    path('assignment/<int:assid>', assignment, name="assignment"),

    path('check_ans', check_ans, name="check_ans"),

    path('check_sess', check_sess, name="check_sess"),

    path('stote_points', stote_points, name="stote_points"),

    path('login', loginuser, name="login"),
    path('registration', registrationuser, name="registration"),
    path('logout', logoutuser, name="logout"),

]