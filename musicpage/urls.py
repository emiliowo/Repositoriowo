from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('review/', views.ListaReviewVista.as_view(), name="review"),
    path('review/<pk>', views.ListaReviewVista.as_view(), name="review-detail"),


]

urlpatterns+=[
   
    path('review/create/', views.ReviewCreate.as_view(), name="review_create"),
    path('review/<pk>/delete/', views.ReviewDelete.as_view(), name="review_delete"),
    path('review/<pk>/update/', views.ReviewUpdate.as_view(), name="review_update"),
    path('templates/registration', include('django.contrib.auth.urls')),

]