from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # for login
from django.views.decorators.cache import cache_control  # For Security
from App.models import Patient, Call  # import from models.py
from django.contrib import messages  # for the message inside the function
from django.http import HttpResponseRedirect
from django.db.models import Q  # for search
from django.core.paginator import Paginator  # for pagination

# =============== FRONTEND  SECTION ===============
# Function to render the home page
@cache_control(no_cache=True, must_revalidate=True,
               no_store=True)  # For Security
def frontend(request):
    return render(request, 'frontend.html')


# =============== BACKEND SECTION ===============
# Function to render the page all patients(backend)
@cache_control(no_cache=True, must_revalidate=True,
               no_store=True)  # For Security
@login_required(login_url='login')
def backend(request):
   # if for search
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone=q) | Q(email=q) | Q(
                diagnosis=q) | Q(age=q) | Q(gender=q) | Q(note=q)
        ).order_by('-created_at')
    else:
        all_patient_list = Patient.objects.all().order_by('-created_at')

    # for pagination
    paginator = Paginator(all_patient_list, 10)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)

    # this line is for count the total number of patients
    total = Patient.objects.all().count()

    return render(request, 'backend.html', {'patients': all_patient, 'count': total})


# Function to Add new patient
@cache_control(no_cache=True, must_revalidate=True,
               no_store=True)  # For Security
@login_required(login_url='login')
def add_patient(request):
    if request.method == "POST":

        email = request.POST['email']

        if Patient.objects.filter(email=email).exists():
            messages.error(request, "Email already registered !")
            return render(request, 'add.html')

        elif request.POST.get('name') \
                and request.POST.get('phone') \
                and request.POST.get('email') \
                and request.POST.get('age') \
                and request.POST.get('gender') \
                and request.POST.get('diagnosis') \
                or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.diagnosis = request.POST.get('diagnosis')
            patient.note = request.POST.get('note')
            patient.save()

            messages.success(request, "Patient Added successfully!")
            return HttpResponseRedirect('/backend')
    else:
        return render(request, 'add.html')

# Function to access the Patient individualy
@cache_control(no_cache=True, must_revalidate=True,
               no_store=True)  # For Security
@login_required(login_url='login')
def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if patient != None:
        return render(request, 'edit.html', {'patient': patient})


# Function to edit the Patient
@cache_control(no_cache=True, must_revalidate=True,
               no_store=True)  # For Security
@login_required(login_url='login')
def edit_patient(request):
    if request.method == 'POST':
        patient = Patient.objects.get(id=request.POST.get('id'))
        if patient != None:

            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.diagnosis = request.POST.get('diagnosis')
            patient.note = request.POST.get('note')
            patient.save()

            messages.success(request, "Patient updated successfully!")
            return HttpResponseRedirect('/backend')

# Function to delete Patient
@cache_control(no_cache=True, must_revalidate=True,
               no_store=True)  # For Security
@login_required(login_url='login')
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    messages.success(request, "Patient removed successfully!")
    return HttpResponseRedirect('/backend')

# SUPPORT
@cache_control(no_cache=True, must_revalidate=True,
               no_store=True)  # For Security
@login_required(login_url='login')
def support(request):
    if request.method == 'POST':

        support = Call()

        user = request.POST.get('user')
        message = request.POST.get('message')
        terms = request.POST.get('terms')
        option = request.POST.get('option')
        reason = request.POST.get('reason')

        support.user = user
        support.message = message
        support.terms = terms
        support.option = option
        support.reason = reason

        support.save()
        messages.success(
            request, "We`ll review your request as soon as possible !")
        return HttpResponseRedirect('/backend')
    else:
        return HttpResponseRedirect('/backend')
