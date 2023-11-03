from django.shortcuts import render, redirect
# user is a already created database table model, so you dont have to create that class. u just have to import it and call .models method to submit data to it
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def register(request):  # accepting register request(registe function)
    if request.method == 'POST':
        # get the user input values and save them in the variable
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # create user object and pass the values to the database fields
        if password1 == password2:
            # checking weather the username the user inputed is already in the database
            if User.objects.filter(username=username).exists():
                # redirect to register page because username is already created
                messages.info(
                    request, 'username already taken please try a different username')

                return redirect('register')
            # checking weather the emai the user inputed is already in the database
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'user is already created')
                # redirect to register page because user is already created
                return redirect('register')
            else:       # any of above doestnt happen, user will be created
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
                # redirect to the login page because the user is saved . so let the user to login redirect to the login page
                return redirect('login')
        else:
            messages.info(request, 'password not maching')
            # redirect to register page because password not maching
            return redirect('register')
        return redirect('/')  # redirect to the home page after user regitered
    else:
        # return to register template if user cliked register button
        return render(request, 'register.html')


def login(request):  # login function
    if request.method == 'POST':
        username = request.POST['username']  # get the values that user enterd
        password = request.POST['password']  # get the values that user enterd
        # authanticate wether the post post values from user are in there in the database username and password fields and store them in the user variable
        user = auth.authenticate(username=username, password=password)

        # if the user is available(which means the database field values and user posted values are maching)
        if user is not None:
            auth.login(request, user)  # give login access to the user
            return redirect('gaming')  # returen to the home page
        else:
            messages.info(request, 'invalid credintials')
            # return redirect to the login page because credintials are incorrect
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)  # if user requesr logout , auth. logout will happen
    # and after that it will redirect to  the home page
    return redirect('gaming')
