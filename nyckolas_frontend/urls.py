from django.urls import path
from . import views as frontend_views

urlpatterns = [
    path('', frontend_views.Index.as_view(), name='frontend_index'),
    path('report/', frontend_views.Report.as_view(), name='report'),
    path('login/', frontend_views.LoginExample.as_view(), name='login'),
    path('accounts/profile/', frontend_views.ListExample.as_view(), name='all_user'),
    path('detail/<pk>/', frontend_views.DetailViewExample.as_view(), name='detail'),
    path('detail-date/<year>/<month>/<day>/<pk>',
         frontend_views.DateDetailViewExample.as_view(), name='detail_date'),
    path('week-archive/<week>/',
         frontend_views.WeekArchiveViewExample.as_view(), name='week_archive'),
    path('create/', frontend_views.CreateViewExample.as_view(), name='create'),
    path('delete/<pk>/', frontend_views.DeleteExample.as_view(), name='delete'),
    path('update/<pk>/', frontend_views.UpdateExample.as_view(), name='update'),
]
