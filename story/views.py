from django.shortcuts import render, Http404
from story.models import Person, PersonDetail, Institution, InstitutionDetail, Event


def all_people(request):
    people = Person.objects.all().order_by('name')
    return render(request, 'story/people.html', {'people': people})


def all_institutions(request):
    institutions = Institution.objects.all().order_by('name')
    return render(request, 'story/institutions.html', {'institutions': institutions})

def all_events(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'story/events.html', {'events': events})


def person(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        details = person.details.all()
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    person_details = person.tagged_person_details.all()
    people = Person.objects.filter(pk__in=person_details.values_list('person_id', flat=True))
    person_data = {p: person_details.filter(person=p) for p in people}
    institution_details = person.tagged_institution_details.all()
    institutions = Institution.objects.filter(pk__in=institution_details.values_list('institution_id', flat=True))
    institution_data = {i: institution_details.filter(institution=i) for i in institutions}
    return render(request, 'story/person.html', {'person': person,
                                               'details': details,
                                                 'person_data': person_data,
                                                 'institution_data': institution_data
                                                 })


def person_detail(request, person_detail_id):
    try:
        person_detail = PersonDetail.objects.get(pk=person_detail_id)
    except PersonDetail.DoesNotExist:
        raise Http404("Person detail does not exist")
    return render(request, 'story/person-detail.html', {'detail': person_detail,
                                                        })


def institution(request, institution_id):
    try:
        institution = Institution.objects.get(pk=institution_id)
        details = institution.details.all()
    except Person.DoesNotExist:
        raise Http404("Institution does not exist")
    person_details = institution.tagged_person_details.all()
    people = Person.objects.filter(pk__in=person_details.values_list('person_id', flat=True))
    person_data = {p: person_details.filter(person=p) for p in people}
    institution_details = institution.tagged_institution_details.all()
    institutions = Institution.objects.filter(pk__in=institution_details.values_list('institution_id', flat=True))
    institution_data = {i: institution_details.filter(institution=i) for i in institutions}
    return render(request, 'story/institution.html', {'institution': institution,
                                                      'details': details,
                                                      'person_data': person_data,
                                                      'institution_data': institution_data,
                                                      })


def institution_detail(request, institution_detail_id):
    try:
        institution_detail = InstitutionDetail.objects.get(pk=institution_detail_id)
    except InstitutionDetail.DoesNotExist:
        raise Http404("Institution detail does not exist")
    return render(request, 'story/institution-detail.html', {'detail': institution_detail,
                                                        })


def event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        # details = institution.details.all()
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    person_details = event.tagged_person_details.all()
    persons = Person.objects.filter(pk__in=person_details.values_list('person_id', flat=True)) | event.tagged_persons.all()
    person_data = {p: person_details.filter(person=p) for p in persons}
    institution_details = event.tagged_institution_details.all()
    institutions = Institution.objects.filter(pk__in=institution_details.values_list('institution_id', flat=True)) | event.tagged_institutions.all()
    institution_data = {i: institution_details.filter(institution=i) for i in institutions}
    return render(request, 'story/event.html', {'event': event,
                                                'person_data': person_data,
                                                'institution_data': institution_data
                                                      # 'details': details,
                                                      })
