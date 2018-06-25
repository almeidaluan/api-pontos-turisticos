from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response

# 1-Viewset
# 2-Serializer
# 3-Rotas
class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    # faz o object all normal mas quando voce quer passar parametros na querystring ?nome=sas&descricao=algumacoisa
    #ele vai nos ifs
    def get_queryset(self):
        id = self.request.query_params.get('id',None) 
        nome = self.request.query_params.get('nome',None)
        queryset = PontoTuristico.objects.all()

        if id:
             queryset = PontoTuristico.objects.filter(id=id)
        if nome:
            queryset = queryset.filter(nome=nome)

        return queryset


    '''

    caso eu queira sobrescrever os metodos.
     
     def list(self,request,*args,**kwargs):
         return Response({'teste':123})
    
     def create(self,request,*args,**kwargs):
         return Response{'Tese':request.data['atributo-do-model']} 

    def retrieve(self,request,*args,**kwargs): Retorna um especifico
        return pass

    def partial_update(self,request,*args,**kwargs): 


    Action Customizada
    def denunciar(methods=['post','get'],detail=true) - quando eu queroa acessar essa action de um detalhe de endpoint
                                                      - ou se eu quiser denunciar em um post
                                                        -detail referencia um endpoint detalhado pra ser o endpoint pai soh teria que ser detail = false
    '''