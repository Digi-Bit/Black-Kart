from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
MERCHANT_KEY = 'Jx%JSQa!#@%dEVtJ'

# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    return render(request, 'home.html')



def contact(request):
    if request.method=='POST':
        # print("This is post")
        name = request.POST['name']
        # lastname = request.POST['lastname']
        email = request.POST['email']
        # subject = request.POST['subject']
        message = request.POST['message']
        # print(name, email, message)
        ins = Contact(name=name, email=email, message=message)
        ins.save()
        print("The data has been written to the db")
    
    # return HttpResponse("This is my contactpage (/contact)")
    return render(request, 'contact.html')
    param_dict = {
        'MID': 'ToRYSY87407031138273',
        'ORDER_ID': '',
        'TXN_AMOUNT': str(amount),
        'CUST_ID': 'email',
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL': 'http://127.0.0.1:8000.blackkart/handlerequest/',
    }
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict)
    return render(request, 'blackkart/paytm.html', {'param_dict': param_dict})

def register(request):
    return render(request, 'register.html')
@csrf_exempt
def handlerequest(request):
    return HttpResponse('done')
    pass

