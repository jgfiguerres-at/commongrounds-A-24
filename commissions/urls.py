from django.urls import path

from .views import *

urlpatterns = [
    path('requests', CommissionListView.as_view(),
         name="commission_list"),
    path('request/<int:pk>', CommissionDetailView.as_view(),
         name="commission_detail"),
    path('request/add', CommissionCreateView.as_view(),
         name="commission_add"),
    path('request/<int:pk>/edit', CommissionUpdateView.as_view(),
         name="commission_edit"),
    path('job/<int:pk>/apply', ApplyToJobView.as_view(),
         name="job_apply"),
]

app_name = 'commissions'
