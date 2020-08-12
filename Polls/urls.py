from django.urls import path
from .views import home,create_question,create_option,vote_page,results,vote_function,index
urlpatterns = [
    path('addPoll/',create_question,name='create-question'),
    path('addPoll/<int:poll_id>',create_option,name='create-option'),
    path('home/',home,name="home"),
    path('', index, name="index"),
    path('poll/<int:poll_id>',vote_page,name='vote-page'),
    path('poll/<int:poll_id>/results',results,name='results'),
    path('poll/<int:poll_id>/vote',vote_function,name='vote-function')
]
