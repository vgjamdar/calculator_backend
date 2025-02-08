from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CalculatorView

router = DefaultRouter(trailing_slash=False)
urlpatterns = router.urls

urlpatterns.append(path(r'calculator', CalculatorView.as_view(), name='calculator'))
