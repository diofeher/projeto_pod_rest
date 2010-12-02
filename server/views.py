from django.http import HttpResponse
from server import restful
from django.core import serializers
from server.models import Produto

class ProdutoRest(restful.RestView):
    def get(self, request):
        if (not 'codigo' in request.GET):
            return HttpResponse(serializers.serialize("xml", Produto.objects.all()))
        else:
            return HttpResponse(serializers.serialize("xml", Produto.objects.get(codigo=request.GET['codigo'])))

    def post(self,request):
        return HttpResponse(serializers.serialize("xml", Produto.objects.all()))
