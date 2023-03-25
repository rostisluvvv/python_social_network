from django.urls import include, path

from . import views

urlpatterns = [
    # path('post/<int:pk>/', views.PostView.as_view(
    #     {'put': 'update',
    #      'get': 'retrieve',
    #      'delete': 'destroy'}
    # )),
    path('', views.FeedView.as_view({'get': 'list'}))
]
