from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    image = models.ImageField(upload_to='services/', verbose_name="صورة الخدمة")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"

class ContactRequest(models.Model):
    # خيارات حالة الطلب
    STATUS_CHOICES = [
        ('new', 'طلب جديد 🔴'),
        ('pending', 'قيد الإصلاح 🟡'),
        ('done', 'تمت الصيانة 🟢'),
    ]

    hospital_name = models.CharField(max_length=255, verbose_name="اسم المستشفى/العيادة")
    device_type = models.CharField(max_length=200, verbose_name="نوع الجهاز")
    phone_number = models.CharField(max_length=20, verbose_name="رقم التواصل")
    description = models.TextField(verbose_name="وصف العطل")
    
    # حقل التاريخ (يضاف تلقائياً عند الإرسال)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    
    # حقل الحالة
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new', 
        verbose_name="حالة الطلب"
    )

    def __str__(self):
        return f"{self.hospital_name} - {self.device_type}"

    class Meta:
        verbose_name = "طلب صيانة"
        verbose_name_plural = "طلبات الصيانة"
        ordering = ['-created_at'] # ترتيب تلقائي من الأحدث للأقدم