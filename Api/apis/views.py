from rest_framework.viewsets import ModelViewSet
from Api.models import Gestor_Banco, Pedido_Materiais, VIEW_VENTAS, VIEW_MASTER, VIEW_DETAIL
from Api.apis.serializers import GestorBancoSerializer, PedidoMateriaisSerializer, ViewVentasSerializer, DatosFacturaSerializer, ViewMasterSerializer, ViewDetailSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from datetime import  datetime

class GestorBancoApiViewSet(ModelViewSet):
    serializer_class = GestorBancoSerializer
    queryset = Gestor_Banco.objects.all()

class PedidoMateriaisApiViewSet(ModelViewSet):
    serializer_class =  PedidoMateriaisSerializer
    queryset = Pedido_Materiais.objects.all()

@csrf_exempt
def PedidoMateriaisApi(request,id=0):
    if request.method=='GET':
        pedidos = Pedido_Materiais.objects.all()[:10]
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
    
@csrf_exempt
def PedidoMateriaisBusquedaApi(request, numpedido, empresa):
    if request.method=='GET':
        print (numpedido)
        print ( empresa)
        pedidos = Pedido_Materiais.objects.filter(PEDIDO=numpedido, EMPRESA=empresa)[:10]
        pedidos_serializer = PedidoMateriaisSerializer(pedidos, many=True)
        return JsonResponse(pedidos_serializer.data, safe=False)
    
@csrf_exempt
def ViewVentasApi(request,id=0):
    if request.method=='GET':
        pedidos = VIEW_VENTAS.objects.all()[:10]
        pedidos_serializer = ViewVentasSerializer(pedidos, many=True)
        return JsonResponse(pedidos_serializer.data, safe=False)
    
@csrf_exempt
def ViewVentasBusqueddaApi(request, numpedido, empresa):
    if request.method=='GET':
        print (numpedido)
        print ( empresa)
        master_info = VIEW_MASTER.objects.filter(PEDIDO=numpedido, EMPRESA=empresa)[:10]

        detail_info = VIEW_DETAIL.objects.filter(PEDIDO=numpedido, EMPRESA=empresa)[:10]

        return JsonResponse(
            DatosFacturaSerializer({
                "cabecera" : master_info,
                "detalle" : detail_info,
            }).data, safe = False, status=200,
        )
    
@csrf_exempt
def ViewVfechasBusqueddaApi(request, fecha_ini, fecha_fin, empresa):
    if request.method=='GET':
        fecha_ini =  fecha_ini + ' 00:00:00'
        fecha_fin =  fecha_fin + ' 23:59:59'
        formatting = "%Y-%m-%d %H:%M:%S"
        startdate = datetime.strptime(fecha_ini, formatting)
        enddate = datetime.strptime(fecha_fin, formatting)
#       print(datetime.strptime(string, formatting))
        print (enddate)

        master_info = VIEW_MASTER.objects.filter(DATA__range=(startdate,enddate))
#        detail_info = ''
        return JsonResponse(
            DatosFacturaSerializer({
                "cabecera" : master_info,
                "detalle" : '',
            }).data, safe = False, status=200,
        )
