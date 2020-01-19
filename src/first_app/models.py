from django.db import models
from faker import Faker
import random

# Create your models here.
"""
CREATE TABLE first_app_student( first_name varchar(20));
"""


# --------------------------------------------------------------------------------------------------------------
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16)  # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)
    group_id = models.CharField(max_length=10, null=True, blank=True)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    def get_all_info(self):
        return f'{self.first_name} {self.last_name}' \
               f'<br>Birth date: {self.birth_date}' \
               f'<br>Email: {self.email}' \
               f'<br>Phone: {self.telephone}'

    @classmethod
    def generate_students(cls):
        fake = Faker()
        student = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      birth_date=fake.date_of_birth(tzinfo=None, minimum_age=10, maximum_age=60),
                      email=fake.email(),
                      telephone=fake.phone_number())
        student.save()
        return student


# --------------------------------------------------------------------------------------------------------------
class Group(models.Model):
    group_name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    group_id = models.CharField(max_length=10, null=True, blank=True)

    def get_info(self):
        r = self.description.split('.')
        return f"{self.group_name}({self.group_id}) " \
               f"<br>_________________________<br>" \
               f"Description: \n{'<br>'.join(r)}"

    @classmethod
    def generate_group(cls):
        fake = Faker()
        seria = ['AA', 'AB', 'BA', 'BB']
        gr_num = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '00']
        group = cls(group_name=f'{fake.first_name()} INC',
                    description=fake.text()',
                    group_id=f'{random.choice(seria)+random.choice(gr_num)} - {random.choice(gr_num)}')
        group.save()
        return group


# --------------------------------------------------------------------------------------------------------------
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    telephone = models.CharField(max_length=16)

    def get_info(self):
        return f'{self.first_name} {self.last_name}' \
               f'<br>Email: {self.email}' \
               f'<br>Phone: {self.telephone}'

    @classmethod
    def generate_teacher(cls):
        fake = Faker()
        teacher = cls(first_name=f'{fake.first_name()}',
                      last_name=f'{fake.last_name()}',
                      email=f'{fake.email()}',
                      telephone=f'{fake.phone_number()}')
        teacher.save()
        return teacher
# --------------------------------------------------------------------------------------------------------------
