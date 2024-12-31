from django.contrib.admin import AdminSite
from .models import Author
from .models import OriginWork
from .models import DerivativeDevelopeDepartment
from .models import DevelopTeam
from .models import Product
from .models import Authorize
from .models import ProductionCommission

class MyAdminSite(AdminSite):
    site_header = "IP公司管理"

admin_site = MyAdminSite(name="myadmin")
# Register your models here.

admin_site.register(Author)
admin_site.register(OriginWork)
admin_site.register(DerivativeDevelopeDepartment)
admin_site.register(DevelopTeam)
admin_site.register(Product)
admin_site.register(Authorize)
admin_site.register(ProductionCommission)
