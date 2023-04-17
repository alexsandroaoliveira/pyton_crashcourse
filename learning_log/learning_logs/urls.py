"""Defines URL patterns for learning_logs."""

from django.urls import path, re_path

from . import views

urlpatterns  = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
