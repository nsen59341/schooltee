from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from teeapp.models import Assignment,Permormance
import random
import copy
from django.contrib.sessions.models import Session

# Create your views here.

@login_required
def home(request):
    if request.method=='GET':
        studId = request.session['student_id']
        # print('studId', studId)
        # studId = 1
        url = 'http://127.0.0.1:8000/teeapp/lessons?studId='+str(studId)
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            # print('data',result[0]['teacher'])
        return render(request, 'home.html', {'data':result})
        # return HttpResponse("Home")

def check_ans(request):
    sel_ans = request.POST['sel_ans']
    id = int(request.POST['id'])
    # print('ans ',sel_ans,request.session['answers'][id])
    correct = sel_ans==request.session['answers'][id]
    return JsonResponse({'correct': correct})

def stote_points(request):
    try:
        percentage = request.POST['percentage']
        assignment_id = request.POST['assignment_id']
        student_id = request.session['student_id']

        # Check the performance already exixts or not
        geturl = "http://127.0.0.1:8000/teeapp/performances?assignment_id="+str(assignment_id)+"&student_id="+str(student_id)
        response2 = requests.get(geturl)
        result2 = response2.json()
        # print("Result 2:", result2)
        if response2.status_code == 200:
            if result2['percentage']:
                # If exists then update
                puturl = "http://127.0.0.1:8000/teeapp/performance/"+str(result2['id'])
                data2 = {
                    'student': student_id,
                    'assignment': assignment_id,
                    'percentage': percentage
                }
                response = requests.put(puturl, data=data2)
            
                return JsonResponse({'success': True, 'message': 'Data has been updated successfully.'})

            else:
                # If not exists then add percentage
                posturl = "http://127.0.0.1:8000/teeapp/performances"
                data3 = {
                    'student': student_id,
                    'assignment': assignment_id,
                    'percentage': percentage
                }
                requests.post(posturl, data=data3)

                # # Debugging the response
                # print("Response status code:", response.status_code)
                # print("Response content:", response.text)

                return JsonResponse({'success': True, 'message': 'Data has been stored successfully.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e) })

def check_sess(request):
    sessions = Session.objects.all()

    # Loop through each session and decode the data
    for session in sessions:
        data = session.get_decoded()
        print(data)
        
    return HttpResponse(1)

@login_required
def assignment(request, assid):
    assignment = Assignment.objects.get(id=assid)
    response = requests.get(assignment.link)
    if response.status_code!=200:
        raise Exception(response)
    questns = response.json()
    assignments = questns['results']
    request.session['answers'] = []
    for assignment in assignments:
        random_position = random.randint(0, len(assignment['incorrect_answers']))
        assignment['answers'] = copy.deepcopy(assignment['incorrect_answers'])
        assignment['answers'].insert(random_position, assignment['correct_answer'])
        assignment['answers'] = [(i,ans) for i,ans in enumerate(assignment['answers'])]
        request.session['answers'].append(assignment['correct_answer'])
    assignments = [(k,ass) for k,ass in enumerate(assignments)]
    # if 'answers' not in request.session:
    #     request.session['answers'] = {}
    # for ind,ass in assignments:
    #     request.session['answers'][ind] = ass['correct_answer']

    return render(request, 'assignment.html', {'assid':assid, 'assignments':assignments})

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    initval = {'username':'', 'password': ''}
    loginForm = AuthenticationForm(initial=initval)
    if request.method=='POST':
        loginForm = AuthenticationForm(request, data=request.POST)
        if loginForm.is_valid():
            user = loginForm.get_user()
            url = 'http://127.0.0.1:8000/teeapp/students?email='+str(user.email)
            response = requests.get(url)
            if response.status_code == 200:
                result = response.json()
                request.session['student_id'] = result['id']
                login(request,user)
            else:
                return HttpResponse(request, "Unable to login")
                
            return redirect('home')
        
    return render(request, 'login.html', {'loginForm': loginForm})

def registrationuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    initval = {'email':'', 'username':'', 'password1': '', 'password2': ''}
    registrationForm = CustomUserCreationForm(initial=initval)
    if request.method=='POST':
        registrationForm = CustomUserCreationForm(request.POST)
        if registrationForm.is_valid():
            user = registrationForm.save()
            student = {'name': user.username, 'email': user.email}

            url = 'http://127.0.0.1:8000/teeapp/students'

            try:
                response = requests.post(url, json=student)
                # print('Response:', response)
                if response.status_code == 201:
                    result = response.json()
                    # print('data',result)
                    request.session['student_id'] = result['id']
                return redirect('home')
            except requests.exceptions.RequestException as e:
                return HttpResponse(request, e)
       
    return render(request, 'registration.html', {'regForm': registrationForm})

def logoutuser(request):
    logout(request)
    return redirect('login')