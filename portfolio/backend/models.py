from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    entry_year = models.IntegerField()
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='social_icons', blank=True)
    url = models.CharField(max_length=100)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)


class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='service_icons', blank=True)
    service_description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonial_pics', blank=True)
    testimonial = models.TextField(max_length=500)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Knowledge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AcquiredSkill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('SkillCategory', on_delete=models.CASCADE)
    level = models.IntegerField()
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='certificate_pics', blank=True)
    year = models.IntegerField()
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    year = models.IntegerField()
    user = models.ForeignKey('accounts.User',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Resume(models.Model):
    domain = models.CharField(max_length=100)
    project = models.ManyToManyField('Project')
    certificate = models.ManyToManyField(
        'Certificate')
    knowledge = models.ManyToManyField('Knowledge')
    acquired_skill = models.ManyToManyField(
        'AcquiredSkill')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
