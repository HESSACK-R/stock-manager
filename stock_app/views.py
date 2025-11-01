from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Phone
from .forms import PhoneForm

def phone_list(request):
    query = request.GET.get('q')
    if query:
        phones = Phone.objects.filter(Q(name__icontains=query) | Q(brand__icontains=query)).order_by('-created_at')
    else:
        phones = Phone.objects.order_by('-created_at')

    paginator = Paginator(phones, 10)  # Show 10 phones per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'stock_app/phone_list.html', {
        'page_obj': page_obj,
        'query': query,
    })

def phone_create(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)  # ← IMPORTANT pour l’upload
        if form.is_valid():
            form.save()
            return redirect('phone_list')
    else:
        form = PhoneForm()
    return render(request, 'stock_app/phone_form.html', {'form': form})

def phone_update(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES, instance=phone)  # ← IMPORTANT pour l’upload
        if form.is_valid():
            form.save()
            return redirect('phone_list')
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'stock_app/phone_form.html', {'form': form, 'edit_mode': True})

def phone_delete(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone_list')
    return render(request, 'stock_app/phone_confirm_delete.html', {'phone': phone})