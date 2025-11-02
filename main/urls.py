from django.urls import path


from .views import *
urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('tasks/<int:pk>/edit/', TaskEditView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]