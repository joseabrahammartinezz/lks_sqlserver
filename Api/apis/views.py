from rest_framework.viewsets import ModelViewSet
from Api.models import Gestor_Banco, Pedido_Materiais
from Api.apis.serializers import GestorBancoSerializer, PedidoMateriaisSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


class GestorBancoApiViewSet(ModelViewSet):
    serializer_class = GestorBancoSerializer
    queryset = Gestor_Banco.objects.all()

class PedidoMateriaisApiViewSet(ModelViewSet):
    serializer_class =  PedidoMateriaisSerializer
    queryset = Pedido_Materiais.objects.all()

@csrf_exempt
def PedidoMateriaisApi(request,id=0):
    if request.method=='GET':
        pedidos = Pedido_Materiais.objects.all()
        pedidos_serializer = PedidoMateriaisSerializer(pedidos, many=True)
        return JsonResponse(pedidos_serializer.data, safe=False)
    elif request.method=='POST':
        pedidos_data=JSONParser().parse(request)
        pedidos_serializer=PedidoMateriaisSerializer(data=pedidos_data)
        if pedidos_serializer.is_valid():
            pedidos_serializer.save()
            return JsonResponse("Adicion  Exitosa", safe=False)
        return JsonResponse("Adicion  Fallida", safe=False)
    elif request.method=='PUT':
        pedidos_data=JSONParser().parse(request)
        pedido=Pedido_Materiais.objects.get(PEDIDO=pedidos_data['PEDIDO'])
        pedidos_serializer=PedidoMateriaisSerializer(pedido,data=pedidos_data)
        if pedidos_serializer.is_valid():
            pedidos_serializer.save()
            return JsonResponse("Actualizacion  Exitosa", safe=False)
        return JsonResponse("Actualizacion  Fallida", safe=False)
    elif request.method=='DELETE':
        pedido=Pedido_Materiais.objects.get(PEDIDO=id)
        pedido.delete()
        return JsonResponse("Eliminacion exitosa", safe=False)
    