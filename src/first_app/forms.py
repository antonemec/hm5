from django.forms import ModelForm

from first_app.models import Student, Group, Teacher


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class TeachersAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
