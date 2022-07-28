from django.urls import path

from . import views

# from .models import ToDoList, Item

urlpatterns = [
path("",views.index,name =  "index"),
path("151",views.id_last,name =  "id_last"),
path("<int:id>",views.id,name =  "id"),
path("feedback/<int:id>",views.feedback,name =  "feedback"),

]