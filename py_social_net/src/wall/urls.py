from django.urls import path

from . import views



urlpatterns = [
    path('comment/<int:pk>', views.CommentsView.as_view(
        {'put': 'update',
         'delete': 'destroy',
         'post': 'create'}
    )),

    path('post/<int:pk>/', views.PostView.as_view(
        {'put': 'update',
         'get': 'retrieve',
         'delete': 'destroy',
         'post': 'create'}
    )),

    path('<int:pk>/', views.PostListView.as_view()),

]