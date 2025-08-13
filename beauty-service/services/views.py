from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import ServiceModel
from .forms import RegisterForm
# Create your views here.

def index_view(request):
    services = ServiceModel.objects.all()
    context = {'services':  services}
    return render(request, 'main.html', context)

def service_view(request, pk):
    service = get_object_or_404(ServiceModel, pk=pk)
    form = RegisterForm(None, initial={'service': service.pk})
    context = {'service': service, 'form': form}
    return render(request, 'service.html', context)

def service_register_view(request, pk):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(reverse('service-view', kwargs={'pk':pk}))