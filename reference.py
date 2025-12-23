


# REST = Representational State Transfer

===================================================

# charachteristic of REST:
from numpy.lib._function_base_impl import delete
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import RetrieveModelMixin
import posixpath
- Statless: 
- client - server architecture
- standardization : (
    get
    post 
    patch = (particial update like : update name only)
    put = (compelete update- Hard reset if any value come null it will set it as null, doesn't matter if it is null or not)
    delete 
)
- easy to read : response come in : xml or json format


# ENDPOINT : 
    - web  : http://127.0.0.1:8000/students/
    - api : http://127.0.0.1:8000/api/students/


===================================================

# NOTES:

Serializer : it's help to convert the data,obj or (queryset) into json or xml format.
Deserializer : it's help to convert the json or xml data into python object (queryset).

    - Serializers : 
    - ModelSerializer : Smart and know how to convert the data into json or xml format.
    - HyperlinkedModelSerializer : 
    - HyperlinkedSerializer : 


# Implement: create a saperate file "serializers.py" in app. (make sure to add "rest_framework" in settings.py)

# In serializers.py : 

from rest_framework import serializers
from student import Student(model)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# In views.py : 

from rest_framework.response import Response
from students.models import Students # model
from .serializer import StudentSerializer # serializer class
from rest_framework import status
from rest_framework.decorators import api_view # to allow only specific methods to access data

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
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

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


    
# Now it's time to wrok with class based views.. 

- inbuilt method: get, post, put, delete()
        


class EmployeeViews(APIView):
    def get(self, request):
        employee = Employees.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailsView(APIView):

    def get_employee(self, pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        employee = self.get_employee(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employee = self.get_employee(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee = self.get_employee(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





=================================================================================================================================

# Mixins : they are resuable classes that provide common functionality to other classes.

    - ListModelMixin : suport for list of objects : list()
    - CreateModelMixin : create new object : create()
    - RetrieveModelMixin : retrieve single object : retrieve()
    - UpdateModelMixin : update single object : update()
    - DestroyModelMixin : delete single object : destroy()

    generatic.generaticAPIView :  foundation class and provide essential fucntionality for incoming http request : get(), post(), put(), delete()

    - also response in structure output. 

    # mixins with Generics

    
    class EmployeeViews(mixins.ListModelMixin, mixins.CreateModelMixin , generics.GenericAPIView):
        queryset = Employees.objects.all()
        serializer_class = EmployeeSerializer
        
        def get(self, request):
            return self.list(request)
        
        def post(self, request):
            return self.create(request)


    class EmployeeDetailsView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
        queryset = Employees.objects.all()
        serializer_class = EmployeeSerializer

        def get(self,request, pk):
            return self.retrieve(request, pk)

        def put(self, request, pk):
            return self.update(request, pk)

        def delete(self, request, pk):
            return self.destroy(request, pk)

=================================================================================================================================

# Generics Views : 


    # single object
    - ListAPIView : for list of objects
    - CreateAPIView : for create new object
    - RetrieveAPIView : for retrieve single object
    - UpdateAPIView : for update single object
    - DestroyAPIView : for delete single object

    # multiple object
    - ListCreateAPIView : for list and create new objects
    - RetrieveUpdateAPIView : for retrieve and update objects
    - RetrieveDestroyAPIView : for retrieve and delete objects
    - RetrieveUpdateDestroyAPIView : for retrieve and update and delete objects

    class EmployeeViews(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    class EmployeeDetailsView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
        queryset = Employees.objects.all()
        serializer_class = EmployeeSerializer
        lookup_field = 'pk'

=================================================================================================================================

# Viewsets: it's a collection of views that are related to a single resource.

    1) viewset.Viewsets :
        - it's a collection of views that are related to a single resource.
        - get(), create(), retrieve(), update(), delete()

    2) viewset.ModelViewSet:
        - it's just take quesryset and serializer_class and provide all the functionality with or without PrimaryKey based operation.
        

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


=======================================================================================================================================


# Nested Serializers : when you need multiple serializers in a single serializer like a blog can have multiple comments or like. 


# blogs

# class BlogsView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
    
# class CommentsView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# #primary key based operations
# class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'pk'

# class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = 'pk'



=====================================================================================================================================

# pagination :  it's a process of breaking down a large dataset into smaller, more manageable chunks.

    1) PageNumberPagination : it's a pagination class that provides a simple way to paginate a queryset. if pagination is 30 the it'll display the 30 record. 

    2) LimitOffsetPagination : there is 2 things limit and offset. limit is the number of records to display and offset is the number of records to skip.

    - if offset is 10 and limit is 10 then it'll display the 10 record from 11 to 20.
    - if offset is 0 and limit is 10 then it'll display the 10 record from 1 to 10.

    # 3) CursorPagination : it's a pagination class that provides a way to paginate a queryset using cursor based pagination.



    # Global Pagination | this will only for generics and viewsets
    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 2
    }

    # CUSTOM Pagination | 
    from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
    from rest_framework.response import Response

    class CustomPagination(PageNumberPagination):
        page_query_param = 'page-num'
        page_size_query_param = 'page_size'
        max_page_size = 1

        def get_paginated_response(self, data):
            return Response({
                'next':self.get_next_link(),
                'previous':self.get_previous_link(),
                'count':self.page.paginator.count,
                'total_pages':self.page.paginator.num_pages,
                'page_size':self.page_size,
                'results':data
            })

====================================================================================================================================


# Filtering : it's a process of filtering a queryset based on a set of conditions.

    1) Global Filtering : it's a process of filtering a queryset based on a set of conditions.
    2) Local Filtering : it's a process of filtering a queryset based on a set of conditions. it can be target to generics and viewsets.


    # Global Filtering
    REST_FRAMEWORK = {
        "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"]
    }

    class EmployeeViewSet(viewsets.ModelViewSet):
        queryset = Employees.objects.all()
        serializer_class = EmployeeSerializer
        pagination_class = CustomPagination
        # filterset_fields = ['designation'] # case sensitive | default inbuilt
        filterset_class = EmployeeFilter # custom class filter

    # Local Filtering
    class BlogsView(generics.ListAPIView, generics.CreateAPIView):
        queryset = Blog.objects.all()
        serializer_class = BlogSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['blog_title', 'blog_body']


    class EmployeeFilter(django_filters.FilterSet):
        designation = django_filters.CharFilter(field_name='designation' ,lookup_expr='iexact')
        name = django_filters.CharFilter(field_name='emp_name' ,lookup_expr='icontains')
        # emp_id = django_filters.RangeFilter(field_name='emp_id') #RangeFilterb will only work with Integer values and primarykey 
        id_min = django_filters.CharFilter(method='filter_by_id', label='From ID')
        id_max = django_filters.CharFilter(method='filter_by_id', label='To EMP_ID')

        class Meta:
            model = Employees
            fields = ['designation', 'name', 'id_min', 'id_max']

        def filter_by_id(self, queryset, value):
            if value == 'id_min':
                return queryset.filter(emp_id__gte=value)
            elif value == 'id_max':
                return queryset.filter(emp_id__lte=value)
            else:
                return queryset


====================================================================================================================================

# Still need to explore : Authentication and Authorization, Permission, Tokens ETC..