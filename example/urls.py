from django.conf.urls import patterns, include

urlpatterns = patterns('',
    # Example:
    (r'^$', include('pastebin.urls'))
    # (r'^pastebin/', include('pastebin.foo.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
