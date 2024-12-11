"""
URL configuration for childcareedu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ChildCare import views as c_views
from . import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line for the Django admin site
    path('', c_views.Home, name='home'),
    path('Parents/', c_views.parents, name='parents'),
    path('Child/', c_views.child, name='child'),


    path('child/', c_views.child_list, name='child_list'),  # List view
    path('child/create/', c_views.child_create, name='child_create'),  # Create view
    path('child/update/<int:child_id>/', c_views.child_update, name='child_update'),  # Update view
    path('child/delete/<int:child_id>/', c_views.child_delete, name='child_delete'),

    path('Doctor/', c_views.doctor, name='doctor'),
    path('Consultation/', c_views.consultation, name='consultation'),

    path('consultation/', c_views.consultation_list, name='consultation_list'),
    path('consultation/create/', c_views.consultation_create, name='consultation_create'),
    path('consultation/update/<int:consultation_id>/', c_views.consultation_update, name='consultation_update'),
    path('consultation/delete/<int:consultation_id>/', c_views.consultation_delete, name='consultation_delete'),
    path('HealthInfo/', c_views.healthInfo, name='healthinfo'),

    path('healthinfo/', c_views.healthinfo_list, name='healthinfo_list'),
    path('healthinfo/create/', c_views.healthinfo_create, name='healthinfo_create'),
    path('healthinfo/update/<int:healthinfo_id>/', c_views.healthinfo_update, name='healthinfo_update'),
    path('healthinfo/delete/<int:healthinfo_id>/', c_views.healthinfo_delete, name='healthinfo_delete'),

    path('Schedule/', c_views.schedule, name='schedule'),
    path('LearningPlan/', c_views.learningPlan, name='learningPlan'),
    path('child/certificate/<int:child_id>/', c_views.view_certificate, name='view_certificate'),
    path('login/', c_views.login_view, name='login'),
    path('signup/', c_views.signup, name='signup'),
    path('logout/', c_views.logout_view, name='logout'),
    path('child/certificate/<int:child_id>/', c_views.view_certificate, name='view_certificate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
