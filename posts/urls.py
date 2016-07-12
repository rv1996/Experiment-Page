from django.conf.urls import url
from .views import list_view, detail_view, add_new, edit_post, delete_post

urlpatterns = [

    url(r'^$', list_view, name="list_view"),
    url(r'^add/$', add_new, name="add_new"),
    url(r'^(?P<slug>[\w-]+)/$', detail_view, name="detail_view"),
    url(r'^(?P<slug>[\w-]+)/edit/$', edit_post, name="edit_view"),
    url(r'^(?P<slug>[\w-]+)/delete/$', delete_post, name="delete_post"),


]
