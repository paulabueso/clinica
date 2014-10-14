from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from clinicadental.forms import AppointmentForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request, 'home.html')


# def map(request):
#     return render(request, 'map.html')
#
# def map1(request):
#     return render(request, 'map1.html')


def tratamientos(request):
    return render(request, 'tratamientos.html')


def contactanos(request):
    return render(request, 'contactanos.html')


def pidetucita(request):
    form = AppointmentForm()
    data = {'form': form}
    return render(request, 'pidetucita.html', data)

def chat(request):
    return render(request, 'chat.html')

def mail(request):
    return render(request, 'mail.html')

def direccion(request):
    return render(request, 'direccion.html')


@csrf_exempt
def chat(request, sender, receiver):
    if request.method == "POST":
        # Should use full variable names for readability (i.e. sender_user and receiver_user)
        s = User.objects.get(pk=int(sender))
        r = User.objects.get(pk=int(receiver))
        message = Messages.objects.create(message=request.POST['message'], sender=s, receiver=r)

        return HttpResponse(json.dumps(message.message, message.sender), content_type='application/json')
    data = {"sender": sender, "receiver": receiver}
    return render(request, 'chat.html', data)


def get_chat(request, sender, receiver):
    s = User.objects.get(pk=int(sender))
    r = User.objects.get(pk=int(receiver))
    messages = Messages.objects.filter(sender=s, receiver=r)
    # response = serializers.serialize('json', [messages])
    res = ""
    for message in messages:
        res += '<p>' + message.message + '</p>'
    return HttpResponse(json.dumps(res), content_type='application/json')



