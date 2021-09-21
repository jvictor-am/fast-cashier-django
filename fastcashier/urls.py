"""fastcashier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# django imports
from django.contrib import admin
from django.urls import path, include

# trhid party imports
from rest_framework import routers

# local imports
from sales import views


router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet, 'product')
router.register(r'customer', views.CustomerViewSet, 'customer')
router.register(r'seller', views.SellerViewSet, 'seller')
router.register(r'order', views.OrderViewSet, 'order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
