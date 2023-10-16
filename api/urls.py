from home.views import TaskViewSet
from home2.views import HomeworkViewSet
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'student', TaskViewSet, basename='student')
router.register(r'homework', HomeworkViewSet, basename='homework')
# urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls))
    # path('api/student/', include('home.urls')),
    # path('api/homework/', include('home2.urls')),
]
