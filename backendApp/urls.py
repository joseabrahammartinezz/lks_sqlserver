"""backendApp URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path, include
from Api.apis.router import router_banco
from rest_framework import permissions
from django.conf import settings
from django.conf.urls import url
from Api.apis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include (router_banco.urls)),
    url(r'^pedidos$',views.PedidoMateriaisApi),
 #   url(r'^pedidos/([0-9]+)$',views.PedidoMateriaisApi), 
   # url(r'^pedidos/([0-9]+)/([0-9]+)/$',views.PedidoMateriaisBusquedaApi), 
   # path('pedidos/PEDIDO=<int:numpedido>&EMPRESA=<int:empresa>',views.PedidoMateriaisBusquedaApi), 
    url(r'^viewventas$/',views.ViewVentasApi),
   # url(r'^viewventas/([0-9]+)$',views.ViewVentasApi),   
    path('ventas/PEDIDO=<int:numpedido>&EMPRESA=<int:empresa>',views.ViewVentasBusqueddaApi),
    path('vfecha/FECHAINI=<fecha_ini>&FECHAFIN=<fecha_fin>&EMPRESA=<int:empresa>',views.ViewVfechasBusqueddaApi),
    #path('facturas/', include ('factura.urls')),
]
