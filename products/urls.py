from django.urls import path
from .views import PostView,CategoryView,ProductView,DetailsView,UpdateView


urlpatterns = [
    path('',CategoryView,name='category'),
    path('product/<int:pk>/',ProductView,name='product'),
    path('details/<int:pk>', DetailsView, name='details'),
    path('post', PostView, name='post'),
    path('update/<int:pk>', UpdateView, name='update')

]