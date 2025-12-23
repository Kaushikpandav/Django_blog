import django_filters
from .models import Employees

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
