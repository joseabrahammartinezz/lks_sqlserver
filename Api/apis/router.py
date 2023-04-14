from rest_framework.routers import DefaultRouter
from Api.apis.views import GestorBancoApiViewSet, PedidoMateriaisApiViewSet

router_banco= DefaultRouter()

router_banco.register(prefix='banco', base_name='banco', viewset=GestorBancoApiViewSet)
router_banco.register(prefix='pedido', base_name='pedido', viewset= PedidoMateriaisApiViewSet)
