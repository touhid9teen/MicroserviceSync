from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import TodoItem
from rest_framework.response import Response
from rest_framework import status
from .authenticate import CustomAuthentication

class TodoView(APIView):
    authentication_classes = [CustomAuthentication]

    def get(self, request):
        user_id = request.GET.get('user_id')
        todo_id = request.GET.get('todo_id')

        if user_id and todo_id:
            try:
                todo = TodoItem.objects.get(user_id=user_id, todo_id=todo_id)
                serializer = TodoSerializer(todo)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except TodoItem.DoesNotExist:
                return Response({"error": "Todo item not found"}, status=status.HTTP_404_NOT_FOUND)
        elif user_id:
            todos = TodoItem.objects.filter(user_id=user_id)
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        user_id = request.GET.get('user_id')
        todo_id = request.GET.get('todo_id')
        try:
            todo = TodoItem.objects.get(todo_id=todo_id, user_id=user_id)
            serializer = TodoSerializer(todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TodoItem.DoesNotExist:
            return Response({"error": "Todo item not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request):
        user_id = request.GET.get('user_id')
        todo_id = request.GET.get('todo_id')
        try:
            todo = TodoItem.objects.get(todo_id=todo_id, user_id=user_id)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TodoItem.DoesNotExist:
            return Response({"error": "Todo item not found"}, status=status.HTTP_404_NOT_FOUND)