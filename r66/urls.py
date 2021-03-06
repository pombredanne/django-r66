from django.conf.urls.defaults import *

urlpatterns = patterns('r66.views',
    (r'^logout/$',
        'logout_user',
        None, 'r66-logout'),

    (r'^$',
        'index',
        None, 'r66'),
    (r'^$/',
        'index',
        None, 'r66-root'),
    (r'^index.html$',
        'index',
        None, 'r66-index'),

    (r'^success.html$',
        'success',
        None, 'r66-success'),

    (r'^home/(?P<page_id>[\w_-]+).html$',
        'home',
        None, 'r66-home'),
    (r'^bridges/index.html$',
        'bridges',
        None, 'r66-bridges'),
    (r'^interfaces/index.html$',
        'interfaces_index',
        None, 'r66-interfaces-index'),
    (r'^interfaces/new.html$',
        'interfaces_new',
        None, 'r66-interfaces-new'),
    (r'^interfaces/$',
        'interfaces',
        None, 'r66-interfaces'),
    (r'^interfaces/(?P<profile_id>\d+)$',
        'interfaces',
        None, 'r66-interfaces-profile'),

    (r'^cifs/index.html$',
        'cifs',
        None, 'r66-cifs-index'),

    (r'^cifs/$',
        'cifs',
        None, 'r66-cifs'),





)
