from django_tables2 import tables
from django_tables2.utils import A
from .models import Band

class BandTable(tables.Table):
    name = tables.LinkColumn('Band_detail', args=[A('pk')])
    age = tables.LinkColumn('Band_detail', args=[A('pk')])

    class Meta:
        model = Band
        template_name = 'django_tables2/bootstrap.html'
        fields = ('name', 'age')
