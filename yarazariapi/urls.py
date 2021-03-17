
from django.contrib import admin
from django.urls import include,path
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/',include('mysite.urls')),
    path('Token/',include('Token.urls')),
    path('auth/', include('rest_framework.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('API.urls')),
    path('user/',include('User.urls')),
]
