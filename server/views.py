from django.http import HttpResponse
from server import restful
from django.core import serializers
from server.models import Produto

class ProdutoView(restful.RestView):
    def get(self, request, codigo="0", formato="xml"):
        print codigo
        
        if (codigo == "0"):
            return HttpResponse(serializers.serialize(formato, Produto.objects.all()))
        else:
            print codigo
            return HttpResponse(serializers.serialize(formato, Produto.objects.filter(codigo=codigo)),mimetype="application/"+formato)

    def post(self,request):
        return HttpResponse(serializers.serialize(formato, Produto.objects.all()),mimetype="application/"+formato)
