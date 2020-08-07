from django.shortcuts import render, Http404
from story.models import Person, PersonDetail, Institution, InstitutionDetail


def all_people(request):
    people = Person.objects.all().order_by('name')
    return render(request, 'story/people.html', {'people': people})


def all_institutions(request):
    institutions = Institution.objects.all().order_by('name')
    return render(request, 'story/institutions.html', {'institutions': institutions})


def person(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        details = person.details.all()
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'story/person.html', {'person': person,
                                               'details': details,
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
    return render(request, 'story/institution.html', {'institution': institution,
                                                      'details': details,
                                                      })


def institution_detail(request, institution_detail_id):
    try:
        institution_detail = InstitutionDetail.objects.get(pk=institution_detail_id)
    except InstitutionDetail.DoesNotExist:
        raise Http404("Institution detail does not exist")
    return render(request, 'story/institution-detail.html', {'detail': institution_detail,
                                                        })