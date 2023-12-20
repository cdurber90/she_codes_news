from django.urls import path
from . import views
# from .views import IndexView, StoryView, AddStoryView, UpdateStoryView, DeleteStoryView

app_name = 'news'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index')
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('edit/<int:pk>', views.UpdateStoryView.as_view(), name='update_story'),
    path('edit/<int:pk>/delete', views.DeleteStoryView.as_view(), name='delete_story'),
    # path('<int:pk>/comments/', views.AddCommentsView.as_view(), name='addComment'),
]
