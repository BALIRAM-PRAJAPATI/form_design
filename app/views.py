from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Incident
from .forms import IncidentForm

# Signup View Function
def sign_up(request):
 if request.method == "POST":
  fm = SignUpForm(request.POST)
  if fm.is_valid():
   messages.success(request, 'Account Created Successfully !!') 
   user = fm.save()   
 else: 
  fm = SignUpForm()
 return render(request, 'signup.html', {'form':fm})

# Login View Function
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully !!')
          return HttpResponseRedirect('/dashboard/')
    else: 
      fm = AuthenticationForm()
    return render(request, 'userlogin.html', {'form':fm})
  else:
    return HttpResponseRedirect('/dashboard/')

# Dahsboard

def user_dashboard(request):
  if request.user.is_authenticated:
    #HttpResponse.set_cookie( “name”, request.user.first_name, max_age=60*60*24*10)
    #request.session['name'] = request.user.first_name   
    request.session['name'] = request.user.first_name
    return render(request, 'dashboard.html', {'name':request.user.first_name})
  else:
    return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
  logout(request)
  if 'name' in request.session:
    del request.session['name']
  return HttpResponseRedirect('/login/')

#report incident
def incident(request):
      if request.method == 'POST':
            form = IncidentForm(request.POST)
            if form.is_valid():
                  location = request.POST.get('location')
                  incident_department = request.POST.get('incident_department')
                  initial_severity = request.POST.get('initial_severity')
                  subincident_types = request.POST.get('subincident_types')
                  date_incident = request.POST.get('date')
                  time_incident = request.POST.get('time')
                  incident_location = request.POST.get('incident_location')
                  suspected_cause = request.POST.get('suspected_cause')
                  immediateaction_taken = request.POST.get('immediateaction_taken')
                  reported_by = request.POST.get('reported_by')
                  print(location,incident_department, initial_severity, subincident_types, date_incident, time_incident, incident_location, suspected_cause, immediateaction_taken, reported_by)
                  user_data = Incident(location = location, incident_department = incident_department, date_incident = date_incident, time_incident = time_incident, incident_location = incident_location, initial_severity = initial_severity, suspected_cause = suspected_cause, immediateaction_taken = immediateaction_taken, subincident_types = subincident_types, reported_by = reported_by)
                  name = request.session['name']
                  user_data.save()
                  messages.success(request, 'data stored successfully !!')                 
                  
      else:
            name = request.session['name']
            form = IncidentForm()            
      return render(request, 'incident.html', {'form':form, 'name':name})
