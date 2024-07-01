"""
URL configuration for personal_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from Contact.views import Contact
from Contact.views import ContactCreateView, ContactDeleteView, ContactUpdateView, create_Message
from Home.views import add_user,index
from projects.views import project_list, create_project, project_detail
from Resume.views  import resume , download_pdf, create_experience, create_certificates, create_education, create_skills, create_languages,Cdetail_view

urlpatterns = [
    path("contact/add", create_Message, name="contact-add"),
    path("contact/<int:pk>", ContactUpdateView.as_view(), name="contact-update"),
    path("contact/<int:pk>/delete", ContactDeleteView.as_view(), name="contact-delete"),
    
    path('', index, name='home'),
    path('index/add', add_user, name='add_user'),
   
    path('projects', project_list, name='project_list'),
    path('projects/add', create_project, name='create_project'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),

    path('resume', resume, name='resume'),
    path('pdf/<str:filename>/', download_pdf, name='download_pdf'),
    path('resume/experience/add', create_experience , name='create_experience'),
    path('resume/certificate/add', create_certificates , name='create_certificates'),
    path('resume/certificate/detail_view/<int:cer_id>/', Cdetail_view, name='Cdetail_view'),
    path('resume/education/add', create_education , name='create_education'),
    path('resume/skills/add', create_skills , name='create_skills'),
    path('resume/languages/add', create_languages , name='create_languages'),
    path('admin/', admin.site.urls),
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)