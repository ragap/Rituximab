from django.conf.urls import url,include
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success/$', views.success, name='success'),
    url(r'^export/$', views.export_csv, name='export_csv'),


   # Login & Log out urls
    url(r'^login/$',auth_views.login, {'template_name':'login.html'},name = 'login'),
    url(r'^logout/$',auth_views.logout,{'template_name':'logout.html'},name = 'logout'),

    #/rtx/hospital/
    url(r'^hospital/$',views.hospital, name='hospital'),
    # url(r'^hospital/search/$', views.hospitalsearch, name='search'),
    url(r'^hospital/add/$',views.hospitaladd, name='add_hospital'),
    url(r'^hospital/(?P<pk>[0-9]+)/edit/$',views.hospitaledit,{},name='edit_hospital'),
    url(r'^hospital/(?P<pk>[0-9]+)/delete/$',views.Hospitaldelete.as_view(),name='del_hospital'),

    #/rtx/doctor/
    url(r'^doctor/$', views.doctor, name='doctor'),
    url(r'^doctor/add/$', views.doctoradd, name='add_doctor'),
    url(r'^doctor/(?P<pk>[0-9]+)/edit/$', views.doctoredit, name='edit_doctor'),
    url(r'^doctor/(?P<pk>[0-9]+)/delete/$', views.doctordelete.as_view(), name='del_doctor'),

    #/rtx/patient/
    url(r'^patient/$', views.patient, name='patient'),
    url(r'^patient/search/$', views.patientsearch, name='search_patient'),
    url(r'^patient/add/$', views.patientadd, name='add_patient'),
    url(r'^patient/(?P<pk>[0-9]+)/edit/$', views.patientedit, name='edit_patient'),
    url(r'^patient/(?P<pk>[0-9]+)/delete/$', views.patientdelete.as_view(), name='del_patient'),

    #/rtx/RTXinfusionForm
    url(r'^patient/infusion/(?P<pk>[0-9]+)/$', views.infusion, name='infusion'),
    url(r'^patient/infusion/(?P<pk>[0-9]+)/add/$', views.infusionadd, name='add_infusion'),
    url(r'^patient/infusion/(?P<pk>[0-9]+)/edit/$', views.infusionedit, name='edit_infusion'),
    url(r'^patient/infusion/(?P<pk>[0-9]+)/delete/$', views.infusiondelete.as_view(), name='del_infusion'),

    #/rtx/RTXinfusionForm/followup
    url(r'^patient/infusion/(?P<pk>[0-9]+)/results/$', views.results, name='test_results'),
    url(r'^patient/infusion/(?P<pk>[0-9]+)/results/add/$', views.addresults, name='results_add'),
    url(r'^patient/infusion/(?P<pk>[0-9]+)/results/edit/$', views.editresults, name='edit_results'),
    url(r'^patient/infusion/(?P<pk>[0-9]+)/results/delete/$', views.resultsdelete.as_view(), name='del_results'),
    ]
