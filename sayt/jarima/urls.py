from django.urls import path, include

from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name='home'),
    path('success', success, name='success'),
    path('forma', forma, name='forma'),
    path('forma/<int:pk>/', update, name='update'),
    path('upload/', upload_file, name='upload_file'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('login/', login_view, name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('xisobot/<int:ids>/', view_xisobot, name='view_xisobot'),
    # path('xisobot/<int:xisobot>/<int:davr>/', view_satrlar, name='satrlar'),
    # path('signup/', signup, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
