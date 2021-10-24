from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^$', views.welcome, name='welcome'),
    url(r'^$',views.index,name='home'),
    path('comment/<int:id>/',views.comment,name='comment'),
    url(r'^singleproject/(\d+)',views.single_project,name='singleproject'),
    url(r'^newproject/$',views.Newproject,name='newproject'),
    path('rate/<int:id>/',views.rate,name='rates'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)