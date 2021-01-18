from django.urls import path
from .views import *
import app.signals

app_name = 'app'

urlpatterns = [
    path('', DataSchemaListView.as_view(), name='list'),
    path('create/', DataSchemaCreateView.as_view(), name='create'),
    path('<int:pk>/', DataSchemaDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', DataSchemaUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DataSchemaDeleteView.as_view(), name='delete'),
]
