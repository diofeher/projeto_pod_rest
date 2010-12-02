from django.http import Http404

class RestView(object):
    def __call__(self, request, *args, **kwargs):
        if (request.method == "GET"):
            return self.get(request, *args, **kwargs)
        if (request.method == "POST"):
            return self.post(request, *args, **kwargs)
        if (request.method == "PUT"):
            return self.put(request, *args, **kwargs)
        if (request.method == "DELETE"):
            return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404()
    def post(self, request, *args, **kwargs):
        raise Http404()
    def put(self, request, *args, **kwargs):
        raise Http404()
    def delete(self, request, *args, **kwargs):
        raise Http404()
