from django.conf.urls import patterns, url

from face_match import views

urlpatterns = patterns('',
        url(r'^$', views.compare_faces, name='compare_face'),
)
