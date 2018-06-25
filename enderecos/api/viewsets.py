from rest_framework.viewsets import ModelViewSet
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco

class EnderecoViewSet(ModelViewSet):
    # queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    
    #Normalmente feito quando a query tem que ser mais complexa
    def get_queryset(self):
        return Endereco.objects.all()