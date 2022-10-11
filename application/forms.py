from .models import Application
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = "__all__"
        widgets = {
            'commence': DateInput(),
            'dob': DateInput(),
            'appointmentdate': DateInput(),
            'submitdate': DateInput(),
        }
        labels = {
            'commence': "Commence From",
            'firstName': "First Name",
            'othernames': "Other Names",
            'maritalStatus': "Marital Status",
            'noOfChildren': "No Of Children",
            'dob': "Date of Birth",
            'placeOfBirth': "Place of Birth",
            'nokphone': "Next of Kin Phone Number",
            'naddress': "Next of Kin Address",
            'institution1': "Institution",
            'institution2': "Institution",
            'placeAndCountry': "Place And Country",
            'datefrom': "Date (From ----- To) ",
            'employeraddress': "Employer Address ",
            'appointmentdate': "Appointment Date",
            'post2': "Title of Post",
            'employername2': "Name of Employer",
            'employmentName': "Employment Name",
            'salary2': "Salary",
            'submitdate': "Date",
            'salary': "Present Salary",
            'post': "Title of post Currently held"
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2'
