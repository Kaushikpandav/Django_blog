from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router  = DefaultRouter()

router.register('employees', views.EmployeeViewSet, basename='employees') # basedname only when used viewset.Viewset. not need while it Modelviewsets | also not need to create a multi path for 'pk' or without 'pk' based operations

urlpatterns = [

    #students
    path('students/', views.StudentViews),
    path('students/<int:pk>/', views.Studentdetailsview),
    
    #employees | for mixins, generics and class based views
    # path('employees/', views.EmployeeViews.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetailsView.as_view())

    #viewset
    path('', include(router.urls)),

    #blogs
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailsView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailsView.as_view()),


]
