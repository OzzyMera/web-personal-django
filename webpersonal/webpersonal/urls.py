"""
URL configuration for webpersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core import views as core_views
from django.conf import settings 
from portfolio import views as portfolio_views
urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portafolio, name="portafolio"),
    path('contacto/', core_views.contacto, name="contacto"),
    path('nosotros/', core_views.nosotros, name="nosotros"), 
    path('anuncios/', core_views.anuncios, name="anuncios"), 
    path('post/', core_views.post, name="post"), 
    path('blog/', core_views.blog, name="blog"),
    path('entrada/', core_views.entrada, name="entrada"),
    path('gracias/', core_views.gracias, name="gracias"),                
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)