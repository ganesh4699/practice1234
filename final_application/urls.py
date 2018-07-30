from django.conf.urls import url
from final_application import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
]