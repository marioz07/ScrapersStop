from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

from .models import Orders, Contact


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home page')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'Main/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login page')

        context = {'form': form}
        return render(request, 'Main/Register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login page')


def home(request):
    return render(request, 'Main/index.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'Main/contact.html')


@login_required(login_url='login page')
def checkout(request):
    orders = Orders.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'Main/checkout.html', context)


def events(request):
    return render(request, 'Main/events.html')


def awareness(request):
    return render(request, 'Main/awareness.html')


def aboutus(request):
    return render(request, 'Main/About.html')


@login_required(login_url='login page')
def sell(request):
    global Price
    Metal = "Metal"
    Steel = "Steel"
    copper = "copper"
    plastic = "plastic"
    Aluminium = "Aluminium"

    if request.method == "POST":
        user = request.user
        Scrap = request.POST.get('Scrap', '')
        Weight = request.POST.get('Weight', '')
        Address1 = request.POST.get('Address1', '')
        Address2 = request.POST.get('Address2', '')
        locality = request.POST.get('locality', '')

        if Scrap.__eq__(Metal):
            Price = 12
        elif Scrap.__eq__(Steel):
            Price = 10
        elif Scrap.__eq__(copper):
            Price = 6
        elif Scrap.__eq__(plastic):
            Price = 2
        elif Scrap.__eq__(Aluminium):
            Price = 30


        Total_price = Price * int(Weight)

        order = Orders(Scrap=Scrap, Total_Price=Total_price, Weight=Weight, Address1=Address1, Address2=Address2,
                       locality=locality, user=user)
        order.save()

        thank = True
        id = order.order_id
        return render(request, 'Main/sell.html', {'thank': thank, 'id': id})
    return render(request, 'Main/sell.html',)





