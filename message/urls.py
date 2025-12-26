from django.urls import path
from . import views

app_name = "message"
urlpatterns = [
        path("view_message/<int:friend_id>",views.chat_view,name="view_message"),
        
        ]

