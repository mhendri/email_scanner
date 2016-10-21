from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import EmailForm
from main_app.models import Flagged, UploadEmail


# Create your views here.
def index(request):
    print('index')
    return render(request, 'home_page.html')#, {'form': form})

def process_email(request):
    field_dict = {}
    flagged = False
    for field in request.POST.items():
        field_dict[str(field[0])] = str(field[1])
    allEmails = UploadEmail.objects.filter(email_To=field_dict['to'], email_From=field_dict['from'])
    if len(allEmails) > 0:
        flagged = Flagged(email_From=field_dict['from'], email_To=field_dict['to'],
                            subject=field_dict['subject'], body=field_dict['body'],
                            reason='Communication between privileged users.')
        flagged.save()
        return render(request, 'email_response.html', { 'flagged': 'comms' })
    else:
        words = compare(field_dict['body'])
        if (len(words) > 0):
            flagged = Flagged(email_From=field_dict['from'], email_To=field_dict['to'],
                                subject=field_dict['subject'], body=field_dict['body'],
                                reason='The following words were flagged:' + str(words))
            flagged.save()
            return render(request, 'email_response.html', { 'flagged': 'words' })
        else:
            return render(request, 'email_response.html', { 'flagged': 'False' })

def compare(body):
    flagged_words = list()
    with open('master_dictionary.txt','r') as f:
        for line in f:
            for word in line.split():
                if word in body:
                    flagged_words.append(word)
    return flagged_words
