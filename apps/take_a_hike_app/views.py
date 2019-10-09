from django.shortcuts import render, redirect
from django.contrib import messages, sessions
import bcrypt

from .models import User, Trip

def register_page(request):
    return render(request, "take_a_hike_app/index.html")

def login_page(request):
    return render(request, "take_a_hike_app/login.html")

def register(request):
    password_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.warning(request, value, extra_tags="register")
            print(key, value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = password_hash
        new_user = User.objects.create(first_name=first_name, last_name = last_name, email=email, password=password)
        request.session['name'] = request.POST['first_name']
        request.session['user_id'] = new_user.id
        print(request.session['user_id'])
        return redirect('/trailhead')

def login(request):
    try: user = User.objects.get(email=request.POST['email_login'])
    except: 
        messages.warning(request, 'Account does not exist. Please register', extra_tags='login')
        return redirect('/login')
    if bcrypt.checkpw(request.POST['password_login'].encode(), user.password.encode()):
        print("password match")
        request.session['name'] = user.first_name
        request.session['user_id'] = user.id
        print(request.session['user_id'])
        return redirect('/trailhead')
    else:
        messages.warning(request, 'Password incorrect.', extra_tags='login')
        return redirect('/login')

def main(request):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_trips": Trip.objects.all(),
    }
    return render(request, 'take_a_hike_app/trailhead.html', context)

def add_bucket(request):
    name = request.POST['name']
    user = request.session['user_id']
    new_bucket = Bucket_list.objects.create(name=name, user=user)
    return redirect('/trailhead')

def new_trip(request):
    return render(request, 'take_a_hike_app/add_trip.html')

def create_trip(request):
    name = request.POST['name']
    location = request.POST['location']
    date = request.POST['date']
    length = request.POST['length']
    new_trip = Trip.objects.create(name=name, location=location, date=date, length=length)
    user = Trip.objects.get(id=new_trip.id)
    user.users = request.POST['user']
    user.save()
    return redirect(f'/trip/{new_trip.id}')

def trip(request, id):
    print("printing trip id:", id)
    trip = Trip.objects.get(id=id)
    context = {
        "trip": Trip.objects.get(id=id),
        "all_users": User.objects.all()
    }
    return render(request, 'take_a_hike_app/trip.html', context)

def cancel_trip(request, id):
    print("printing trip id:", id)
    cancel_trip = Trip.objects.get(id=id)
    cancel_trip.delete()
    return redirect('/trailhead')

def add_hiker(request):
    user_id = request.POST['this_user']
    trip_id = request.POST['this_trip']
    current_user = User.objects.get(id=user_id)
    current_trip = Trip.objects.get(id=trip_id)
    current_trip.users.add(current_user)
    print(current_user)
    return redirect(f'/trip/{trip_id}')

def trips(request):
    context = {
        "all_trips": Trip.objects.all()
    }
    return render(request, 'take_a_hike_app/all_trips.html', context)

def logout(request):
    try:
        del request.session['user_id']
        del request.session['name']
    except KeyError:
        pass
    return redirect('/')

