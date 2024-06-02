from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.user_login, name='login'),
    path('home/',views.home, name='home'),
    path('raise_rfc/',views.Raise_Rfc, name='raise_rfc'),
    path('rejected_rfc/',views.Rejected_Rfc, name='rejected_rfc'),
    path('rollback_rfc/',views.Rollback_Rfc, name='rollback_rfc'),
    path('my_rfc/',views.My_Rfc, name='my_rfc'),
    path('rfc_details/<int:pk>',views.Rfc_details, name='rfc_details'),
    path('cp/',views.Change_Password,name='cp'),
    path('opened_rfc/',views.Opened_rfc, name='opened_rfc'),
    path('closed_rfc/',views.Closed_rfc, name='closed_rfc'),
]