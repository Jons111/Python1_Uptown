import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def home(malumot):
    if malumot.method =="POST":
        text = malumot.POST.get('matn')
        soz = str(text).strip()
        qidirish = Q(nomi__contains=soz)| Q(old_price__startswith=soz)|Q(new_price__startswith=soz)\
                   |Q(son1__startswith=soz)|Q(son2__startswith=soz)|Q(manzil__contains=soz)|Q(kv__startswith=soz)|Q(vaqt__startswith=soz)

        serviclar = Service.objects.filter(qidirish)
        return render(malumot, 'index.html', {"services": serviclar,})
    else:
        serviclar = Service.objects.all().order_by('-id')[:3]
        return render(malumot,'index.html',{"services":serviclar})

def contact(malumot):
    if malumot.method =="POST":
        ism = malumot.POST.get('ism')
        gmail = malumot.POST.get('mail')
        fan = malumot.POST.get('sub')
        xabar = malumot.POST.get('message')
        vaqt = datetime.datetime.now()
        Murojaat(ism=ism,mail=gmail,subject=fan,message=xabar,vaqt=vaqt).save()
    return render(malumot,'contact.html')