from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('global_question',views.global_question,name='global_question'),
    path('update_question/<int:id>',views.update_question,name='update_question'),
    path('create_question/',views.create_question,name='create_question'),
    path('each_question/<int:id>',views.each_question,name='each_question'),
    path('search_question/',views.search_question,name='search_question'),
    path('delete_question/<int:id>',views.delete_question,name='delete_question'),
    path('questions_show/',views.questions_show,name='questions_show'),
    path('votes_show/',views.votes_show,name='votes_show'),
    path('global_question_show/',views.global_question_show,name='global_question_show'),
    path('global_votes_show/',views.global_votes_show,name='global_votes_show'),
]