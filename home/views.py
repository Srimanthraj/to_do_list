from django.shortcuts import render, HttpResponse, redirect
from home.models import Task
from home.serializers import TaskSerializers
from rest_framework import viewsets
import requests
import json
import datetime
import logging
# logger = logging.getLogger(__name__)
logger = logging.getLogger('Django')


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()

    def create(self, request, *args, **kwargs):
        logger.info('POST/API call received for TaskViewSet create ')
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info('API call received for TaskViewSet retrieve')
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info(
            f'PUT/ API call received for TaskViewSet update with id {instance.id}')
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info(
            f'DELETE/ API call received for TaskViewSet with id {instance.id}')
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        logger.info('GET/ API call received for TaskViewSet list ')
        return super().list(request, *args, **kwargs)
        # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(
    #         instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

# class TaskViewSet(viewsets.ModelViewSet):
#     # logger.info('API call received for your_api_view')
#     serializer_class = TaskSerializers
#     queryset = Task.objects.all()

#     def create(self, request, *args, **kwargs):
#         logger.info('API call received for TaskViewSet create')
#         return super().create(request, *args, **kwargs)

#     def retrieve(self, request, *args, **kwargs):
#         logger.info('API call received for TaskViewSet retrieve')
#         return super().retrieve(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def list(self, request, *args, **kwargs):
#         logger.info('GET/ API call received for TaskViewSet list')
#         return super().list(request, *args, **kwargs)


# def homepage(request):
#     context = {'success': False}
#     logger.warning('Homepage was accessed at ' +
#                    str(datetime.datetime.now())+' hours!')
#     # logger.critical('Homepage...')
#     if request.method == "POST":

#         data = json.loads(request.body)
#         elapsed_time = data.get('elapsed_time')
#         logger.info(f'User spent {elapsed_time:.2f} seconds on the page.')
#         print(elapsed_time)

#         title = request.POST['title']
#         desc = request.POST['desc']
#         # print(title, desc)
#         # ins = Task(taskTitle=title, taskDesc=desc)
#         # ins.save()
#         api_endpoint = 'http://127.0.0.1:8000/api/student/'
#         data = {'taskTitle': title, 'taskDesc': desc}
#         response = requests.post(api_endpoint, data=data)
#         context = {'success': True}

#     return render(request, 'index.html', context)
def homepage(request):
    User = request.user
    Username = User.username
    context = {'success': False}
    logger.warning('Homepage was accessed by  ' + Username)

    if request.method == "POST":
        # data = json.loads(request.body)
        # elapsed_time = data.get('elapsed_time')

        title = request.POST['title']
        desc = request.POST['desc']
        api_endpoint = 'http://127.0.0.1:8000/api/student/'
        data = {'taskTitle': title, 'taskDesc': desc}
        response = requests.post(api_endpoint, data=data)
        context = {'success': True}

    return render(request, 'index.html', context)


def house(request):
    return render(request, 'homie.html')


def index1(request):
    context = {'success': False}

    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        # print(title, desc)
        # ins = Task(taskTitle=title, taskDesc=desc)
        # ins.save()
        api_endpoint = 'http://127.0.0.1:8000/api/student/'
        data = {'taskTitle': title, 'taskDesc': desc}
        response = requests.post(api_endpoint, data=data)
        context = {'success': True}

    return render(request, 'index1.html', context)


def ignore_favicon(request):
    return HttpResponse(status=200)


def index2(request):
    return render(request, 'index2.html')
# post


# get


def taskspage(request):
    response = requests.get('http://127.0.0.1:8000/api/student/').json()
    # allTasks = Task.objects.all()
    # print(allTasks)
    # context = {'tasks': allTasks}
    context = {'tasks': response}
    return render(request, 'tasks.html', context)

# delete


def deleteTask(request, id):
    api_endpoint = f'http://127.0.0.1:8000/api/student/{id}/'
    response = requests.delete(api_endpoint)
    return redirect('/tasks')
    if response.status_code == 204:
        return redirect('/tasks')
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
        title = request.POST['title']
        desc = request.POST['desc']
        context = {'taskTitle': title, 'taskDesc': desc}
        api_endpoint = f'http://127.0.0.1:8000/api/student/{id}/'
        data = {'taskTitle': title, 'taskDesc': desc}
        response = requests.put(api_endpoint, data=data)
        return redirect('/tasks/')
    return render(request, 'update.html', context)

# def UpdateTask(request, id):
#     upt = Task.objects.get(id=id)
#     context = {"task": upt}

#     if request.method == "POST":
#         title = request.POST['title']
#         desc = request.POST['desc']
#         upt.taskTitle = title
#         upt.taskDesc = desc
#         upt.save()
#         return redirect('/tasks/')
#     return render(request, 'update.html', context)
