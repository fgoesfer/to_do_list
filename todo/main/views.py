from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo


def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    
    len_completed = len(Todo.objects.filter(complete=True))
    
    len_not = len(todo_items) - len_completed

    return render(request, 'main/index.html', {'todo_items': todo_items, 'len_completed': len_completed, 'len_not': len_not})

@csrf_exempt
def add_to_do(request):
    current_data = timezone.now()
    content = request.POST['content']
    Todo.objects.create(added_date=current_data, text=content, complete=False)
    

    return HttpResponseRedirect("/")

@csrf_exempt
def delete_all(request):
    """
    Function that delets all the list
    """
    Todo.objects.all().delete()
    return HttpResponseRedirect("/")


@csrf_exempt
def add_completed(request, todo_id):
    """
    Add activity to completed list
    """
    
    todo = Todo.objects.get(pk=todo_id)
    
    if todo.complete:
        todo.complete = False
    else:
        todo.complete = True
    
    todo.save()
    
    return HttpResponseRedirect("/")