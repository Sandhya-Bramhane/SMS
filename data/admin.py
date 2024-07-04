from django.contrib import admin
from data.models import Registration,Admin,Student,Notice,Hostel
# Register your models here.

admin.site.register(Registration)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Notice)
admin.site.register(Hostel)
