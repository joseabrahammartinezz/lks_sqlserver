from rest_framework.serializers import ModelSerializer
from Api.models import Gestor_Banco, Pedido_Materiais

class GestorBancoSerializer(ModelSerializer):
    class Meta:
        model = Gestor_Banco
        fields = ['GESTOR_BANCO','Codigo_Banco', 'Descricao']

class PedidoMateriaisSerializer(ModelSerializer):
    class Meta:
        model = Pedido_Materiais
        fields = '__all__'