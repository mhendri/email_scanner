from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EmailForm


# Create your views here.
def index(request):
    print('index')
    return render(request, 'home_page.html')#, {'form': form})

def process_email(request):
    field_dict = {}
    flagged = False
    for field in request.POST.items():
        field_dict[str(field[0])] = str(field[1])
    # if not flagged:
    #     flagged = Flagged(from=field_dict['from'], to=field_dict['to'],
    #                         subject=field_dict['subject'], body=field_dict['body'],
    #                         reason='some reason')
    #     print(flagged)
    # print(unicode(request.POST.items()))
    return HttpResponseRedirect('/email_sent/')

def email_sent(request):
    return render(request, 'email_sent.html')
