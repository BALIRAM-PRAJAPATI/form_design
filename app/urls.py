from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.user_dashboard, name='dashboard'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('incident/', views.incident, name = 'incident_report')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
