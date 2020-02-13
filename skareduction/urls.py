"""skareduction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from skar.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^about-us/$', about_us, name='about-us'),
    url(r'^blog/$', blog, name='blog'),
    url(r'^faq/$', faq, name='faq'),
    url(r'^team/$', team, name='team'),
    url(r'^careers/$', careers, name='careers'),
    url(r'^contact-us/$', contact_us, name='contact-us'),
    url(r'^tutor/(?P<slug>[\w-]+)/$', tutor_content, name='tutor_content'),
    url(r'^student/(?P<slug>[\w-]+)/$', student_content, name='student_content'),
    url(r'^register-student/$', register_student, name='register_student'),
    url(r'^register-tutor/$', register_tutor, name='register_tutor'),
]
