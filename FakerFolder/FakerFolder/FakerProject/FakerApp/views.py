from django.shortcuts import render
from .models import Employee
from faker import Faker

# Create your views here.
fake = Faker()

def fakeDataView(request):
    data = []
    for i in range(20):
        fname = fake.name()
        faddress = fake.address()
        femail = fake.email()
        fsalary = fake.random_number(digits=5)
        emp = Employee.objects.get_or_create(name = fname,address = faddress, email = femail, salary = fsalary)
        data.append(emp)
    return render(request, 'FakerApp/show.html', {'data':data})


