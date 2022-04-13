from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import timedelta
from django.utils.timezone import localtime


def is_strange(duration):
    return duration > timedelta(hours=1)


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    serialized_passcard_visits = []
    for visit in passcard_visits:
        serialized_passcard_visits.append({
            'entered_at': localtime(visit.entered_at),
            'duration': visit.get_duration(),
            'is_strange': is_strange(visit.get_duration()),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
