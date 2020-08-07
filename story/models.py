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
    tagged_institutions = models.ManyToManyField(Institution, blank=True, related_name='tagged_institutions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def tagged_person_details_string(self):
        return ', '.join(p.person.name for p in self.tagged_person_details.all())

    def tagged_persons_string(self):
        return ', '.join(p.name for p in self.tagged_persons.all())

    # def tagged_events_string(self):
    #     return ', '.join(e.name for e in self.tagged_events.all())

    def tagged_institution_details_string(self):
        return ', '.join(str(i.institution) for i in self.tagged_institution_details.all())

    def tagged_institutions_string(self):
        return ', '.join(str(i) for i in self.tagged_institutions.all())




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









class OldPoliticalParty(models.Model):
    name = models.CharField(max_length=256)
    acronym = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        dtr = self.name
        if self.acronym:
            dtr += f' ({self.acronym})'
        return dtr

    class Meta:
        verbose_name_plural = 'Political parties'


class PartyAffiliation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    political_party = models.ForeignKey(OldPoliticalParty, on_delete=models.CASCADE)
    title = models.CharField(max_length=512, blank=True, null=True)
    status = models.ForeignKey(AffiliationStatus, on_delete=models.SET_NULL, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person.name} - {self.political_party.name}'


class PartyDetail(models.Model):
    party = models.ForeignKey(OldPoliticalParty, on_delete=models.CASCADE)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.party.name} - {self.details[:48]}'