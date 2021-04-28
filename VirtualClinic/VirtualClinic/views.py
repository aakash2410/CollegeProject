import json
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .Dis_Test import RFTest
from appointment.models import Doctor

# app.config["MAIL_SERVER"] = 'smtp.gmail.com'
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USERNAME"] = 'ronshawn29@gmail.com'
# app.config['MAIL_PASSWORD'] = 'ViS29@@@'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

d = RFTest()
dict1 = {}
def details(request):
    # email2 = 'dhandesagar78@gmailcom'

    # print(email2)
    # msg = Message('OTP', sender='username@gmail.com', recipients=[email2])
    # msg.body = str('Appointment Booked')
    # mail.send(msg)
    return render(request, 'details.html', dict1)

def index(request):
    
    gdict = {}
    b = d.get_dis()
    gdict = {
        'b': b
    }
    return render(request, 'indexsym.html', gdict)

def predictdis(request):
    b = request.POST.get('sym')
    global dict1
    dict1 = {}
    a = []
    str = ''
    for i in b:
        str += i
        if i == ' ':
            a.append(int(str))
            str = ''
    a.append(int(str))
        
    # print(a)
    # a = list(map(int, input().split()))
    x = len(a)
    for i in  range(x,17):
        a.append(0)
    print(a)
    doctors = Doctor.objects.all()

    result = d.RF_Predict(a)[0]
    
    dict1 = {
        'a':result,
        'doctors':doctors,
        'n':range(len(list(doctors)))

    }
    print(dict1)
    print(result)
    return render(request, 'FindMyDoc.html', dict1)