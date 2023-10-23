from django.urls import path
from applications.taski.views import tasksView, createTasksView, detailTaskView,completeTaskView,deleteTaskView, completedTasksView

app_name = 'taskapp'

urlpatterns = [
    path('', tasksView, name='tasks'),
    path('completed/', completedTasksView, name='completed'),
    path('create/', createTasksView, name='create'),
    path('detail/<int:task_id>/', detailTaskView, name='detail'),
    path('complete/<int:task_id>/', completeTaskView, name='complete'),
    path('delete/<int:task_id>/', deleteTaskView, name='delete'),

]
