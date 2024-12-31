from django.contrib import admin
from .models import Author
from .models import OriginWork
from .models import DerivativeDevelopeDepartment
from .models import DevelopTeam
from .models import Product
from .models import Authorize
from .models import ProductionCommission


# Register your models here.

admin.site.register(Author)
admin.site.register(OriginWork)
admin.site.register(DerivativeDevelopeDepartment)
admin.site.register(DevelopTeam)
admin.site.register(Product)
admin.site.register(Authorize)
admin.site.register(ProductionCommission)
