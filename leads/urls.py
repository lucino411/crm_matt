from django.urls import path
from .views import (
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView,
    LeadAssignAgentView, CategoryListView, CategoryDetailView, LeadCategoryUpdateView,
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView
)
app_name = 'leads'

urlpatterns = [
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('', LeadListView.as_view(), name='leads_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/assign-agent/', LeadAssignAgentView.as_view(), name='lead_assign_agent'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(),
         name='lead-category-update'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(),
         name='category-detail'),
    path('categories/<int:pk>/update/',
         CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/',
         CategoryDeleteView.as_view(), name='category-delete'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
]