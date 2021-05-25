from django.shortcuts import render
from .models import ContactModel, ContactForm
from django.http import HttpResponseRedirect
# Create your views here.


def get(request):
    all = ContactModel.objects.all()
    form = ContactForm(request.POST)
    if request.POST:
        form.save()
        return HttpResponseRedirect("/")
    data = {
        'all': all, 'form': form
    }
    return render(request, template_name= 'main.html', context= data)