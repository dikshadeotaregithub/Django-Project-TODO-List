from django.http import HttpResponse
from django.shortcuts import render
from home.models import Task

def home(request):
    context = {'success': False}
    if request.method == "POST":
        # Handle the form submission
        title = request.POST.get('title')
        desc = request.POST.get('Desc')  # Ensure the key matches the form field name

        if title and desc:  # Ensure both title and desc are provided
            # Save the task to the database
            ins = Task(taskTitle=title, taskDesc=desc)
            ins.save()
            context['success'] = True  # Indicate success

    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
   # print(allTasks)
   # for item in allTasks:
    #    print(item.taskDesc)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html',context)




