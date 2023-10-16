from django.shortcuts import render, HttpResponse, redirect
from home2.models import Homework
from home2.serializers import HomeworkSerializers
from rest_framework import viewsets
import requests


class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializers
    queryset = Homework.objects.all()


# post


def homepage(request):
    context = {'success2': False}
    if request.method == "POST":
        print('entered post2')
        title2 = request.POST['title']
        desc2 = request.POST['desc']
        print(title2, desc2)
        # ins = Task(taskTitle=title, taskDesc=desc)
        # ins.save()
        api_endpoint = 'http://127.0.0.1:8000/api/homework/'
        data = {'taskTitle2': title2, 'taskDesc2': desc2}
        response = requests.post(api_endpoint, data=data)
        context = {'success2': True}
        return redirect('/post2/')

    return render(request, 'index.html', context)

# get


def taskspage(request):
    response = requests.get('http://127.0.0.1:8000/api/homework/').json()
    # allTasks = Task.objects.all()
    # print(allTasks)
    # context = {'tasks': allTasks}
    context = {'tasks': response}
    return render(request, 'tasks2.html', context)

# delete


def deleteTask(request, id):
    api_endpoint = f'http://127.0.0.1:8000/api/homework/{id}/'
    response = requests.delete(api_endpoint)
    return redirect('/tasks2')
    if response.status_code == 204:
        return redirect('/tasks2')
    else:
        return HttpResponse('failed to delete the task')
        # return render(request, 'error.html', {'message': 'Failed to delete task'})


# def deleteTask(request, id):
#     dee = Task.objects.get(id=id)
#     dee.delete()
#     return redirect('/tasks')


# PUT
def UpdateTask(request, id):
    context = {'success': False}
    if request.method == "POST":
        title2 = request.POST['title']
        desc2 = request.POST['desc']
        context = {'taskTitle': title2, 'taskDesc': desc2}
        api_endpoint = f'http://127.0.0.1:8000/api/homework/{id}/'
        data = {'taskTitle2': title2, 'taskDesc2': desc2}
        response = requests.put(api_endpoint, data=data)
        return redirect('/tasks2/')
    return render(request, 'update2.html', context)
