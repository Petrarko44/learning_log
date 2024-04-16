'''определяет схемы URL для learning_logs'''
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    #home page
    path('',views.index, name='index'),
    #page with list of topics
    path('topics/', views.topics, name='topics'),
    #topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for input user new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #page to input new entries about topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #page for edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]