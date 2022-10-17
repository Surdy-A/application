from email.mime import application
from mmap import PAGESIZE
from django.http import HttpResponseRedirect
from django.shortcuts import render
from reportlab.lib.units import inch

from localgov.settings import BASE_DIR, STATIC_URL

from .forms import ApplicationForm, PrintForm
import os
from .models import Application
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.conf import settings


def form_view(request):
    context = {}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
     # create object of form
        form = ApplicationForm(request.POST or None, request.FILES or None)
        # check if form data is valid
        if form.is_valid():
            print("value ", form.cleaned_data['commence'])
        # save the form data to model
            form.save()
            messages.success(request, 'Form submission successful')

            return HttpResponseRedirect('/')

    else:
        form = ApplicationForm()
    context['form'] = form
    return render(request, "index.html", context)

def generatePDF(request, id):
    buffer = io.BytesIO()
    x = canvas.Canvas(buffer)
    imgdir = [os.path.join(BASE_DIR, 'static\\assets\\img\\oaulogo.png')]
    x.drawImage(imgdir[0], 40, 750, width=72, height=72)
    x.setFont('Helvetica', 20)
    x.drawString(130, 800, "OBAFEMI AWOLOWO UNIVERSITY, ILE-IFE")
    x.setFont('Helvetica', 12)
    x.drawString(
        130, 780, "DEPARTMENT OF LOCAL GOVERNMENT AND DEVELOPMENT STUDIES")
    application = Application.objects.get(id=id)
    app = """DIPLOMA APPLICATION FORM ({session})""".format(
        session=application.session)
    x.drawString(225, 766, app)

    txt1 = """
    Registration Number:                    {regNumber}
    Commencing from:                       {commence}
    First Name:                                   {firstName}
    Surname:                                      {surname}
    Other Name:                                 {othernames}
    Phone Number:                            {phone}
    State:                                            {state}
    Nationality:                                    {nationality}
    Place of Birth:                               {placeofbirth}
    Date of Birth:                                {dob}
    Sex:                                               {sex}
    Marital Status:                              {maritalStatus}
    Number of Children:                       {noofchildren}
    Religion:                                       {religion}
    Mail Address for Reply:                {email}
    Permanent Home Address:          {address}
    Next of Kin
    Name:                                          {nokname}
    Address:                                      {naddress}
    Phone Number:                           {nokphone}
    Relationship:                               {relationship}
    Educational Record
    Name of Institution:                    {institution1}
    Place and Country:                     {placeAndCountry}
    Date (From-To):                          {datefrom}
    Other Institution:                         {institution2}
    Employer Details
    Name:                                         {employername}
    Address:                                      {employeraddress}
    Date of Appointment:                  {appointmentdate}
    Present Salary:                           {salary}
    Title of post currently held:         {post}
    Details of previous employment (s) and post(s) held
    Title of Post:                                {post2}
    Name of Employer:                     {employername2}
    Salary:                                         {salary2}

    The University Accepts no obligation to provide accommodation for students 
    but will be willing to render advisory services to such students.
    I hereby undertake to observe the rules and regulations of the university 
    and to subject myself to discipline during my course of study.

    Signature: _________________________
    """.format(
        regNumber=application.registration_number,
        commence=application.commence,
        firstName=application.firstName,
        surname=application.surname,
        othernames=application.othernames,
        phone=application.phone,
        state=application.state,
        nationality=application.nationality,
        placeofbirth=application.placeOfBirth,
        dob=application.dob,
        sex=application.sex,
        maritalStatus=application.maritalStatus,
        noofchildren=application.noOfChildren,
        religion=application.religion,
        email=application.email,
        address=application.address,
        nokname=application.name,
        naddress=application.address,
        nokphone=application.nokphone,
        relationship=application.relationship,
        institution1=application.institution1,
        placeAndCountry=application.placeAndCountry,
        datefrom=application.datefrom,
        institution2=application.institution2,
        employername=application.employername,
        employeraddress=application.employeraddress,
        appointmentdate=application.appointmentdate,
        salary=application.salary,
        post=application.post,
        post2=application.post2,
        employername2=application.employername2,
        salary2=application.salary2
    )
    textobject = x.beginText()
    textobject.setTextOrigin(48, 726)
    x.setFont('Helvetica', 12)
    textobject.setFont("Helvetica", 14)
    textobject.textLines(txt1)
    x.drawText(textobject)
    x.showPage()
    x.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Local Government Diploma Application.pdf')


def print_view(request):
    context = {}
    registration_number = str(request.GET.get("registration_number"))
    print(registration_number)

    
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
     # create object of form
        form = PrintForm(request.POST or None, request.FILES or None)
        # check if form data is valid
        if form.is_valid():
            print("value ", form.cleaned_data['registration_number'])
        # save the form data to model
            #form.save()
            #messages.success(request, 'Form submission successful')

            return HttpResponseRedirect('/')

    else:
        form = PrintForm()
    context['form'] = form
    context['registration_id'] = registration_number
    return render(request, "print.html", context)