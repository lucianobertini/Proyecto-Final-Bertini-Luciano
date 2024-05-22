from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('send/', views.send_message, name='send_message'),
    path('reply/<int:message_id>/', views.reply_message, name='reply_message'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
]