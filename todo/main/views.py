from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo


def home(request):
    return render(request, 'main/index.html')

@csrf_exempt
def add_to_do(request):
    current_data = timezone.now()
    content = request.POST['content']
    #Todo.added_date = current_data
    #Todo.text = content
    aux = Todo.objects.create(added_date=current_data, text=content)
    
    return HttpResponseRedirect("/")