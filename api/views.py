from django.contrib.admin.utils import lookup_field
from django.db.models.query import QuerySet
from rest_framework.response import Response
from students.models import Students # model
from .serializer import StudentSerializer # serializer class
from rest_framework import status
from rest_framework.decorators import api_view # to allow only specific methods to access data
from rest_framework.views import APIView
from employees.models import Employees
from .serializer import EmployeeSerializer
from django.http import Http404
from rest_framework import generics, mixins, viewsets
from django.shortcuts import get_object_or_404
from blogs.models import Blog, Comment
from blogs.serializer import BlogSerializer, CommentSerializer

@api_view(['GET','POST'])
def StudentViews(request):
    if request.method == 'GET':
        student = Students.objects.all()
        serializer = StudentSerializer(student, many=True) # student data can be more then one
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def Studentdetailsview(request,pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Http404()

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class EmployeeViews(APIView):
#     def get(self, request):
#         employee = Employees.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetailsView(APIView):

#     def get_employee(self, pk):
#         try:
#             return Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         employee = self.get_employee(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_employee(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_employee(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# mixins
# class EmployeeViews(mixins.ListModelMixin, mixins.CreateModelMixin , generics.GenericAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)


# class EmployeeDetailsView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self,request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)




#generics based
 # single object
    # - ListAPIView : for list of objects
    # - CreateAPIView : for create new object
    # - RetrieveAPIView : for retrieve single object
    # - UpdateAPIView : for update single object
    # - DestroyAPIView : for delete single object

    # # multiple object
    # - ListCreateAPIView : for list and create new objects
    # - RetrieveUpdateAPIView : for retrieve and update objects
    # - RetrieveDestroyAPIView : for retrieve and delete objects
    # - RetrieveUpdateDestroyAPIView : for retrieve and update and delete objects


# class EmployeeViews(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

# class EmployeeDetailsView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'


# viewsets.ViewSet:
# class EmployeeViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = Employees.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employees, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employees, pk=pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         employee = get_object_or_404(Employees, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# viewsets.ModelViewSet
# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer




# blogs

class BlogsView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class CommentsView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#primary key based operations
class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


