from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
users = ['Rashid', 'Artem', 'Vladilen']
def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            if username in users:
                info['error'] = "Username already exists."
            elif password != repeat_password:
                info['error'] = "Passwords do not match."
            elif age < 18:
                info['error'] = "You must be at least 18 years old."
            else:
                users.append(username)
                info['success'] = f"Welcome, {username}!"
        else:
            info['error'] = "Invalid form submission."
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        age = request.POST.get('age')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(age)

        if username in users:
            info['error'] = "Username already exists."
        elif password != repeat_password:
            info['error'] = "Passwords do not match."
        elif age < 18:
            info['error'] = "You must be at least 18 years old."
        else:
            users.append(username)
            info['success'] = f"Welcome, {username}!"

    return render(request, 'fifth_task/registration_page.html', info)
