"""tibbles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tibblesapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('dashboard/', home),
    path('about/', about),
    path('', myhome),
    path('main/', myhome),
    path('signin/', signin),
    path('signout/', signout),
    path('signup/', signup),
    path('prefsub/', sub_pref),
    path('prefslot/', slot_pref),
    path('timetable/', display),
    path('pdf/', GeneratePdf.as_view(), name="pdf_view"),
    path('export/', export_to_excel, name="export_to_excel"),
    path('slotp/', slotp),
    path('subp/', subp),
    path('faculty/', viewfac),
    path('delfac/<int:faculty_id>/', delfac, name='delfac'),
    path('subject/', viewsub),
    path('addsub/', addsub),
    path('delsub/<str:subject_code>/', delsub, name='delsub'),
    path('delslotpref/<str:faculty_id>/<str:day>/<int:slot>/',delete_slotentry, name='delslotpref'),
    path('viewslotpref/', view_slotentry),
    path('delsubpref/', delete_subentry),
    path('viewsubpref/', view_subentry),
    path('updatesub/', updatesub),
]
