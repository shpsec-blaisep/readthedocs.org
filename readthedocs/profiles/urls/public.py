from django.conf.urls import patterns, url

from readthedocs.profiles import views


urlpatterns = patterns('',
                       url(r'^(?P<username>[\w@.-]+)/$',
                           views.profile_detail,
                           {'template_name': 'profiles/public/profile_detail.html'},
                           name='profiles_profile_detail'),
                       )
