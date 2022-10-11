from pyexpat import model
from re import M
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Application(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    commence = models.DateField()
    firstName = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200, default='')
    othernames = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    dob = models.DateField()
    placeOfBirth = models.CharField(max_length=200)
    sex = models.CharField(max_length=200, choices=GENDER_CHOICES)
    maritalStatus = models.CharField(max_length=200)
    noOfChildren = models.PositiveBigIntegerField(blank=True)
    religion = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    nokphone = models.CharField(max_length=500)
    naddress = models.CharField(max_length=500)
    relationship = models.CharField(max_length=500)
    institution1 = models.CharField(max_length=500)
    placeAndCountry = models.CharField(max_length=500)
    datefrom = models.CharField(max_length=100)
    certificate1 = models.FileField(max_length=100)
    institution2 = models.CharField(max_length=500, blank=True)
    certificate2 = models.FileField(blank=True)
    employername = models.CharField(max_length=500)
    employeraddress = models.CharField(max_length=500)
    appointmentdate = models.CharField(max_length=500, blank=True)
    salary = models.IntegerField(blank=True)
    post = models.CharField(max_length=500)
    post2 = models.CharField(max_length=500)
    employername2 = models.CharField(max_length=500)
    employmentName = models.CharField(max_length=500)
    salary2 = models.IntegerField()
    submitdate = models.DateField()
    Signature = models.FileField()

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return self.firstName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.firstName)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('application', args=[self.slug])