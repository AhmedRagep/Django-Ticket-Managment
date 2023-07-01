from django.urls import path
from . import views


urlpatterns = [
    path('ticket_detail/<int:pk>', views.ticket_detail ,name='ticket_detial'),
    path('create_ticket', views.create_ticket ,name='create_ticket'),
    path('update_ticket/<int:pk>', views.update_ticket ,name='update_ticket'),
    path('all_tickets', views.all_tickets ,name='all_tickets'),
    path('ticket_queue', views.ticket_queue ,name='ticket_queue'),
    path('accept_ticket/<int:pk>', views.accept_ticket ,name='accept_ticket'),
    path('closed_ticket/<int:pk>', views.closed_ticket ,name='closed_ticket'),
    path('workspace', views.workspace ,name='workspace'),
    path('all_closed_tickets', views.all_closed_tickets ,name='all_closed_tickets'),

]
