from django.urls import path

from pages.views import *


urlpatterns = [

    path("", project_index, name="project_index"),

    #path("<int:pk>/", project_detail, name="project_detail"),

]