from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from . import models
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,"index.html")
# Para que cualquiera pueda acceder a la vista
@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request):
        blogPost = models.PostGeneral.objects.all()
        jsonPost = []
        
        for post in blogPost:
            jsonPost.append({
                "title": post.title,
                "content": post.content,
                "created_at": post.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })
        return HttpResponse(json.dumps(jsonPost), content_type="application/json")
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            new_post = models.PostGeneral.objects.create(
                title=data.get('title'),
                content=data.get('content'),  
            )
            
            return JsonResponse({
                "message": "README.md guardado exitosamente",
                "id": new_post.id,
                "title": new_post.title
            })
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
    