from rest_framework.routers import DefaultRouter
from Api.apis.views import GestorBancoApiViewSet, PedidoMateriaisApiViewSet

router_banco= DefaultRouter()

router_banco.register(prefix='banco', basename='banco', viewset=GestorBancoApiViewSet)
router_banco.register(prefix='pedido', basename='pedido', viewset= PedidoMateriaisApiViewSet)