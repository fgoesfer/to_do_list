from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo


def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'main/index.html', {'todo_items': todo_items})

@csrf_exempt
def add_to_do(request):
    current_data = timezone.now()
    content = request.POST['content']
    Todo.objects.create(added_date=current_data, text=content)
    
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_all(request):
    """
    Function that delets all the list
    """

    Todo.objects.all().delete()
    
    return HttpResponseRedirect("/")