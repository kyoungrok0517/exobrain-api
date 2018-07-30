from django.conf.urls import url
from kcg import views

urlpatterns = [
    url(r'^kcg/$', views.triple_list)
]
