from django.conf.urls import url, include
from django.contrib import admin
from apps.channelmanager import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'channels', views.ChannelViewSet, base_name='channels-api')
router.register(r'categories', views.CategoryViewSet,
                base_name='categories-api')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
