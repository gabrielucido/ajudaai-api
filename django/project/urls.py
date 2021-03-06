from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from users.viewsets import CreateAnonUser

from issues.viewsets import IssueViewSet
from comments.viewsets import CommentaryViewSet  # pylint: disable=unused-import

router = routers.DefaultRouter()
router.register(r'issues', IssueViewSet, basename='issue')
router.register(r'token-anon', CreateAnonUser, basename='token-anon')
# router.register(r'comments', CommentaryViewSet, basename='commentary')

urlpatterns = [
    path('ajudaai/v1/', include('users.urls')),
    path('ajudaai/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('openapi/',
                         get_schema_view(title="My Project Api",
                                         description="API for My Project.",
                                         version="1.0.0"
                                         ),
                         name='openapi-schema'),
                    path('',
                         TemplateView.as_view(template_name='swagger-ui.html',
                                              extra_context={
                                                  'schema_url': 'openapi-schema'}
                                              ), name='swagger-ui')]
