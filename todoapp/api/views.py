from django.shortcuts import render
from api.models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TaskSerializer
from rest_framework import status
from django.http.response import JsonResponse


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Task List':'/task-list/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Detail':'/tast-detail/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/'
    }
    return Response(api_urls)



@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)



@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return JsonResponse(serializer.data, safe=False)
    except:
        return JsonResponse('Record Not Found', safe=False)



@api_view(['POST'])
def task_update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse("Updated Successfully!", safe=False)
    except:
        return JsonResponse("Failed to update!", safe=False)




@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Created Successfully!", safe=False)
    return JsonResponse("Failed to create!", safe=False)



@api_view(['POST'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return JsonResponse("Deleted Successfully!", safe=False)
    except:
        return JsonResponse("Failed to delete!", safe=False)