from django.db import models

# Create your models here.
class Gestor_Banco(models.Model):
    GESTOR_BANCO = models.IntegerField (primary_key= True, unique=True)
    Codigo_Banco = models.CharField(max_length=255)
    Descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'GESTOR_BANCO'

class Pedido_Materiais(models.Model):
    PEDIDO = models.IntegerField (primary_key= True)
    EMPRESA = models.IntegerField ()
    COTACAO = models.IntegerField()
    DATA = models.DateTimeField()
    DTFECHAMENTO = models.DateTimeField()
    DTENTREGA = models.DateTimeField()
    FORNECEDOR = models.IntegerField()
    CLIENTE = models.IntegerField()
    TIPO = models.CharField(max_length=15)
    CENTRO_CUSTO = models.IntegerField()
    SETOR = models.IntegerField()
    CATEG = models.CharField(max_length=5)
    CLASS = models.CharField(max_length=5)
    CLASSE = models.IntegerField()
    TPCOMPRA = models.IntegerField()
    FPGTOID = models.IntegerField()
    FPGTO = models.CharField(max_length=30)
    PRAZO_ENTREGA = models.CharField(max_length=30)
    VENDEDOR_ID = models.IntegerField()
    VENDEDOR = models.CharField(max_length=30)
    AOSCUIDADOS = models.CharField(max_length=30)
    SEUPEDIDO = models.CharField(max_length=30)
    QUANT_ITENS = models.FloatField()
    VLRFRETE = models.FloatField()
    TOTAL_PRODUTOS = models.FloatField()
    TOTAL_PRODUTOS_IPI = models.FloatField()
    TOTAL_SUBSTITUICAO = models.FloatField()
    TOTAL_PEDIDO = models.FloatField()
    URGENCIA = models.CharField(max_length=10)
    NF = models.IntegerField()
    POSICAO = models.CharField(max_length=15)
    POSICAOENT = models.CharField(max_length=15)
    POSICAOESPERA = models.CharField(max_length=15)
    OBS = models.TextField()
    PA = models.IntegerField()
    STATUS = models.CharField(max_length=30)
    PCP = models.IntegerField()
    APROVACAO = models.IntegerField()
    FIN = models.CharField(max_length=2)
    PAFIN = models.IntegerField()

    class Meta:
        unique_together = (('PEDIDO', 'EMPRESA'),)
    
    class Meta:
        managed = False
        db_table = 'PEDIDO_MATERIAIS'

class VIEW_VENTAS(models.Model):
    PEDIDO = models.IntegerField (primary_key= True)
    EMPRESA = models.IntegerField ()
    RAZAO_SOCIAL = models.CharField(max_length=100)
    NOME = models.CharField(max_length=100)
    DATA = models.DateTimeField()
    VENDEDOR = models.CharField(max_length=30)
    TOTAL_PAGO = models.FloatField()
    TOTAL_PEDIDO = models.FloatField()
    OBS = models.TextField()
    POSICAO = models.CharField(max_length=15)
    DTFECHAMENTO = models.DateTimeField()
    TOTAL_PRODUTOS = models.FloatField()
    AUTOID = models.IntegerField()
    CODID = models.IntegerField()
    COD_INTERNO = models.CharField(max_length=30)
    COD_PEDIDO = models.CharField(max_length=30)
    DESCRICAOPROD = models.CharField(max_length=70)
    QUANT = models.FloatField()
    VLR_GARANTIA = models.FloatField()
    VLR_CUSTO = models.FloatField()
    VLR_UNIT = models.FloatField()
    VLR_TABELA = models.FloatField()
    VLR_TOTAL = models.FloatField()

    class Meta:
        unique_together = (('PEDIDO', 'EMPRESA'),)
    
    class Meta:
        managed = False
        db_table = 'VIEW_VENTAS'    

class VIEW_MASTER(models.Model):
    PEDIDO = models.IntegerField (primary_key= True)
    EMPRESA = models.IntegerField ()
    RAZAO_SOCIAL = models.CharField(max_length=100)
    COD_CLIENTE = models.IntegerField ()
    RG_INSC = models.CharField(max_length=25)
    NOME = models.CharField(max_length=100)
    EMAIL = models.CharField(max_length=60)
    DATA = models.DateTimeField()
    VENDEDOR = models.CharField(max_length=30)
    TOTAL_PAGO = models.FloatField()
    TOTAL_PEDIDO = models.FloatField()
    OBS = models.TextField()
    POSICAO = models.CharField(max_length=15)
    DTFECHAMENTO = models.DateTimeField()
    TOTAL_PRODUTOS = models.FloatField()
    
    class Meta:
        unique_together = (('PEDIDO', 'EMPRESA'),)
    
    class Meta:
        managed = False
        db_table = 'VIEW_VMASTER'  

class VIEW_DETAIL(models.Model):
    PEDIDO = models.IntegerField (primary_key= True)
    EMPRESA = models.IntegerField ()
    AUTOID = models.IntegerField()
    CODID = models.IntegerField()
    COD_INTERNO = models.CharField(max_length=30)
    COD_PEDIDO = models.CharField(max_length=30)
    DESCRICAOPROD = models.CharField(max_length=70)
    QUANT = models.FloatField()
    VLR_GARANTIA = models.FloatField()
    VLR_CUSTO = models.FloatField()
    VLR_UNIT = models.FloatField()
    VLR_TABELA = models.FloatField()
    VLR_TOTAL = models.FloatField()

    class Meta:
        unique_together = (('PEDIDO', 'EMPRESA'),)
    
    class Meta:
        managed = False
        db_table = 'VIEW_VDETAIL'
