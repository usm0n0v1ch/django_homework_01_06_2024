from django.urls import re_path

from todolist_app import views

urlpatterns = [
    re_path(r'^$', views.task_list, name='task_list'),
    # Отображает список всех задач. Главная страница приложения.

    re_path(r'^create/$', views.task_create, name='task_create'),
    # Предоставляет форму для создания новой задачи.

    re_path(r'^update/(?P<pk>\d+)/$', views.task_update, name='task_update'),
    # Позволяет изменять существующую задачу. В `pk` передается id задачи для редактирования.

    re_path(r'^delete/(?P<pk>\d+)/$', views.task_delete, name='task_delete'),
    # Отображает страницу подтверждения удаления задачи. В `pk` передается id задачи для удаления.
]
