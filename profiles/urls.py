from django.conf.urls import url
from .views import (
    MasterListView,
    ParticipantListView,
    MasterDetailView,
    ParticipantDetailView,
    ParticipantCreateView,
    MasterCreateView,
    ParticipantDeleteView,
    MasterDeleteView,
    MasterUpdateView,
    ParticipantUpdateView,
)


urlpatterns = [
    url(r'^members/$', ParticipantListView.as_view(), name="member_list"),
    url(r'^masters/$', MasterListView.as_view(), name="master_list"),
    url(r'^members/(?P<pk>\d+)/$', ParticipantDetailView.as_view(), name='member_detail'),
    url(r'^masters/(?P<pk>\d+)/$', MasterDetailView.as_view(), name='master_detail'),
    url(r'^members/add/$', ParticipantCreateView.as_view(), name="member_create"),
    url(r'^masters/add/$', MasterCreateView.as_view(), name="master_create"),
    url(r'^members/(?P<pk>\d+)/delete/$', ParticipantDeleteView.as_view(), name='member_delete'),
    url(r'^masters/(?P<pk>\d+)/delete/$', MasterDeleteView.as_view(), name='master_delete'),
    url(r'^members/(?P<pk>\d+)/edit/$', ParticipantUpdateView.as_view(), name='member_update'),
    url(r'^masters/(?P<pk>\d+)/edit/$', MasterUpdateView.as_view(), name='master_update'),
]