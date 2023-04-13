from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from bankapp.models import District, Branch, Application


def home(request):
    return render(request, 'index.html')


def body(request):
    return render(request, 'body.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bankapp:new')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('bankapp:login')
    return render(request, 'login.html')


# def apply(request):
#     return render(request, 'apply.html')


def new(request):
    return render(request, 'newpage.html')


# def apply(request):
#     districts = District.objects.all().values('id', 'name')
#     branches = Branch.objects.all().values('name')
#     return render(request, 'apply.html', {'districts': districts, 'branches': branches})


def register(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()
                return redirect('bankapp:login')
        else:
            messages.info(request, 'The Password is not matching')
            return redirect('bankapp:register')

    return render(request, 'register.html')


def apply(request):
    districts = District.objects.all().values('id', 'name')
    branches = Branch.objects.all().values('id', 'name')
    length = len(Application.objects.all())
    if request.method == 'POST':
        name = request.POST.get('name', )
        dob = request.POST.get('date', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        district = request.POST.get('district', )
        branch = request.POST.get('branch', )
        account = request.POST.get('account', )
        materials = request.POST.get('materials', )

        app = Application(id=length + 1, name=name, dob=dob, age=age, gender=gender, phone=phone, email=email, address=address, district_id=district, branch_id=branch, account=account, materials=materials)
        app.save()
        messages.info(request, 'Application Successfully Completed')
        return redirect('/')
    return render(request, 'apply.html', {'districts': districts, 'branches': branches})


# def branch(request):
#     branches = Branch.objects.all().values('name')
#     return render(request, 'apply.html', {'branches': branches})
