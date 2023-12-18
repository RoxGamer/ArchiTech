from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import logout, authenticate, login
# from django.utils import timezone
# from .models import UserLoginHistory
# from datetime import datetime
# from django.contrib import messages
from django.http import JsonResponse

# from utils.calculator import calculate_sum

# def calculate(request):
#     if request.method == 'GET':
#         return render(request, 'index.html')
#     elif request.method == 'POST':
#         num1 = int(request.POST.get('num1'))
#         num2 = int(request.POST.get('num2'))
#         result = calculate_sum(num1, num2)
#         return render(request, 'index.html', {'result': result})

########################################################################################3
from django.shortcuts import render
from utils.color_image_generator import generate_color_image

# def color_image(request):
#     if request.method == 'POST':
#         red = int(request.POST.get('red', 0))
#         green = int(request.POST.get('green', 0))
#         blue = int(request.POST.get('blue', 0))
#         image_size = 100

#         # Generate color image
#         image_data = generate_color_image(red, green, blue, image_size)
        
#         return render(request, 'getStarted.html', {'image_data': image_data, 'image_size': image_size})
#     else:
#         return render(request, 'getStarted.html')
    
def regenerate_image(request):
    if request.method == 'POST':
        image_size = int(request.session.get('image_size', 100))
        image_size = int(image_size * 1.2)  # Increase image size by 5%
        red = int(request.session.get('red', 0))
        green = int(request.session.get('green', 0))
        blue = int(request.session.get('blue', 0))
        image_data = generate_color_image(red, green, blue, image_size)
        request.session['image_size'] = image_size
        return render(request, 'getStarted.html', {'image_data': image_data, 'image_size': image_size, 'red': red, 'green': green, 'blue': blue})



# def clear_image(request):
#     if request.method == 'POST':
#         request.session.pop('image_data', None)
#         request.session.pop('image_size', None)
#     return render(request, 'index.html')
def clear_image(request):
    if request.method == 'POST':
        request.session.pop('image_data', None)
        request.session.pop('image_size', None)
    #     return redirect('get_started')
    
    # # Return a response for other cases (e.g., GET requests)
    return redirect('get_started')

def index(request):
    return render(request, 'index11.html')

def get_started_page(request):
    if request.method == 'POST':
        red = int(request.POST.get('red', 0))
        green = int(request.POST.get('green', 0))
        blue = int(request.POST.get('blue', 0))
        image_size = 100

        # Generate color image
        image_data = generate_color_image(red, green, blue, image_size)
        
        return render(request, 'getStarted.html', {'image_data': image_data, 'image_size': image_size})
    else:
        return render(request, 'getStarted.html')

def go_home(request):
    return render(request, 'index11.html')

def get_started(request):
    return redirect('https://brsknken3fgmmh-3000.proxy.runpod.net/')
