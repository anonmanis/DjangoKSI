import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ujian_praktikum_1174043.settings')

import django

django.setup()

import random
from ujian_aplikasi_1174043.models import User
from faker import Faker

fakegen = Faker()

def po_1174043(N=30):
    for entry in range (N):
        firstname = fakegen.first_name_male()
        lastname = fakegen.last_name()
        email = fakegen.email()
        user = User.objects.get_or_create(firstname=firstname, lastname=lastname, email=email)[0]
        user.save()

if __name__=='__main__':
    print("Populating the database.....Please Wait!")
    po_1174043(30)
    print("Populating Complete!")