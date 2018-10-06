"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from utils.router import DefaultRouterWithAPIViews

admin.site.site_header = settings.ADMIN_SITE_HEADER

router = DefaultRouterWithAPIViews()


schema_view = get_schema_view(title=settings.API_BROWSER_HEADER, public=True)
doc_urls = include_docs_urls(title=settings.API_BROWSER_HEADER)
api_browser_urls = include('rest_framework.urls')
#auth_urls = include('auth.urls')

urlpatterns = [
    path('api/', doc_urls),
    #path('api/auth/', auth_urls),
    path('api/schema/', schema_view),
    path('api/browser/', api_browser_urls),
    path('api/admin/', admin.site.urls),
]

urlpatterns += router.urls
