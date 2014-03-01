from django.conf.urls import patterns, url

urlpatterns = patterns('members.views',
    url(r'^$', 'index',
        name='members_index'),
    url(r'^login/$', 'login',
        name='members_login'),
    url(r'^logout/$', 'logout',
        name='members_logout'),
    url(r'^all/$', 'list_all',
        name='members_list_all'),
    url(r'^id/(?P<id>\d+)/$', 'get_member',
        name='members_get_member'),
    url(r'^forgot-password/$', 'forgot_password',
        name='members_forgot_password'),
    url(r'^reset-password/(?P<link>[-a-zA-Z0-9]{32})/$', 'reset_password',
        name='members_reset_password'),
    # url(r'^edit/$', 'edit_profile',
    #     name='members_edit'),

    # ispis crvenih za pozivnice
    url(r'^red/table/$', 'red_table',
        name='members_red_table'),
    url(r'^red/list/$', 'red_list',
        name='members_red_list'),
)
