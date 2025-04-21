from django.shortcuts import render

# Create your views here.
# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import slow_add

class AddView(APIView):
    def get(self, request):
        slow_add.delay(3, 4)
        return Response({"status": "Task Submitted"})
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import process_user_data

class UserProcessAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "User ID required"}, status=status.HTTP_400_BAD_REQUEST)

        # Trigger Celery task
        task = process_user_data.delay(user_id)
        
        return Response({
            "message": "Task has been queued.",
            "task_id": task.id
        }, status=status.HTTP_202_ACCEPTED)
        
from celery.result import AsyncResult
from rest_framework.views import APIView
from rest_framework.response import Response
# Optional: Get Task Status via API
# To track task status:

class TaskStatusAPIView(APIView):
    def get(self, request, task_id):
        result = AsyncResult(task_id)
        return Response({
            'task_id': task_id,
            'state': result.state,
            'result': result.result if result.ready() else None,
        })

