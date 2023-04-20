from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Api.models import Gestor_Banco, Pedido_Materiais, VIEW_VENTAS, VIEW_MASTER, VIEW_DETAIL

class GestorBancoSerializer(ModelSerializer):
    class Meta:
        model = Gestor_Banco
        fields = ['GESTOR_BANCO','Codigo_Banco', 'Descricao']

class PedidoMateriaisSerializer(ModelSerializer):
    class Meta:
        model = Pedido_Materiais
        fields = '__all__'

class ViewVentasSerializer(ModelSerializer):
    class Meta:
        model = VIEW_VENTAS
        fields = '__all__'

class ViewMasterSerializer(ModelSerializer):
    class Meta:
        model = VIEW_MASTER
        fields = '__all__'

class ViewDetailSerializer(ModelSerializer):
    class Meta:
        model = VIEW_DETAIL
        fields = '__all__'

class DatosFacturaSerializer(serializers.Serializer):
    cabecera = ViewMasterSerializer(many=True)
    detalle = ViewDetailSerializer (many=True)
