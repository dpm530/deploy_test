from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^homePage$',views.homePage),
    url(r'^login$',views.login),
    url(r'^createWishListPage$',views.createWishListPage),
    url(r'^createNewListItem$',views.createNewListItem),
    url(r'^deleteItem/(?P<item_id>\d+)$',views.deleteItem),
    url(r'^listItem/(?P<id>\d+)$',views.listItem),

]
