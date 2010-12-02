from django.conf.urls.defaults import*
from server import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^produto/$', views.ProdutoView()),
    (r'^produto\.(?P<formato>\w+)/$', views.ProdutoView()),
    (r'^produto/(?P<codigo>\d+)/$', views.ProdutoView()),
    (r'^produto\.(?P<formato>\w+)/(?P<codigo>\d+)/$', views.ProdutoView()),
    (r'^admin/', include(admin.site.urls)),
)
