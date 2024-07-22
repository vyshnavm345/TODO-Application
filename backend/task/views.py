from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# handles the get all and create new
# class TaskList(generics.ListCreateAPIView):
#     permission_classes = [AllowAny]
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
class TaskList(APIView):
    print("inside the get function")
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("inside the get function")
        print("request ", request)
        tasks = Task.objects.filter(user=request.user)
        print("tasks ", tasks)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Ensure only the tasks belonging to the authenticated user are returned
        return Task.objects.filter(user=self.request.user)






# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [AllowAny]
#     queryset = Task.objects.all(user=request.user)
#     serializer_class = TaskSerializer