from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import RandomNumber
import random

@login_required(login_url='/admin/login/')
def dashboard(request):
    number = get_random_number()
    RandomNumber.objects.all().delete()
    RandomNumber.objects.create(value=number)
    return render(request, 'myapp/dashboard.html', {'number': number})

def get_random_number():
    return random.randint(1, 100)

@login_required(login_url='/admin/login/')
def get_latest_random_number(request):
    try:
        latest_entry = RandomNumber.objects.latest('id')
        latest_number = latest_entry.value
        new_number = random.randint(1, 100)
        RandomNumber.objects.create(value=new_number)
        return JsonResponse({'number': latest_number})
    except RandomNumber.DoesNotExist:
        initial_number = random.randint(1, 100)
        RandomNumber.objects.create(value=initial_number)
        return JsonResponse({'number': initial_number})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)