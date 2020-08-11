from django.contrib import admin
from story.models import PoliticalParty, Person, PersonDetail, AffiliationStatus, \
    InstitutionAffiliation, Event, Institution, Title, InstitutionDetail, PoliticalPartyAffiliation, \
    PoliticalPartyDetail


admin.site.register(AffiliationStatus)
admin.site.register(InstitutionAffiliation)
admin.site.register(Title)


@admin.register(PersonDetail)
class PersonDetailAdmin(admin.ModelAdmin):
    raw_id_fields = ('tagged_persons', 'tagged_events', 'tagged_institutions')
    readonly_fields = ('tagged_persons_string', 'tagged_events_string', 'tagged_institutions_string')
    list_display = ('name', 'details', 'tagged_persons_string', 'tagged_events_string', 'tagged_institutions_string')
    ordering = ('person__name', )


@admin.register(InstitutionDetail)
class InstitutionDetailAdmin(admin.ModelAdmin):
    raw_id_fields = ('tagged_persons', 'tagged_events', 'tagged_institutions')
    readonly_fields = ('tagged_persons_string', 'tagged_events_string', 'tagged_institutions_string')
    list_display = ('name', 'details', 'tagged_persons_string', 'tagged_events_string', 'tagged_institutions_string')


class PersonDetailInline(admin.TabularInline):
    model = PersonDetail


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ('name', 'alias')
    inlines = [
        PersonDetailInline
    ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ('name', 'details', 'date')
    list_display = ('name', 'details', 'date_str', 'date', 'tagged_person_details_string', 'tagged_persons_string',
                    'tagged_institution_details_string', 'tagged_institutions_string')
    raw_id_fields = ('tagged_persons', 'tagged_institutions')
    readonly_fields = ('tagged_person_details_string', 'tagged_institution_details_string')


class InstitutionDetailInline(admin.TabularInline):
    model = InstitutionDetail


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    search_fields = ('name', 'acronym', 'alias')
    inlines = [
        InstitutionDetailInline
    ]


@admin.register(PoliticalPartyAffiliation)
class PoliticalPartyAffiliationAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.objects.filter(institution__political_party=True)


@admin.register(PoliticalPartyDetail)
class PoliticalPartyDetailAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.objects.filter(institution__political_party=True)


@admin.register(PoliticalParty)
class PoliticalPartyAdmin(admin.ModelAdmin):
    inlines = [
        InstitutionDetailInline
    ]

    def get_queryset(self, request):
        return self.model.objects.filter(political_party=True)