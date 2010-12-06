from django.http import HttpResponse
from server import restful
from django.core import serializers
from server.models import Produto

class ProdutoView(restful.RestView):
    def get(self, request, codigo="0", formato="xml"):
        print request.GET
        print request.POST
        if (codigo == "0"):
            return HttpResponse(serializers.serialize(formato, Produto.objects.all()))
        else:
            print codigo
            return HttpResponse(serializers.serialize(formato, Produto.objects.filter(codigo=codigo)),mimetype="application/"+formato)

    def post(self,request):
        print request.GET
        print request.POST
        return HttpResponse("POST")

    def put(self, request):
        print request.GET
        print request.POST
        return HttpResponse("PUT")

    def delete(self, request):
        print request.GET
        print request.POST
        return HttpResponse("DELETE")

