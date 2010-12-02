from django.conf.urls.defaults import*
from server.views import ProdutoRest

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^produto/', ProdutoRest()),
)
