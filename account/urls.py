from django.conf.urls import include, re_path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter(trailing_slash=False)
router.register('accounts',UserV1,basename='account')

urlpatterns = [
    re_path('',include((router.urls,'accounts'),namespace='V1')),
]
