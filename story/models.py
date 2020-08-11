from django.db import models


class Media(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=256)
    acronym = models.CharField(max_length=10, blank=True, null=True)
    alias = models.CharField(max_length=256, blank=True, null=True)
    political_party = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def connected_people(self):
        person_details = self.tagged_person_details.all()
        return Person.objects.filter(pk__in=person_details.values_list('person_id', flat=True))

    def connected_people_count(self):
        return self.connected_people().count()

    def person_data(self):
        person_details = self.tagged_person_details.all()
        return {p: person_details.filter(person=p) for p in self.connected_people()}

    def connected_institutions(self):
        institution_details = self.tagged_institution_details.all()
        return Institution.objects.filter(pk__in=institution_details.values_list('institution_id', flat=True))

    def connected_institutions_count(self):
        return self.connected_institutions().count()

    def institution_data(self):
        institution_details = self.tagged_institution_details.all()
        return {i: institution_details.filter(institution=i) for i in self.connected_institutions()}

    def connected_events(self):
        return self.tagged_events.all()

    def connected_events_count(self):
        return self.connected_events().count()

    def total_connections(self):
        return self.connected_institutions_count() + self.connected_events_count() + self.connected_people_count()


class PoliticalParty(Institution):
    class Meta:
        proxy = True
        verbose_name_plural = 'Political parties'


class Person(models.Model):
    name = models.CharField(max_length=256)
    alias = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'People'

    def connected_people(self):
        person_details = self.tagged_person_details.all()
        return Person.objects.filter(pk__in=person_details.values_list('person_id', flat=True))

    def connected_people_count(self):
        return self.connected_people().count()

    def person_data(self):
        person_details = self.tagged_person_details.all()
        return {p: person_details.filter(person=p) for p in self.connected_people()}

    def connected_institutions(self):
        institution_details = self.tagged_institution_details.all()
        return Institution.objects.filter(pk__in=institution_details.values_list('institution_id', flat=True))

    def connected_institutions_count(self):
        return self.connected_institutions().count()

    def institution_data(self):
        institution_details = self.tagged_institution_details.all()
        return {i: institution_details.filter(institution=i) for i in self.connected_institutions()}

    def connected_events(self):
        return self.tagged_events.all()

    def connected_events_count(self):
        return self.connected_events().count()

    def total_connections(self):
        return self.connected_institutions_count() + self.connected_events_count() + self.connected_people_count()


class AffiliationStatus(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Affiliation statuses'


class InstitutionAffiliation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='affiliations')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    title = models.CharField(max_length=512, blank=True, null=True)
    status = models.ForeignKey(AffiliationStatus, on_delete=models.SET_NULL, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person.name} - {self.institution.name}'


class PoliticalPartyAffiliation(InstitutionAffiliation):

    class Meta:
        proxy = True


class Title(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='titles')
    title = models.CharField(max_length=512)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person.name} - {self.title}'


class Event(models.Model):
    name = models.CharField(max_length=256)
    details = models.TextField()
    date_str = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    tagged_persons = models.ManyToManyField(Person, blank=True, related_name='tagged_events')
    tagged_institutions = models.ManyToManyField(Institution, blank=True, related_name='tagged_events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def tagged_person_details_string(self):
        return ', '.join(p.person.name for p in self.tagged_person_details.all())

    def tagged_persons_string(self):
        return ', '.join(p.name for p in self.tagged_persons.all())

    def tagged_institution_details_string(self):
        return ', '.join(str(i.institution) for i in self.tagged_institution_details.all())

    def tagged_institutions_string(self):
        return ', '.join(str(i) for i in self.tagged_institutions.all())

    def connected_people(self):
        person_details = self.tagged_person_details.all()
        return Person.objects.filter(
            pk__in=person_details.values_list('person_id', flat=True)) | self.tagged_persons.all()

    def connected_people_count(self):
        return self.connected_people().count()

    def person_data(self):
        person_details = self.tagged_person_details.all()
        return {p: person_details.filter(person=p) for p in self.connected_people()}

    def connected_institutions(self):
        institution_details = self.tagged_institution_details.all()
        return Institution.objects.filter(
            pk__in=institution_details.values_list('institution_id', flat=True)) | self.tagged_institutions.all()

    def connected_institutions_count(self):
        return self.connected_institutions().count()

    def institution_data(self):
        institution_details = self.tagged_institution_details.all()
        return {i: institution_details.filter(institution=i) for i in self.connected_institutions()}

    def total_connections(self):
        return self.connected_institutions_count() + self.connected_people_count()


class PersonDetail(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='details')
    details = models.TextField()
    tagged_persons = models.ManyToManyField(Person, blank=True, related_name='tagged_person_details')
    tagged_events = models.ManyToManyField(Event, blank=True, related_name='tagged_person_details')
    tagged_institutions = models.ManyToManyField(Institution, blank=True, related_name='tagged_person_details')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person.name} - {self.details[:48]}'

    def tagged_persons_string(self):
        return ', '.join(p.name for p in self.tagged_persons.all())

    def tagged_events_string(self):
        return ', '.join(e.name for e in self.tagged_events.all())

    def tagged_institutions_string(self):
        return ', '.join(str(i) for i in self.tagged_institutions.all())

    def details_short(self):
        return self.details[:30]

    def name(self):
        return self.person.name


class InstitutionDetail(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='details')
    details = models.TextField()
    tagged_persons = models.ManyToManyField(Person, blank=True, related_name='tagged_institution_details')
    tagged_events = models.ManyToManyField(Event, blank=True, related_name='tagged_institution_details')
    tagged_institutions = models.ManyToManyField(Institution, blank=True, related_name='tagged_institution_details')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.institution.name} - {self.details[:48]}'

    def tagged_persons_string(self):
        return ', '.join(p.name for p in self.tagged_persons.all())

    def tagged_events_string(self):
        return ', '.join(e.name for e in self.tagged_events.all())

    def tagged_institutions_string(self):
        return ', '.join(str(i) for i in self.tagged_institutions.all())

    def details_short(self):
        return self.details[:30]

    def name(self):
        return self.institution.name


class PoliticalPartyDetail(InstitutionDetail):
    class Meta:
        proxy = True