from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.ListBlog.as_view()),
    path('<int:pk>/', views.DetailBlog.as_view()),
    path('fm/', views.ListFM.as_view()),
    path('<int:pk>/', views.DetailFM.as_view()),
]
