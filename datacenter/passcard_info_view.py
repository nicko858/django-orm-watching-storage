from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import timedelta
from datacenter.storage_information_view import get_duration
from django.utils.timezone import localtime


def is_strange(duration):
    return duration > timedelta(hours=1)


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    duration = None
    for visit in passcard_visits:
        if visit.leaved_at:
            duration = get_duration(
                entered_at=visit.entered_at,
                leaved_at=visit.leaved_at,
                )
        else:
            duration = get_duration(
                visit=visit,
                entered_at=visit.entered_at,
                )
        this_passcard_visits.append({
            'entered_at': localtime(visit.entered_at),
            'duration': duration,
            'is_strange': is_strange(duration),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
