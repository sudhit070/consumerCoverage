from django.urls import include, path
from rest_framework import routers
from App_User import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.home),
    path('addStudent', views.post_student),
    path('updateStudent/<userid>', views.update_student),
    path('deleteStudent/<userid>', views.delete_student),
    path('getBooks', views.get_book),
    path('student', views.StudentAPI.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]