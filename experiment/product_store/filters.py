import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    """Добавляет url-ы
    /?max_price=<int>
    /?min_price=<int>
    при этом граница включается в фильтр
    field_name - это название поле в модели, по которому производится фильтрация"""
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    release_date_undo = django_filters.DateFilter(field_name='release_date', lookup_expr='lte')

    class Meta:
        model = Product
        # указываем поля для точной фильтрации по значению
        fields = ['id', 'price', 'name', 'manufacturer__name']

        # exclude = ('release_date', )

        """добавляет url-ы
         /?price__lt=<int>
         /?price__gt=<int>
         /?price=<int>
         при этом граница не включается в фильтр, в отличие от объявления 
         поля через NumberFilter()"""
        # fields = {
        #     'price': ['lt', 'gt', 'exact'],
        # }
