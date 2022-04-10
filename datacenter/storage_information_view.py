#from tkinter import N
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import datetime, timezone
from django.utils.timezone import localtime


def get_duration(visit=None, entered_at=None, leaved_at=None):
    now = localtime(datetime.now(timezone.utc).replace(microsecond=0))
    duration = None
    if entered_at and leaved_at:
        duration = leaved_at - entered_at
    else:
        entered_at = localtime(visit.entered_at)
        duration = now - entered_at
    return duration


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visit = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': str(get_duration(visit=visit)),
        }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
