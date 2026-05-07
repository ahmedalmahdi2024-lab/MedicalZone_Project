from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, ContactRequest

def index(request):
    # أولاً: التعامل مع إرسال النموذج (POST)
    if request.method == "POST":
        hospital_name = request.POST.get('hospital_name')
        device_type = request.POST.get('device_type')
        phone_number = request.POST.get('phone_number')
        description = request.POST.get('description')

        # حفظ الطلب في قاعدة البيانات
        ContactRequest.objects.create(
            hospital_name=hospital_name,
            device_type=device_type,
            phone_number=phone_number,
            description=description
        )
        
        # تجهيز رسالة النجاح
        messages.success(request, "تم إرسال طلبك بنجاح!")
      

        
        # إعادة التوجيه لمنع إرسال البيانات مرتين عند تحديث الصفحة
        return redirect('index')

    # ثانياً: عرض الصفحة والخدمات (GET)
    services = Service.objects.all()
    return render(request, 'MedicalZone/index.html', {'services': services})