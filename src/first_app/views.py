from django.http import HttpResponseRedirect  # HttpResponse
from django.shortcuts import render
from first_app.models import Student, Group, Teacher
from first_app.forms import StudentsAddForm, TeachersAddForm, GroupsAddForm
from django.db.models import Q


# ----------------------------------------------------------------------------
# Вьюхи для студентов
# ----------------------------------------------------------------------------
def generate_student(request):
    student = Student.generate_students()
    response = f'{student.get_all_info()}'
    return render(request,
                  'gen_student.html',
                  context={'student_gen': response})


# ----------------------------------------------------------------------------
def students(request):
    queryset = Student.objects.all()
    # quarks = Student.objects.all()
    response = ''

    # print("request.GET.get('first_name')")
    fn = request.GET.get('data')
    if fn:
        queryset = queryset.filter(Q(first_name__startswith=fn) | Q(last_name__startswith=fn) | Q(email__startswith=fn))
    for student in queryset:
        response += student.get_all_info() + '<br> ______________ <br>'
        ''' quarks = quarks.filter(last_name__contains=fn)
        for student in quarks:
            response += student.get_all_info() + '<br> ______________ <br>'''
    # return queryset(response)
    # print('queryset.query')quarks
    # print(queryset.query)
    return render(request,
                  'students_list.html',
                  context={'students_list': response})


# ----------------------------------------------------------------------------
def students_add(request):

    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            print('DATA SAVE')
            return HttpResponseRedirect('/students/')
        else:
            print('TRY AGAIN')
            form = StudentsAddForm()
    else:
        form = StudentsAddForm()

    return render(request,
                  'students_add.html',
                  context={'form': form})


# ----------------------------------------------------------------------------
# Вьюхи для групп
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
def generate_group(request):
    group = Group.generate_group()
    response = f'{group.get_info()}'
    return render(request,
                  'gen_group.html',
                  context={'group_gen': response})


# ----------------------------------------------------------------------------
def groups(request):
    queryset = Group.objects.all()
    response = ''

    # print("request.GET.get('group_name')")
    fn = request.GET.get('data')
    if fn:
        queryset = queryset.filter(Q(group_name__startswith=fn) | Q(group_id__startswith=fn))
    for group in queryset:
        response += group.get_info() + '<br> ______________ <br><br>'
    # return HttpResponse(response)group_id
    # print('queryset.query')
    # print(queryset.query)
    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})


# ----------------------------------------------------------------------------

def groups_add(request):

    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            print('DATA SAVE')
            return HttpResponseRedirect('/groups/')
        else:
            print('TRY AGAIN')
            form = GroupsAddForm()
    else:
        form = GroupsAddForm()

    return render(request,
                  'groups_add.html',
                  context={'form': form})


# ----------------------------------------------------------------------------
# Вьюхи для  учителей
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    response = f'{teacher.get_info()}'
    return render(request,
                  'gen_teacher.html',
                  context={'teacher_gen': response})


# ----------------------------------------------------------------------------
def teachers(request):
    queryset = Teacher.objects.all()
    response = ''

    # print("request.GET.get('first_name')")
    fn = request.GET.get('data')
    if fn:
        queryset = queryset.filter(Q(first_name__startswith=fn) | Q(last_name__startswith=fn) | Q(email__startswith=fn))
    for teacher in queryset:
        response += teacher.get_info() + '<br> ______________ <br><br>'
    # return HttpResponse(response)
    print('queryset.query')
    print(queryset.query)
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})


# ----------------------------------------------------------------------------

def teachers_add(request):

    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            print('DATA SAVE')
            return HttpResponseRedirect('/teachers/')
        else:
            print('TRY AGAIN')
            form = TeachersAddForm()
    else:
        form = TeachersAddForm()

    return render(request,
                  'teachers_add.html',
                  context={'form': form})


# ----------------------------------------------------------------------------
# Вьюха стартовой страницы
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
def index(request):
    return render(request,
                  'index.html',
                  context={})
# ----------------------------------------------------------------------------

