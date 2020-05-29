# encoding: utf-8
from django.conf.urls import url

from haystack.views import SearchView

urlpatterns = [
    url(r"^$", SearchView(), name="haystack_search"),
    url(r"^discussion/$", discussionSearchView(), name="haystack_search_1"),
            ]
