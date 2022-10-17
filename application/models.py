from email.policy import default
from pyexpat import model
from re import M
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import datetime


class Application(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    SESSION_CHOICES = (
        ('2022/2023', '2022/2023'),
        ('2023/2024', '2023/2024'),
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
    session = models.CharField(max_length=200, choices=SESSION_CHOICES, default='2022/2023')
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
    registration_number = models.CharField(max_length=250, null=True, blank=True)
    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return f'{self.firstName} Application'

    
    def get_absolute_url(self):
            return reverse('application', args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.firstName)
        today = datetime.date.today()
        year = today.strftime("%Y")
        if not self.registration_number:
            number = ("LocGov", year, str(self.id))
            self.registration_number = '/'.join(number)
            print("reg ", self.registration_number)
        super().save(*args, **kwargs)

   