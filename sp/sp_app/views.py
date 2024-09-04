import os
import django
import cv2
import numpy as np
from datetime import datetime
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render
from sp_app.models import Login, User
from sp_app.test import imagepredict

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sp.settings')
django.setup()

# Define your views
def ab(request):
    return render(request, 'index.html')

def abc(request):
    return render(request, 'indexhm.html')

def addfile(request):
    return render(request, 'indexhm.html')
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt       ###since there occurs csfr error and cant upload image(overrides the error)
def addfilepost(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            photo = request.FILES['file']
            file_name = default_storage.save(photo.name, photo)
            file_path = default_storage.path(file_name)  # Get the local file path

            if not os.path.exists(file_path):
                return HttpResponse("File not found")

            if file_name.endswith((".mp4", ".avi")):
                cap = cv2.VideoCapture(file_path)
                if not cap.isOpened():
                    return HttpResponse("Error opening video file")

                lists = []
                count = 0
                while cap.isOpened():
                    ret, frame = cap.read()
                    if ret:
                        if count % 20 == 0:
                            sample_image_path = os.path.join('media', 'sample.png')
                            cv2.imwrite(sample_image_path, frame)
                            res = imagepredict(sample_image_path)
                            lists.append(res)
                    else:
                        break
                    count += 1

                cap.release()
                cv2.destroyAllWindows()

                pc = sum(1 for i in lists if i[1] == "Real")
                nc = len(lists) - pc

                if nc > pc:
                    c = nc / (nc + pc)
                    result = [c, "DeepFake"]
                else:
                    c = pc / (nc + pc)
                    result = [c, "Real"]

                return render(request, "indexhm.html", {"val": result})

            else:
                res = imagepredict(file_path)
                return render(request, "indexhm.html", {"val": res})

        else:
            return render(request, "indexhm.html", {"popup": True})
    else:
        return HttpResponse("Invalid request method.")

def user_register(request):
    return render(request, 'user_register.html')

def user_register_POST(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']

    # Ensure proper user creation using Django's User model
    user = Login.objects.create(username=email, password=password, type='user')
    User.objects.create(name=name, email=email, phone_number=phone, LOGIN=user)

    return HttpResponse('''<script>alert('Registration Successful');window.location="/login"</script>''')

def login(request):
    return render(request, 'login.html')

def login_post(request):
    username = request.POST['name']
    password = request.POST['password']
    
    try:
        user = Login.objects.get(username=username, password=password)
        request.session['lid'] = user.id
        if user.type == 'user':
            return HttpResponse('''<script>alert('Login Successful');window.location="/addfile"</script>''')
    except Login.DoesNotExist:
        pass

    return HttpResponse('''<script>alert('Invalid username or password');window.location="/login"</script>''')
