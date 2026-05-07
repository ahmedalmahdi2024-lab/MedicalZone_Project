from django.contrib import admin
from .models import Service, ContactRequest

class ContactRequestAdmin(admin.ModelAdmin):
    # قائمة الأعمدة التي ستراها في لوحة التحكم
    list_display = ('hospital_name', 'device_type', 'created_at', 'status')
    # لجعل التاريخ قابلاً للقراءة فقط (لأن Django يمنع تعديله يدوياً)
    readonly_fields = ('created_at',)

admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(Service)